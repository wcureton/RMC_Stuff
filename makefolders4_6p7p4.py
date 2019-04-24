#!/Applications/User/bin/python

import os
from shutil import copy

inp = int(input('How many run folders would you like?: '))
i = 1

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text 
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


files = [f for f in os.listdir('.') if os.path.isfile(f)]


for file in [f for f in os.listdir('.') if f.endswith('.rmc6f')]:
    stem_name, rmc6f_ext = os.path.splitext(file) # setting stem_name equal to basename of .rmc6f file

print(stem_name)

while i <= inp:
    path = 'run_{}'.format(i)
    os.mkdir(path)
    for f in files:
        if f.endswith('.pbs'):
            command = 'run_rmcprofile {} > {}_out'.format(stem_name, path)
            replace_line(f, 6, command)
        copy(f, path)
    i = i + 1
