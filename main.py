import subprocess

# Check if Google Chrome is installed
try:
    subprocess.check_output(['which', 'google-chrome-stable'])
except subprocess.CalledProcessError:
    print("Google Chrome is not installed")
    exit()

# Launch Google Chrome
subprocess.Popen(['google-chrome-stable'])

# Get the version of Google Chrome
version_info = subprocess.check_output(['google-chrome-stable', '--version']).decode().strip()
print("Google Chrome version:", version_info.split()[-1])
