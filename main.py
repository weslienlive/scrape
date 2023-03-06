import subprocess

chrome_path = subprocess.check_output(['which', 'google-chrome-stable']).decode().strip()
print("Chrome path is:", chrome_path)
