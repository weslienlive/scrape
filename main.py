import distro
import subprocess

# Get the distribution name
distname = distro.id()

# Set the name of the Google Chrome binary based on the distribution
if distname == "ubuntu" or distname == "debian":
    chrome_binary = "google-chrome-stable"
elif distname == "fedora" or distname == "centos" or distname == "rhel":
    chrome_binary = "google-chrome"
elif distname == "arch":
    chrome_binary = "google-chrome-stable"
elif distname == "opensuse":
    chrome_binary = "google-chrome-stable"
else:
    print("Unsupported Linux distribution")
    exit()

# Check if Google Chrome is installed
try:
    subprocess.check_output(['which', chrome_binary])
except subprocess.CalledProcessError:
    print("Google Chrome is not installed")
    exit()

# Launch Google Chrome
subprocess.Popen([chrome_binary])

# Get the version of Google Chrome
version_info = subprocess.check_output([chrome_binary, '--version']).decode().strip()
print("Google Chrome version:", version_info.split()[-1])
