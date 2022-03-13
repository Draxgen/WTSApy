'''
Creates a bat file with all python scripts and runs the bat file so the python scripts in parallel in the background. 
This script should be added to windows' Startup folder to be run at Startup
'''
__author__ = 'Jan Tuziak'

import os
import sys
import subprocess
import glob

def main():
    #get this script name
    this_script = os.path.basename(__file__)

    # get working folder and set it
    main_folder = os.path.join(sys.path[0], 'Scripts')
    os.chdir(main_folder)

    # get python scripts to run
    scripts = []
    for file in glob.glob('*.py'):
        scripts.append(file)

    # if no scripts found stop execution
    if not scripts: return
        
    # create batch file text
    bat = ''
    for scr in scripts:
        path = os.path.join(main_folder, scr)
        bat += f'start "" pythonw "{path}"\n'

    # create batch file
    bat_path = os.path.join(main_folder, 'scripts.bat')
    f = open(bat_path, 'w')
    f.write(bat)
    f.close()

    # call batch file
    subprocess.call(bat_path)

    # remove batdh file
    os.remove(bat_path)    

if __name__ == '__main__':
    main()
    