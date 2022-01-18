from ast import arg
import imp
from subprocess import run
from sys import argv

def ship() -> None:
    """
    quick form packageing tool that runs the autodoc tool and pushes code to github

    executes:
    doxygen cccs_autodoc_file
    git add.
    git commit -m "quick push"
    git push
    """

    run(['doxygen', 'cccs_autodoc_file'])
    # import os
    # os.execl('doxygen', 'cccs_autodoc_file')
    run('git add .', shell=True)
    run('git commit -m "quick push"', shell=True)
    run('git push', shell=True)

def deploy() -> None:
    run('git pull', shell=True)
    run(['doxygen', 'cccs_autodoc_file'])

    


if __name__ == "__main__":
    print(argv)

    if argv[1] == "ship": ship()
    elif argv[1] == "delpoy": ship()