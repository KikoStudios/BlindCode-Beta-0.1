import os

# Get the current username
current_username = os.getlogin()

# Define the new username
new_username = "kryst"

# Input path with the current username
current_path = os.path.join(r"C:\Users", current_username, "Documents", "ArduinoData")

# Replace the current username with the new username in the path
new_path = current_path.replace(current_username, new_username)

# Check if the new path exists before attempting to use it
if os.path.exists(new_path):
    print(f"Current path: {current_path}")
    print(f"New path: {new_path}")
else:
    print(f"The new path does not exist: {new_path}")