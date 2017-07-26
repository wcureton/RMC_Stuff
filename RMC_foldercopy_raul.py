# This is a python script to copy contents of a 'master' folder to 'run_#' subfolders
# The user can make as many subfolders as desired
# If there is a .pbs file in the master folder, the file can be modified before copying
# Available .pbs modifications include: file name, RMC stem name, gen of nodes, output file name

# Last modified by: Raul Palomares 07/14/2017

import os
import shutil

folder_n = int(raw_input('How many run folders would you like?: '))

stem_n = raw_input('What is the stem name?: ') # stem name from RMC files

gen = int(raw_input('Which generation of nodes are you using?: '))

def replace_line(file_name, line_num, text): # defining function to replace lines in a file
    lines = open(file_name, 'r').readlines() # reads all lines from file_name
    lines[line_num] = text # replacing line# 'line_num' with new text
    out = open(file_name, 'w') # opening file to re-write
    out.writelines(lines) # overwrite all the lines with new ones
    out.close() # close the output file

def copy_rename(old_file_name, new_file_name, subfolder_name): # defining function to copy and rename a file
        master_dir = os.curdir # define path for master folder
        run_dir = os.path.join(os.curdir, subfolder_name) # define path for subfolder
        master_file = os.path.join(master_dir, old_file_name) # define original file
        shutil.copy(master_file,run_dir) # copy original file to subfolder
        copied_file = os.path.join(run_dir, old_file_name) # copied file with old name
        new_copied_file = os.path.join(run_dir, new_file_name) # copied file with new name
        os.rename(copied_file, new_copied_file) # overwrite old with new copied file

files = [f for f in os.listdir('.') if os.path.isfile(f)] # make a list of all files

i = 1

while i <= (folder_n):
	run_n = 'run_{}'.format(i) # setting 'run_n' equal to 'run_#'
	os.mkdir(run_n) # making new run_# subfolder
	for f in files:
		if f.endswith('.pbs'): # modify the file if it is the pbs file...
			pbs_mod = os.path.join(os.curdir, f) # defining original pbs file to be modified
			shutil.copy2(pbs_mod, os.path.join(os.curdir, 'temp_pbs')) # making a temporary copy of the un-modified pbs file
			pbs_unmod = os.path.join(os.curdir, 'temp_pbs') # defining temporary unmodified pbs file
			
			gen_line = '#PBS -q gen{}\n'.format(gen)
			replace_line(f, 2, gen_line) # replacing line 2 of .pbs file
			
			ncommand = '/home/rpalomar/RMCProfile_package/exe/rmcprofile {} > {}_{}out'.format(stem_n, stem_n, run_n)
			replace_line(f, 7, ncommand) # replacing line 7 of .pbs file
			
			copy_rename(f, stem_n+'_'+run_n+'.pbs', run_n) # copy modified pbs file to run_# subfolder and rename pbs file
			os.rename(pbs_unmod, pbs_mod) # overwrite modified pbs in master folder with unmodified (temporary) version
		else:
			shutil.copy(f, run_n) # all other files are only copied and not modified
	i = i + 1