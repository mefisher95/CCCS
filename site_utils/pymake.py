from subprocess import run

def make():

    run('doxygen cccs_autodoc_file', shell=True)
    run('git add .', shell=True)
    run('git commit -m "quick push"', shell=True)
    run('git push', shell=True)

make()