import os
import subprocess

def main():
    # Path to the virtual environment activation script
    activate_script = os.path.join(".venv", "bin", "activate") if os.name != "nt" else os.path.join(".venv", "Scripts", "activate.bat")
    
    if not os.path.exists(".venv"):
        print("Error: .venv environment does not exist.")
        return

    try:
        # Activate the virtual environment and run pip freeze
        command = f"source {activate_script} && pip freeze > requirements.txt" if os.name != "nt" else f"{activate_script} && pip freeze > requirements.txt"
        subprocess.run(command, shell=True, check=True, executable="/bin/bash" if os.name != "nt" else None)
        print("requirements.txt has been successfully updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()