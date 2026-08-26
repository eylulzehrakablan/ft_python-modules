# Entering the Matrix (ex0)

## Problem: the global environment
when we install python on our computer, it comes with a **global environment**. if a we install a package (like a tool), it goes into this global space. 

imagine if every project you ever worked on had to share the same tools and versions.

Project A might need an older version of a tool, while project B need the newest one. if you update the tool for project B, you break project A. 

## Solution: The Construct (virtual environment)
a **virtual environment** is a self-contained directory yree that contains a python installation for a particular version of python, plus a number of additional packages.

when you create a virtual environment, you are creating a **clean isolated space** to work.
> **isolated:** packages installed here do not affect the global environment, and the global environment does not affect this space.
> **safe:** you can experiment, install dependencies and build pipelines without breaking other projects on your computer

in our project; the script `construct.py` acts as an environment scanner. it looks at the system paths and environment variables to determine if you are currently running inside the global enviroment or inside a safe virtual environment


## How to create virtual environments

to create a virtual environment in python usinf the command-line tool venv: 

`python3 -m venv <target_directory>`

> **-m**: stands for module-name. it changes where python looks for the script. when you add -m before 'venv', you are telling python that it should look for a built-in module named venv and run that module as an executable script.
    - without **-m** (python3 venv.py): you are handing python a file that you have on your library
    - without **-m** (python -m venv): you are asking python to go fetch a tool built directly into its master library

> **venv**: the name of the built-in python standart library module responsible for creating virtual environments.

> **<target_directory>**: the target directory name where the virtual environment will be created. you can name this folder anything. (.venv, env, matrix_env)


1. create the environment inside the project directory: `python3 -m venv matrix_env`

2. before installing packages or runnin to project within the construct, 

you must activate it with: `source matrix_env/bin/activate` or `. matrix_env/bin/activate`
    - once activated, the terminal prompt will show (matrix_env) prefixed to the shell prompt. any package installed via a package manager will now go into `matrix_env/lib/python3.x/site-packages` instead of your global environment.

3. when you are done working and want to return to your global environment: `deactivate`

### Source command
When you run a regular script (like ./script.sh), the system creates a child subshell to execute it. which means: 

- Subshell execution: the parent shell invokes the fork() and execve() system calls to spawn a child process with its own isolated memory address space. any modificatipns to environment variables (export key=value), functions or working directory exists strictly within the stack of that child process and are discarded upon process exit (exit 0)

- Sourced execution (source script.sh / . script.sh): the current shell process reads, parses and executes the commands directly within its own runtime. all environment variables assignments, alias declarations and state changes directly in the parent process's environment.

**source** command: is a shell built-in used to executes a script *inside the current terminal process* rather than launching a new temporary background process (a subshell). 
    
**dot operator (.)** can also be used instead of *source*. the only difference is that **"."** is the POSIX-standart command for executing commands from a file; while source is a synonym provided by Bash and some other shells.