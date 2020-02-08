
# ----------------------------------------
# PREAMBLE:
# ----------------------------------------

import MDAnalysis
import sys

# ----------------------------------------
# FUNCTIONS: 
# ----------------------------------------
def trajectory_analysis_config_parser(config_file,parameters):	# Function to take config file and create/fill the parameter dictionary 
        """ Function to take config file and create/fill the parameter dictionary (created before function call). 
        
        Usage: 
            parameters = {}     # initialize the dictionary to be filled with keys and values
            trajectory_analysis_config_parser(config_file,parameters)

        Arguments:
            config_file: string object that corresponds to the local or global position of the config file to be used for this analysis.

        """
        necessary_parameters = ['output_directory','node_selection_file','trajectory_functions_file','pdb','trajectory_list','substrate_node_definition','substrate_selection_string']
        all_parameters = ['output_directory','node_selection_file','trajectory_functions_file','pdb','trajectory_list','substrate_node_definition','substrate_selection_string','summary_boolean','nonstandard_substrates_selection','homemade_selections','alignment_node_definition','alignment_selection_string','trajectory_step','contact_map_distance_cutoff','which_contact_map']
        for i in range(len(necessary_parameters)):
            parameters[necessary_parameters[i]] = ''
	
        # SETTING DEFAULT PARAMETERS FOR OPTIONAL PARAMETERS:
        parameters['summary_boolean'] = False 
        parameters['nonstandard_substrates_selection'] = None
        parameters['homemade_selections'] = None
        parameters['alignment_node_definition'] = 'ATOMIC'
        parameters['alignment_selection_string'] = 'protein and name CA'
        parameters['trajectory_step'] = 1
        parameters['contact_map_distance_cutoff'] = 99999.9
        parameters['which_contact_map'] = 'average contact map'
        
        # GRABBING PARAMETER VALUES FROM THE CONFIG FILE:
        with open(config_file) as f:
            exec(compile(f.read(),config_file,'exec'),parameters)
        
        for key, value in list(parameters.items()):
            if value == '':
                print('%s has not been assigned a value. This variable is necessary for the script to run. Please declare this variable within the config file.' %(key))
                sys.exit()

def trajectory_analysis_summary(summary_file_name,arguments,parameters):
        """ Function to create a text file that holds important information about the analysis that was just performed. Outputs the version of MDAnalysis, how to rerun the analysis, and the parameters used in the analysis.

        Usage:
            trajectory_analysis_summary(summary_file_name,arguments,parameters)

        Arguments:
            summary_file_name: string object of the file name to be written that holds the summary information.
            parameters: dictionary object filled with the parameters used in the analysis.

        """
        with open(summary_file_name,'w') as f:
            f.write('Using MDAnalysis version: %s\n' %(MDAnalysis.version.__version__))
            f.write('\nAtom selections analyzed have been written out to node_selections.txt\n')
            f.write('To recreate this analysis, run this line:\n')
            for i in range(len(arguments)):
                f.write('%s ' %(arguments[i]))
            f.write('\n\n')
            f.write('Parameters used:\n')
            for key, value in list(parameters.items()):
                if key == '__builtins__':
                    continue
                if type(value) == int or type(value) == float:
                    f.write("%s = %s\n" %(key,value))
                else:
                    f.write("%s = '%s'\n" %(key,value))

def create_hessian_config_parser(config_file,parameters):	# Function to take config file and create/fill the parameter dictionary 
        """ Function to take config file and create/fill the parameter dictionary (created before function call). 
        
        Usage: 
            parameters = {}     # initialize the dictionary to be filled with keys and values
            trajectory_analysis_config_parser(config_file,parameters)

        Arguments:
            config_file: string object that corresponds to the local or global position of the config file to be used for this analysis.

        """
        necessary_parameters = ['output_directory','hessian_algorithm','system_covariance_file','system_average_structure_file','hessian_functions_file']

        all_parameters = ['output_directory','hessian_algorithm','system_covariance_file','system_average_structure_file','hessian_functions_file','summary_boolean','plotting_boolean','initial_guess_hessian','henm_alpha','henm_max_iterations','henm_threshold','temperature']
        
        for i in range(len(necessary_parameters)):
            parameters[necessary_parameters[i]] = ''
        
        # SETTING DEFAULT PARAMETERS FOR OPTIONAL PARAMETERS:
        parameters['summary_boolean'] = False 
        parameters['plotting_boolean'] = False 
        parameters['initial_guess_hessian'] = None
        parameters['henm_alpha'] = 1E-2
        parameters['henm_max_iterations'] = 100
        parameters['henm_threshold'] = 1E-4
        parameters['temperature'] = 303.
        #parameters[''] = 
        
        # GRABBING PARAMETER VALUES FROM THE CONFIG FILE:
        with open(config_file) as f:
            exec(compile(f.read(),config_file,'exec'),parameters)
        
        for key, value in list(parameters.items()):
            if value == '':
                print('%s has not been assigned a value. This variable is necessary for the script to run. Please declare this variable within the config file.' %(key))
                sys.exit()

def create_hessian_summary(summary_file_name,arguments,parameters):
        """ Function to create a text file that holds important information about the analysis that was just performed. Outputs the version of MDAnalysis, how to rerun the analysis, and the parameters used in the analysis.

        Usage:
            create_hessian_analysis_summary(summary_file_name,arguments,parameters)

        Arguments:
            summary_file_name: string object of the file name to be written that holds the summary information.
            parameters: dictionary object filled with the parameters used in the analysis.

        """
        with open(summary_file_name,'w') as f:
            f.write('To recreate this analysis, run this line:\n')
            for i in range(len(arguments)):
                f.write('%s ' %(arguments[i]))
            f.write('\n\n')
            f.write('Parameters used:\n')
            for key, value in list(parameters.items()):
                if key == '__builtins__':
                    continue
                if type(value) == int or type(value) == float:
                    f.write("%s = %s\n" %(key,value))
                else:
                    f.write("%s = '%s'\n" %(key,value))

