from uncertainties import ufloat, umath, unumpy
import numpy as np
from tsunami_ip_utils.readers import RegionIntegratedSdfReader, read_uncertainty_contributions_out, read_uncertainty_contributions_sdf
from tsunami_ip_utils._error import _unit_vector_uncertainty_propagation, _dot_product_uncertainty_propagation
from copy import deepcopy
from typing import List, Set, Tuple, Dict, Union, Optional
from pathlib import Path
from uncertainties.core import Variable
from tsunami_ip_utils.utils import _convert_paths
import os
from tempfile import NamedTemporaryFile
import tempfile
from string import Template
import subprocess
from tsunami_ip_utils.readers import read_integral_indices
from tsunami_ip_utils.utils import modify_sdf_names

def _calculate_E_from_sensitivity_vecs(application_vector: unumpy.uarray, experiment_vector: unumpy.uarray, 
                                      application_filename: Path=None, experiment_filename: Path=None, 
                                      uncertainties: str='automatic', experiment_norm: Variable=None, 
                                      application_norm: Variable=None) -> Variable:
    """Calculates the integral index: E given the sensitivity vectors for an application and an experiment. **NOTE**: the 
    application and experiment filenames are used to break the correlation between the application and experiment vectors 
    (that should not exist). This is because the vectors are only correlated if the application and experiment are the same.
    
    Parameters
    ----------
    application_vector
        Sensitivity vector for the application.
    experiment_vector
        Sensitivity vector for the experiment.
    application_filename
        Filename of the application sdf file (only needed for automatic uncertianty propagation).
    experiment_filename
        Filename of the experiment sdf file (only needed for automatic uncertianty propagation).
    uncertainties
        Type of error propagation to use. Default is 'automatic' which uses the uncertainties package.
        If set to 'manual', then manual error propagation is used which is generally faster
    experiment_norm
        Norm of the experiment vector. If not provided, it is calculated. This is mainly used for
        calculating E contributions, where the denominator is not actually the norm of the application and experiment
        vectors.
    application_norm
        Norm of the application vector. If not provided, it is calculated. This is mainly used for
        calculating E contributions, where the denominator is not actually the norm of the application and experiment
        vectors.
        
    Returns
    -------
        Similarity parameter between the application and the experiment"""
    
    norms_not_provided = ( experiment_norm == None ) and ( application_norm == None )
    if uncertainties == 'automatic': # Automatic error propagation with uncertainties package
        if application_filename == None or experiment_filename == None:
            raise ValueError("Application and experiment filenames must be provided for automatic error propagation")
        
        if norms_not_provided:
            application_norm = umath.sqrt(np.sum(application_vector**2))
            experiment_norm = umath.sqrt(np.sum(experiment_vector**2))
        
        application_unit_vector = application_vector / application_norm
        experiment_unit_vector = experiment_vector / experiment_norm

        # For some reason, the above introduces a correlation between the application and experiment vectors
        # which should only be the case if the application and the experiment are the same, so we manually 
        # break this correlation otherwise
        
        if application_filename != experiment_filename:
            # Break dependency to treat as independent
            application_unit_vector = np.array([ufloat(v.n, v.s) for v in application_unit_vector])
            experiment_unit_vector = np.array([ufloat(v.n, v.s) for v in experiment_unit_vector])

        dot_product = np.dot(application_unit_vector, experiment_unit_vector)

        E = dot_product
        return E

    else:
        # Manual error propagation

        # Same calculation for E
        if norms_not_provided:
            application_norm = umath.sqrt(np.sum(application_vector**2))
            experiment_norm = umath.sqrt(np.sum(experiment_vector**2))

        application_unit_vector = application_vector / application_norm
        experiment_unit_vector = experiment_vector / experiment_norm

        dot_product = np.dot(application_unit_vector, experiment_unit_vector)
        E = dot_product.n
        
        # ------------------------------------------
        # Now manually perform the error propagation
        # ------------------------------------------

        """Idea: propagate uncertainty of components of each sensitivity vector to the normalized sensitivty vector
        i.e. u / ||u|| = u^, v / ||v|| = v^
        
        E = u^ . v^

        Since u^ and v^ are completely uncorrelated, we may first calculate the uncertainty of u^ and v^ separately then
        use those to calculate the uncertainty of E."""

        # Calculate the uncertainties in the unit vectors
        application_unit_vector_error = _unit_vector_uncertainty_propagation(application_vector)
        experiment_unit_vector_error = _unit_vector_uncertainty_propagation(experiment_vector)

        # Construct application and experiment unit vectors as unumpy.uarray objects
        application_unit_vector = unumpy.uarray(unumpy.nominal_values(application_unit_vector), \
                                                    application_unit_vector_error)
        experiment_unit_vector = unumpy.uarray(unumpy.nominal_values(experiment_unit_vector), experiment_unit_vector_error)

        # Now calculate error in dot product to get the uncertainty in E
        E_uncertainty = _dot_product_uncertainty_propagation(application_unit_vector, experiment_unit_vector)

        return ufloat(E, E_uncertainty)


def _create_sensitivity_vector(sdfs: List[unumpy.uarray]) -> unumpy.uarray:
    """Creates a senstivity vector from all of the sensitivity profiles from a specific application or experiment
    by concatenating them together.

    Examples
    --------
    >>> sdfs = [ unumpy.uarray( [1, 2, 3], [0.1, 0.2, 0.3] ), unumpy.uarray( [4, 5, 6], [0.4, 0.5, 0.6] ) ]
    >>> _create_sensitivity_vector(sdfs)
    array([1.0+/-0.1, 2.0+/-0.2, 3.0+/-0.3, 4.0+/-0.4, 5.0+/-0.5, 6.0+/-0.6],
          dtype=object)
    
    Parameters
    ----------
        List of sensitivity profiles for each nuclide-reaction pair in consideration.
    
    Returns
    -------
        Sensitivities from all of the sensitivity profiles combined into a single vector of length
        ``sum( [ len(sdf_profile) for sdf_profile in sdfs ] )``"""
    uncertainties = np.concatenate([unumpy.std_devs(sdf) for sdf in sdfs])
    senstivities = np.concatenate([unumpy.nominal_values(sdf) for sdf in sdfs])

    return unumpy.uarray(senstivities, uncertainties)


def calculate_E(application_filenames: Union[List[str], List[Path]], experiment_filenames: Union[List[str], List[Path]], 
                reaction_type: str='all', uncertainties: str='manual') -> np.ndarray:
    """Calculates the similarity parameter, E for each application with each available experiment given the application 
    and experiment sdf files
    
    Parameters
    ----------
    application_filenames
        Paths to the application sdf files.
    experiment_filenames
        Paths to the experiment sdf files.
    reaction_type 
        The type of reaction to consider in the calculation of E. Default is ``'all``' which considers all 
        reactions.
    uncertainties 
        The type of uncertainty propagation to use. Default is ``'automatic'`` which uses the uncertainties
        package for error propagation. If set to ``'manual'``, then manual error propagation is used.
    
    Returns
    -------
        Similarity parameter for each application with each experiment, shape: ``(len(application_filenames), len(experiment_filenames))``"""

    # Read the application and experiment sdf files

    application_sdfs = [ RegionIntegratedSdfReader(filename).convert_to_dict() for filename in application_filenames ]
    experiment_sdfs  = [ RegionIntegratedSdfReader(filename).convert_to_dict() for filename in experiment_filenames ]

    # Create a matrix to store the similarity parameter E for each application with each experiment
    E_vals = unumpy.umatrix(np.zeros( ( len(experiment_sdfs), len(application_sdfs) ) ), \
                            np.zeros( ( len(experiment_sdfs), len(application_sdfs) ) ))
    
    # Now calculate the similarity parameter E for each application with each experiment
    for i, experiment in enumerate(experiment_sdfs):
        for j, application in enumerate(application_sdfs):
            # Now add missing data to the application and experiment dictionaries
            all_isotopes = set(application.sdf_data.keys()).union(set(experiment.sdf_data.keys()))
            _add_missing_reactions_and_nuclides(application.sdf_data, experiment.sdf_data, all_isotopes)
            
            # Sometimes the application and experiment dictionaries have different orders, which causes their sensitivity
            # profiles and hence sensitivity vectors to be different. To fix this, we need to sort the dictionaries

            # Sort the application by the experiment keys
            application.sdf_data = { isotope: { reaction: application.sdf_data[isotope][reaction] \
                                               for reaction in experiment.sdf_data[isotope] } \
                                                for isotope in experiment.sdf_data.keys() }

            application_profiles = application.get_sensitivity_profiles()
            experiment_profiles  = experiment.get_sensitivity_profiles()

            application_vector = _create_sensitivity_vector(application_profiles)
            experiment_vector  = _create_sensitivity_vector(experiment_profiles)

            E_vals[i, j] = _calculate_E_from_sensitivity_vecs(application_vector, experiment_vector, \
                                                             application_filenames[j], experiment_filenames[i], uncertainties)

    return E_vals

def _get_reaction_wise_E_contributions(application: dict, experiment: dict, isotope: str, all_reactions: List[str], 
                                      application_norm: Variable, experiment_norm: Variable) -> List[dict]:
    """Calculate contributions to the similarity parameter E for each reaction type for a given isotope.
    
    Parameters
    ----------
    application
        Dictionary of application sensitivity profiles.
    experiment
        Dictionary of experiment sensitivity profiles.
    isotope
        Isotope to consider.
    all_reactions
        List of all possible reaction types.
    application_norm
        Norm of the application sensitivity vector.
    experiment_norm
        Norm of the experiment sensitivity vector.
    
    Returns
    -------
        List of dictionaries containing the contribution to the similarity parameter E for each
        reaction type."""
    
    E_contributions = []
    for reaction in all_reactions:
        application_vector = application[isotope][reaction]['sensitivities']
        experiment_vector = experiment[isotope][reaction]['sensitivities']

        E_contribution = _calculate_E_from_sensitivity_vecs(application_vector, experiment_vector, uncertainties='manual', \
                                                           application_norm=application_norm, experiment_norm=experiment_norm)
        E_contributions.append({
            "isotope": isotope,
            "reaction_type": reaction,
            "contribution": E_contribution
        })

    return E_contributions

def _add_missing_reactions_and_nuclides(application: dict, experiment: dict, all_isotopes: List[str], 
                                       mode: str='sdfs') -> Set[str]:
    """Add missing reactions and nuclides to the application and experiment dictionaries with an sdf profile of all zeros.
    The set of all isotopes 
    **NOTE**: since dictionaries are passed by reference, this function does not return anything, but modifies the
    application and experiment dictionaries in place.
    
    Parameters
    ----------
    application
        Dictionary of application sensitivity profiles.
    experiment
        Dictionary of experiment sensitivity profiles.
    all_isotopes
        List of all isotopes in the application and experiment dictionaries.
    mode
        The mode to use for adding missing reactions and nuclides. Default is ``'sdfs'`` which adds sdf profiles to missing
        reactions and nuclides. If set to ``'contribution'``, then the contributions to the similarity parameter E are set to zero
        for missing nuclides and reactions.
    
    Returns
    -------
        Set of all isotopes in the application and experiment dictionaries."""
    # Whether or not the supplied data is only isotopes or includes reactions
    isotopes_only =  type( application[ list( application.keys() )[0] ] ) != dict

    if not isotopes_only:
        application_reactions = set([ key for isotope in application.keys() for key in application[isotope].keys() ])
        experiment_reactions = set([ key for isotope in experiment.keys() for key in experiment[isotope].keys() ])
        all_reactions = application_reactions.union(experiment_reactions)

        # Now, for any reactions that are in experiment but not application (and vice versa), they need to be added with an sdf
        # profile of all zeros

        # Get an arbitrary sdf profile to get the shape from
        first_application_nuclide = list(application.keys())[0]
        first_application_reaction = list(application[first_application_nuclide].keys())[0]
        if mode == 'sdfs':
            zero_data = {
                'sensitivities': application[first_application_nuclide][first_application_reaction]['sensitivities']
            }
        elif mode == 'contribution':
            zero_data = ufloat(0,0)

        # Now define a function used for updating the reactions for a given isotope
        def update_reactions(isotope):
            for reaction in all_reactions:
                if reaction not in isotope.keys():
                    isotope[reaction] = deepcopy(zero_data)
    else:
        # No reactions, only isotope totals
        all_reactions = []

        if mode == 'sdfs':
            zero_data = {
                'sensitivities': application[first_application_nuclide]['sensitivities']
            }
        elif mode == 'contribution':
            zero_data = ufloat(0,0)

    # ---------------------------------------
    # Now add missing reactions and nuclides
    # ---------------------------------------
    if not isotopes_only:
        for isotope in application.keys():
            # If reaction is missing for this isotope, add it with an sdf profile of all zeros
            update_reactions(application[isotope])

        for isotope in experiment.keys():
            # If reaction is missing for this isotope, add it with an sdf profile of all zeros
            update_reactions(experiment[isotope])

    # Now zero out nuclides that are not in the application or experiment
    for isotope in all_isotopes:
        if isotope not in application.keys():
            if not isotopes_only:
                application[isotope] = { reaction: deepcopy(zero_data) for reaction in all_reactions }
            else:
                application[isotope] = deepcopy(zero_data)
            
        if isotope not in experiment.keys():
            if not isotopes_only:
                experiment[isotope] = { reaction: deepcopy(zero_data) for reaction in all_reactions }
            else:
                experiment[isotope] = deepcopy(zero_data)

    return all_reactions

def _get_nuclide_and_reaction_wise_E_contributions(application: RegionIntegratedSdfReader, experiment: RegionIntegratedSdfReader
                                                   ) -> Tuple[List[dict], List[dict]]:
    """Calculate the contributions to the similarity parameter E for each nuclide and for each reaction type for a given
    application and experiment.
    
    Parameters
    ----------
    application
        Contains application sensitivity profile dictionaries.
    experiment
        Contains experiment sensitivity profile dictionaries.
    
    Returns
    -------
        * nuclide_wise_contributions
            List of dictionaries containing the contribution to the similarity parameter E.
            for each nuclide
        * nuclide_reaction_wise_contributions
            List of dictionaries containing the contribution to the similarity."""

    # First, extract the sensitivity vectors for the application and experiment
    
    # Calculate |S_A| and |S_E| to normalize the E contributions properly

    application_vector = _create_sensitivity_vector(application.get_sensitivity_profiles())
    experiment_vector = _create_sensitivity_vector(experiment.get_sensitivity_profiles())

    application_norm = umath.sqrt(np.sum(application_vector**2))
    experiment_norm = umath.sqrt(np.sum(experiment_vector**2))

    # Now convert the application and experiment sdf's to dictionaries keyed by nuclide and reaction type
    application = application.convert_to_dict().sdf_data
    experiment  = experiment.convert_to_dict().sdf_data

    nuclide_wise_contributions = []
    nuclide_reaction_wise_contributions = []

    # All isotopes in the application and experiment
    all_isotopes = set(application.keys()).union(set(experiment.keys()))

    # Since different nuclides can have different reactions, we need to consider all reactions for each nuclide (e.g. 
    # fissile isotopes will have fission reactions, while non-fissile isotopes will not)
    all_reactions = _add_missing_reactions_and_nuclides(application, experiment, all_isotopes)

    for isotope in all_isotopes:

        # For isotope-wise contribution, the sensitivity vector is all of the reaction sensitivities concatenated together
        application_vector = _create_sensitivity_vector([ application[isotope][reaction]['sensitivities'] \
                                                        for reaction in all_reactions ] )
        experiment_vector  = _create_sensitivity_vector([ experiment[isotope][reaction]['sensitivities'] \
                                                        for reaction in all_reactions ])

        E_isotope_contribution = _calculate_E_from_sensitivity_vecs(application_vector, experiment_vector, uncertainties='manual',
                                                                   application_norm=application_norm, \
                                                                    experiment_norm=experiment_norm)

        nuclide_wise_contributions.append({
            "isotope": isotope,
            "contribution": E_isotope_contribution
        })

        # For nuclide-reaction-wise contribution, we need to consider each reaction type
        nuclide_reaction_wise_contributions += \
            _get_reaction_wise_E_contributions(application, experiment, isotope, all_reactions, \
                                              application_norm, experiment_norm)
        
    return nuclide_wise_contributions, nuclide_reaction_wise_contributions


def calculate_E_contributions(application_filenames: List[str], experiment_filenames: List[str]
                              ) -> Tuple[Dict[str, unumpy.uarray], Dict[str, unumpy.uarray]]:
    """Calculates the contributions to the similarity parameter E for each application with each available experiment 
    on a nuclide basis and on a nuclide-reaction basis.
    
    Parameters
    ----------
    application_filenames
        Paths to the application sdf files.
    experiment_filenames
        Paths to the experiment sdf files.
    
    Returns
    -------
        * E_contributions_nuclide
            Contributions to the similarity parameter E for each application with each
            experiment on a nuclide basis.
        * E_contributions_nuclide_reaction
            Contributions to the similarity parameter E for each application with
            each experiment on a nuclide-reaction basis."""
    
    application_sdfs = [ RegionIntegratedSdfReader(filename) for filename in application_filenames ]
    experiment_sdfs  = [ RegionIntegratedSdfReader(filename) for filename in experiment_filenames ]
    
    # Initialize np object arrays to store the E contributions
    E_nuclide_wise          = {'contribution': {'application': [], 'experiment': []}}
    E_nuclide_reaction_wise = {'contribution': {'application': [], 'experiment': []}}

    # Calculate contributions to E for each application
    for application in application_sdfs:
        nuclide_wise_contributions, nuclide_reaction_wise_contributions = \
            _get_nuclide_and_reaction_wise_E_contributions(application, application)

        E_nuclide_wise['contribution']['application'].append(nuclide_wise_contributions)
        E_nuclide_reaction_wise['contribution']['application'] = nuclide_reaction_wise_contributions

    # Calculate contributions to E for each experiment
    for experiment in experiment_sdfs:
        nuclide_wise_contributions, nuclide_reaction_wise_contributions = \
            _get_nuclide_and_reaction_wise_E_contributions(experiment, experiment)

        E_nuclide_wise['contribution']['experiment'].append(nuclide_wise_contributions)
        E_nuclide_reaction_wise['contribution']['experiment'] = nuclide_reaction_wise_contributions

    E_nuclide_wise['filenames'] = {
        'application': application_filenames,
        'experiment': experiment_filenames
    }

    E_nuclide_reaction_wise['filenames'] = {
        'application': application_filenames,
        'experiment': experiment_filenames
    }

    return E_nuclide_wise, E_nuclide_reaction_wise


@_convert_paths
def get_uncertainty_contributions(application_filenames: Optional[Union[ List[str], List[Path] ]]=None, 
                                  experiment_filenames: Optional[Union[ List[str], List[Path] ]]=None,
                                  variance: bool=False
                                  ) -> Tuple[ Dict[ str, List[unumpy.uarray] ], Dict[ str,  List[unumpy.uarray] ] ]:
    """Read the contributions to the uncertainty in :math:`k_{\\text{eff}}` (i.e. :math:`\\frac{dk}{k}`) for each 
    application and each available experiment on a nuclide basis and on a nuclide-reaction basis from the
    provided TSUNAMI-IP ``.out`` or ``.sdf`` files.

    Parameters
    ----------
    application_filenames
        (Optional) Paths to the application output (``.out``) or ``.sdf`` files.
    experiment_filenames
        (Optional) Paths to the experiment output (``.out``) or ``.sdf`` files.
    variance
        If the contributions to the nuclear data induced variance should be returned, default is ``False``.

    Returns
    -------
        - uncertainty_contributions_nuclide
            List of contributions to the uncertainty in :math:`k_{\\text{eff}}` for each application and 
            each experiment on a nuclide basis. Keyed by ``'application'`` and ``'experiment'``.
        - uncertainty_contributions_nuclide_reaction
            List of contributions to the uncertainty in :math:`k_{\\text{eff}}` for each application and each experiment 
            on a nuclide-reaction basis. Keyed by ``'application'`` and ``'experiment'``.
            
    Notes
    -----
    If either the application or experiment filenames are not provided, then the corresponding output will be an empty list.

    
    Theory
    ======
    The nuclear-data induced varaince in :math:`k_{\\text{eff}}` (defined in 
    `Equation 6.3.34 <https://scale-manual.ornl.gov/sams.html#equation-eq6-3-34>`_ ) can be decomposed into contributions 
    from each nulicde-reaction covariance via `Equation 6.3.35 <https://scale-manual.ornl.gov/sams.html#equation-eq6-3-35>`_
    in the SALE manual. The `total` uncertainty in :math:`k_{\\text{eff}}` (as well as the contributions on a nuclide-reaction
    wise basis) can be calculated from these two definitions by simply taking the square root. For nuclide-reaction covariances
    that are not principle submatrices, the contribution to the variance may be negative (as they are not guaranteed to be
    positive definite), and so the uncertainty contribution may be (formally) imaginary. However, these contributions physically
    represent anticorrelations in the nuclear data, and so TSUNAMI reports them as negative values, but with a note that there
    is a special rule for handling these values (see the footer of the ``Uncertainty Information`` section in
    `Example 6.6.3 <https://scale-manual.ornl.gov/sams.html#list6-3-3>`_ )."""
    
    dk_over_k_nuclide_wise = {
        'application': [],
        'experiment': [],
    }
    dk_over_k_nuclide_reaction_wise = {
        'application': [],
        'experiment': [],
    }

    application_filenames = application_filenames if application_filenames is not None else []
    experiment_filenames = experiment_filenames if experiment_filenames is not None else []
    all_filenames = application_filenames + experiment_filenames

    at_least_one_not_out = any([ filename.suffix != '.out' for filename in all_filenames ])
    all_sdf = all([ filename.suffix == '.sdf' for filename in application_filenames + experiment_filenames ])
    if at_least_one_not_out and not all_sdf:
        raise ValueError("All files must be either .out or .sdf files")
    
    if all_sdf:
        # Application
        if application_filenames != []:
            dk_over_k_nuclide_wise['application'], dk_over_k_nuclide_reaction_wise['application'] = \
                read_uncertainty_contributions_sdf(application_filenames)
        else:
            dk_over_k_nuclide_wise['application'] = []
            dk_over_k_nuclide_reaction_wise['application'] = []

        # Experiment
        if experiment_filenames != []:
            dk_over_k_nuclide_wise['experiment'], dk_over_k_nuclide_reaction_wise['experiment'] = \
                read_uncertainty_contributions_sdf(experiment_filenames)
        else:
            dk_over_k_nuclide_wise['experiment'] = []
            dk_over_k_nuclide_reaction_wise['experiment'] = []
    else:
        for i, application_filename in enumerate(application_filenames):
            dk_over_k_nuclide_wise['application'][i], dk_over_k_nuclide_reaction_wise['application'][i] = \
                read_uncertainty_contributions_out(application_filename)

        for i, experiment_filename in enumerate(experiment_filenames):
            dk_over_k_nuclide_wise['experiment'][i], dk_over_k_nuclide_reaction_wise['experiment'][i] = \
                read_uncertainty_contributions_out(experiment_filename)
            
    if variance:
        for key in dk_over_k_nuclide_wise.keys():
            # Now square all of the contributions for each system (application or experiment)
            for contributions_list in [dk_over_k_nuclide_wise[key], dk_over_k_nuclide_reaction_wise[key]]:
                for system in contributions_list:
                    for nuclide_index, contribution_dict in enumerate(system):
                        contribution = contribution_dict['contribution']
                        system[nuclide_index]['contribution'] = (contribution)**2 if contribution > 0 else -(contribution)**2

    # Add filenames to contribution dictionary for use by other functions
    dk_over_k_nuclide_wise['filenames'] = {
        'application': application_filenames,
        'experiment': experiment_filenames
    }
    dk_over_k_nuclide_reaction_wise['filenames'] = {
        'application': application_filenames,
        'experiment': experiment_filenames
    }
        
    return dk_over_k_nuclide_wise, dk_over_k_nuclide_reaction_wise

@_convert_paths
def get_integral_indices(application_sdfs: Union[ List[str], List[Path] ], experiment_sdfs: Union[ List[str], List[Path] ],
                         coverx_library='252groupcov7.1') -> Dict[str, unumpy.uarray]:
    """Gets the TSUNAMI-IP computed integral indices for a set of application and experiment sdfs
    
    Parameters
    ----------
    application_sdfs
        List of paths to the application SDF files.
    experiment_sdfs
        List of paths to the experiment SDF files.
    coverx_library
        The covariance library to use. Default is ``'252groupcov7.1'``. This must be explicitly specified, and must correspond
        to the multigroup library used to generate the SDF files.
    
    Returns
    -------
        Tuple of dictionaries containing the integral indices for the applications and experiments. The dictionaries have keys:
        ``'c_k'``, ``'E_total'``, ``'E_fission'``, ``'E_capture'``, and ``'E_scatter'``.
    """

    # Template the TSUNAMI-IP input file with the application and experiment filenames
    current_dir = Path(__file__).parent
    with open(current_dir / "input_files" / "tsunami_ip_base_input.inp", 'r') as f:
        input_template = Template(f.read())

    # -------------------------------------------
    # Modify the sdf file names to exclude spaces
    # -------------------------------------------
    # This is necessary for the reader to correctly parse the TSUNAMI-IP output
    output_directory = Path( tempfile.gettempdir() )
    modify_sdf_names(list(set(application_sdfs + experiment_sdfs)), output_directory=output_directory)

    # Update the application and experiment SDF paths to the paths to the SDFs with modified names
    application_sdfs = [ output_directory / sdf_file.name for sdf_file in application_sdfs ]
    experiment_sdfs = [ output_directory / sdf_file.name for sdf_file in experiment_sdfs ]

    # Convert the application and experiment SDF paths to strings
    application_sdfs = [ str(filename) for filename in application_sdfs ]
    experiment_sdfs = [ str(filename) for filename in experiment_sdfs ]

    # Now template the input file
    tsunami_ip_input = input_template.safe_substitute(
        application_filenames='\n'.join(application_sdfs),
        experiment_filenames='\n'.join(experiment_sdfs),
        coverx_library=coverx_library
    )

    # Now write the input file to a temorary file and run it
    with NamedTemporaryFile('w', delete=False) as f:
        f.write(tsunami_ip_input)
        input_filename = f.name

    # Run the TSUNAMI-IP calculation
    process = subprocess.Popen( ['scalerte', input_filename], cwd=str( Path( input_filename ).parent ) )
    process.wait()

    # Read the integral indices
    integral_matrices = read_integral_indices(f"{input_filename}.out")

    # Remove the temporary input and output files
    os.remove(input_filename)
    os.remove(f"{input_filename}.out")

    # Now remove the temporary SDF files with modified names
    for sdf_file in application_sdfs + experiment_sdfs:
        if Path(sdf_file).exists():
            os.remove(sdf_file)

    return integral_matrices