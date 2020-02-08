
# ----------------------------------------
# USAGE AND REFERENCING
# ----------------------------------------
#   python analyze_trajectory.py trajectory_analysis_config_file_name IO_functions_file

# ----------------------------------------
# CODE OUTLINE
# ----------------------------------------
#   Allosteric Paths in Proteins - Trajectory Analysis Code
#       1) Load in user defined parameters
#       2) Load in necessary functions from module files
#       3) Trajectory Analysis
#           a) Create the MDAnalysis.Universe object and desired atom selections
#           b) Analyze trajectories (or the user can read in the necessary matrices)
#               i)   Fill a numpy array with node positions
#               ii)  Calculate the average node positions using iterative alignment
#                   ### NOTE: NOT IMPLEMENTED YET 0) Calculate RMSD from average node positions to find a traj. frame that is most representative of the average structure
#               iii) Calculate the node cartesian covariance matrix
#               iv)  Calculate the node pair distances

# ----------------------------------------
# PREAMBLE:
# ----------------------------------------
import sys
import os
import importlib
import numpy as np
import MDAnalysis
#from IO import trajectory_analysis_config_parser,trajectory_analysis_summary

# ----------------------------------------
# VARIABLE DECLARATION: 
# ----------------------------------------

config_file = sys.argv[1]
IO_functions_file = sys.argv[2]

trajectory_analysis_config_parser = importlib.import_module(IO_functions_file.split('.py')[0],package=None).trajectory_analysis_config_parser
trajectory_analysis_summary = importlib.import_module(IO_functions_file.split('.py')[0],package=None).trajectory_analysis_summary

# ----------------------------------------
# FUNCTIONS: 
# ----------------------------------------

def main():
    # ----------------------------------------
    # 3a) CREATE THE MDAnalysis.Universe OBJECT AND DESIRED ATOM SELECTIONS
    # ----------------------------------------
    u = MDAnalysis.Universe(parameters['pdb'])
    selection_list = make_selections(u,parameters['output_directory'] + 'node_selections.txt',parameters['substrate_node_definition'],parameters['substrate_selection_string'], nonstandard_substrates_selection = parameters['nonstandard_substrates_selection'], homemade_selections = parameters['homemade_selections'])
    print('Number of analysis nodes:', len(selection_list), '\nNode selections written out to', parameters['output_directory'] + 'node_selections.txt')
    
    alignment_list = make_selections(u,parameters['output_directory'] + 'alignment_node_selections.txt',parameters['alignment_node_definition'],parameters['alignment_selection_string'], nonstandard_substrates_selection = parameters['nonstandard_substrates_selection'], homemade_selections = parameters['homemade_selections'])
    
    print('Number of alignment nodes:', len(alignment_list), '\nNode selections written out to', parameters['output_directory'] + 'alignment_node_selections.txt')
    
    # ----------------------------------------
    # 3b) ANALYZE TRAJECTORIES
    # ----------------------------------------
    # i) FILL A NUMPY ARRAY WITH NODE POSITIONS and ii) SIMULTANEOUSLY ALIGN THE NODE POSITIONS AND CALCULATE THE AVERAGE POSITIONS USING ITERATIVE ALIGNMENT
    # ----------------------------------------
    Node_trajectory, avg_Node_positions = traj_alignment_and_averaging(u,parameters['alignment_selection_string'],alignment_list,parameters['alignment_node_definition'],selection_list,parameters['substrate_node_definition'],parameters['trajectory_list'],parameters['output_directory'], step = parameters['trajectory_step'], convergence_threshold = 1E-5)
    
    # ----------------------------------------
    # iii) CALCULATE THE NODE CARTESIAN COVARIANCE MATRIX 
    # ----------------------------------------
    calc_cartesian_covariance(Node_trajectory,avg_Node_positions,parameters['output_directory'])
    
    # ----------------------------------------
    # iv) CALCULATE THE NODE PAIR DISTANCES
    # ----------------------------------------
    print('Beginning node pair distance calculation.')
    if parameters['which_contact_map'] == '75% trajectory':
        calc_contact_map(parameters['which_contact_map'],Node_trajectory,parameters['output_directory'],distance_cutoff = parameters['contact_map_distance_cutoff'])
    elif parameters['which_contact_map'] == 'average':
        calc_contact_map(parameters['which_contact_map'],avg_Node_positions,parameters['output_directory'],distance_cutoff = parameters['contact_map_distance_cutoff'])
    
    if parameters['summary_boolean']:
        trajectory_analysis_summary(parameters['output_directory'] + 'trajectory_analysis.summary',sys.argv,parameters)
        #summary(parameters['output_directory'] + 'trajectory_analysis.summary',sys.argv,parameters)

# ----------------------------------------
# 1) LOAD IN USER DEFINED PARAMETERS
# ----------------------------------------
parameters = {}
#config_parser(config_file,parameters)
trajectory_analysis_config_parser(config_file,parameters)

# ----------------------------------------
# SETTING UP THE OUTPUT DIRECTORY
# ----------------------------------------
if parameters['output_directory'][-1] != os.sep:
    parameters['output_directory'] += os.sep

if os.path.exists(parameters['output_directory']):
    print('The output directory, ', parameters['output_directory'], 'already exists. Please select a different directory name for output.')
    sys.exit()
else:
    os.mkdir(parameters['output_directory'])

# ----------------------------------------
# 2) LOAD IN NECESSARY FUNCTIONS FROM MODULE FILES
# ----------------------------------------

make_selections = importlib.import_module(parameters['node_selection_file'].split('.py')[0],package=None).make_selections
traj_alignment_and_averaging = importlib.import_module(parameters['trajectory_functions_file'].split('.py')[0],package=None).traj_alignment_and_averaging
calc_cartesian_covariance = importlib.import_module(parameters['trajectory_functions_file'].split('.py')[0],package=None).calc_cartesian_covariance
calc_contact_map = importlib.import_module(parameters['trajectory_functions_file'].split('.py')[0],package=None).calc_contact_map

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == '__main__':
    main()

