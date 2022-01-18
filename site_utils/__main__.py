        
# from Class import parse_class
# from Function import parse_functions
# from Dependencies import parse_dependencies, Module
# from File import File
# import os
# import ast
# import write_HTML

import subprocess

def main():
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "quick push"', shell=True)
    subprocess.run('git push', shell=True)



if __name__ == "__main__":
    main()