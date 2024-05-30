import subprocess
import os

try:
    if os.name == 'nt':  # Windows system
        # /c : Run Command and then terminate
        # /k : Run Command and then return to the CMD prompt
        # /b : Bare format (no heading information or summary)
        command = ["cmd.exe", "/c", "dir", "/b"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")
except subprocess.CalledProcessError as error:
    print(f"Error: {error}")
