# Imports
import os
import sys

if len(sys.argv) == 1: # script itself is an arg only
    print('Usage: init_dirs <box name>')
    print('Sets up directory templates for new HTB box')
    exit(-2)

path_to_create_from = '$some_path' # fill this out w/ your working dir for HTB
dirs_to_create = ['nmap','busters','exploits','loot','scripting']

path = path_to_create_from +  '/' + sys.argv[1] + '/'

print('Initializing directory at %s' % (path))

try:
    os.mkdir(path)
except OSError as e:
    print('Error creating path:\n%s' % (e))
    exit(-1)

for dir in dirs_to_create:
    create_path = path + dir
    print('Initializing subdir at %s ' % (create_path))
    try:
        os.mkdir(create_path)
    except OSError as e:
        print('Error initializing subdir:\n%s' % (e))
