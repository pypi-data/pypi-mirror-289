import sys
import subprocess
import os

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
    package_path = os.path.join(os.path.dirname(__file__), 'packages')
    if os.path.exists(package_path):
        sys.path.insert(0, package_path)

    with open(filename, 'r') as file:
        code = file.read()

    exec(code, globals())

def main():
    if len(sys.argv) < 2:
        print("Usage: streamsys <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'run':
        if len(sys.argv) != 3:
            print("Usage: streamsys run <filename.strS>")
            sys.exit(1)
        filename = sys.argv[2]
        if not filename.endswith('.strS'):
            print("File extension must be .strS")
            sys.exit(1)
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            sys.exit(1)
        run_file(filename)
    elif command == 'install':
        if len(sys.argv) != 3:
            print("Usage: streamsys install <package-name>")
            sys.exit(1)
        package_name = sys.argv[2]
        install_package(package_name)
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
