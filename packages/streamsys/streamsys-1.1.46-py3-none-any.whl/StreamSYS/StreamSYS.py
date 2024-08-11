import sys
import os
import subprocess
import urllib.request
import json

def get_current_version():
    version_file = os.path.join(os.path.dirname(__file__), 'vrs.txt')
    if not os.path.exists(version_file):
        return None
    with open(version_file, 'r') as file:
        return file.read().strip()

def check_for_update():
    current_version = get_current_version()
    if current_version is None:
        print("Version file not found. Unable to check for updates.")
        return

    try:
        url = "https://pypi.org/pypi/streamsys/json"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            pypi_version = data['info']['version']
    except Exception as e:
        print(f"Error checking for updates: {e}")
        return

    if current_version != pypi_version:
        print(f"A new version ({pypi_version}) is available!")
        print(f"Update using: pip install --upgrade streamsys")
    else:
        print("You are using the latest version.")

def install_package(package_name):
    package_path = os.path.join(os.path.dirname(__file__), 'packages')
    if not os.path.exists(package_path):
        os.makedirs(package_path)

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--target", package_path])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package '{package_name}'. Error: {e}")

def run_file(filename):
    package_path = os.path.dirname(__file__)
    sys.path.insert(0, package_path)

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        sys.exit(1)

    subprocess.run([sys.executable, filename])

def main():
    if len(sys.argv) < 2:
        print("Usage: streamsys <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'run':
        if len(sys.argv) != 3:
            print("Usage: streamsys run <filename.py>")
            sys.exit(1)
        filename = sys.argv[2]
        if not filename.endswith('.py'):
            print("File extension must be .py")
            sys.exit(1)
        run_file(filename)
    elif command == 'install':
        if len(sys.argv) != 3:
            print("Usage: streamsys install <package-name>")
            sys.exit(1)
        package_name = sys.argv[2]
        install_package(package_name)
    elif command == 'update':
        check_for_update()
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
