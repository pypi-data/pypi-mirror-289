import os
import subprocess

def streamsysLoad(script_path):
    # Check if the script file exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script file '{script_path}' not found.")

    # Add the StreamSYS directory to sys.path to enable module imports
    script_dir = os.path.dirname(script_path)
    os.sys.path.insert(0, script_dir)

    # Run the script
    subprocess.run([os.sys.executable, script_path], check=True)
