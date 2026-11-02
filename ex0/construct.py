import sys
import os
import site

if __name__ == "__main__":
    is_in_venv = sys.prefix != sys.base_prefix

    if is_in_venv:
        py_path = sys.executable
        env_path = sys.prefix
        venv_name = os.path.basename(env_path)
        package_path = site.getsitepackages()[0]

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {py_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(package_path)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
