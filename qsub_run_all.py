import os
import time

run_folders = 0 # Initialize counter
for item in os.listdir(os.curdir): # Obtains list of run directories
	if item.startswith('run') == True and os.path.isdir(item) == True:
		run_folders += 1

run_n=1 # Initialize counter
while run_n <= run_folders:
	run_dir = os.path.join(os.curdir, 'run_{}'.format(run_n)) # setting path for run folder
	for file in [f for f in os.listdir(run_dir) if f.endswith('.pbs')]: # lists all files in run directory and finds submission script
		os.chdir(run_dir) # changes to the run directory
		os.system('qsub {}'.format(file)) # runs the job submission script within the run directory
		os.chdir('..') # changes back to the master directory
	run_n += 1
	time.sleep(2) # two second pause
