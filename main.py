import subprocess

bin_contents = subprocess.check_output(['ls', '/root/.nix-profile/bin']).decode().strip().split('\n')
print("Contents of /root/.nix-profile/bin:")
for item in bin_contents:
    print(item)
