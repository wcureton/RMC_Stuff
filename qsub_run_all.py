import os
import time

run_folders = 0
for item in os.listdir(os.curdir):
	if item.startswith('run') == True and os.path.isdir(item) == True:
		run_folders += 1

run_n=1
while run_n <= run_folders:
	run_dir = os.path.join(os.curdir, 'run_{}'.format(run_n)) # setting path for run folder
	for file in [f for f in os.listdir(run_dir) if f.endswith('.pbs')]:
		os.chdir(run_dir)
		os.system('qsub {}'.format(file))
		os.chdir('..')
	run_n += 1
	time.sleep(2)
