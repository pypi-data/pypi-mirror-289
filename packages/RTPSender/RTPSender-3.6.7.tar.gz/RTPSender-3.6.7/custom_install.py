import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

def main():
    try:
        # Uninstall av if it exists
        run_command(f"{sys.executable} -m pip uninstall -y av")
        print("Uninstalled existing 'av' package.")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling 'av': {e.stderr}")

    try:
        # Install av with the --no-binary option
        run_command(f"{sys.executable} -m pip install av --no-binary av")
        print("Installed 'av' with --no-binary option.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing 'av': {e.stderr}")

if __name__ == "__main__":
    main()
