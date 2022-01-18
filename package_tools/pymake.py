from subprocess import run

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
