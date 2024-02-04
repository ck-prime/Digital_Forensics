import os
import platform
import psutil
import wmi
import sys
import ctypes

def identify_drives():
    drives = psutil.disk_partitions(all=True)
    drive_list = []
    for drive in drives:
        if 'removable' in drive.opts:
            drive_list.append(drive.device)
    return drive_list

def document_drive_specifications(drive):
    wmi_obj = wmi.WMI()
    drive_info = wmi_obj.query("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = '{}'".format(drive.rstrip('\\')))[0]
    print("Drive make: {}".format(drive_info.Caption))
    print("Drive capacity: {} GB".format(int(drive_info.Size) / (1024**3)))
    print("Drive model: {}".format(drive_info.Description))
    if hasattr(drive_info, 'InterfaceType'):
        print("Drive interface type: {}".format(drive_info.InterfaceType))
    else:
        print("Drive interface type: Unknown")

def setup_write_blocker(drive):
    # Implement your write-blocker setup logic here
    print("Setting up write-blocker...")

# Check if the script is running on Windows
if platform.system() != 'Windows':
    print("This script requires Windows platform.")
    sys.exit(1)

# Specify the directory where the drive list should be saved
directory = r"D:\workplace\forensics\drives"

# Step 1: Identify the drives
drive_list = identify_drives()

# Create a file with drive details
file_path = os.path.join(directory, "drive_list.txt")
with open(file_path, "w") as file:
    for drive in drive_list:
        file.write(drive + "\n")

# Display the available drives and ask for user input
print("Available drives:")
with open(file_path, "r") as file:
    drive_lines = file.readlines()
    for index, line in enumerate(drive_lines):
        print(f"{index + 1}. {line.strip()}")

# Ask the user to select the target drive
selection = int(input("Select the target drive number: "))
if 1 <= selection <= len(drive_list):
    target_drive = drive_lines[selection - 1].strip()
    print(f"Selected target drive: {target_drive}")
    document_drive_specifications(target_drive)
    setup_write_blocker(target_drive)
else:
    print("Invalid selection.")
