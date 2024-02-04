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

def list_directory_files(directory, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for root, dirs, files in os.walk(directory):
                file.write("Directory: {}\n".format(root))
                for file_name in files:
                    try:
                        file.write("File: {}\n".format(os.path.join(root, file_name)))
                    except UnicodeEncodeError:
                        pass
    except Exception as e:
        print("An error occurred while listing directories and files: {}".format(str(e)))

def restart_with_admin():
    if platform.system() != 'Windows':
        print("This script requires Windows platform.")
        sys.exit(1)

    if ctypes.windll.shell32.IsUserAnAdmin():
        print("Already running with administrative privileges.")
        return

    script_path = sys.argv[0]
    params = ' '.join([script_path] + sys.argv[1:])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

    sys.exit(0)

# Restart the script with admin privileges
restart_with_admin()

# Specify the directory where the drive list should be saved
directory = r"D:\workplace\forensics\lists"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Step 1: Identify the drives
drive_list = identify_drives()

# Create a file with drive details for each drive
for drive in drive_list:
    drive_path = os.path.join(directory, "drive_list_{}.txt".format(drive.replace(":", "")))
    try:
        with open(drive_path, "w") as file:
            file.write(drive + "\n")
        print("Drive list created for: {}".format(drive))
    except Exception as e:
        print("An error occurred while creating the drive list for {}: {}".format(drive, str(e)))

# Process each drive and store directories in separate files
for drive in drive_list:
    target_drive = drive.strip()
    print("\nProcessing drive: {}".format(target_drive))
    document_drive_specifications(target_drive)
    setup_write_blocker(target_drive)

    # Step 2: Retrieve the partition list
    partitions = psutil.disk_partitions(all=True)
    print("\nPartition List:")
    for partition in partitions:
        print("Device: {}".format(partition.device))
        print("Mountpoint: {}".format(partition.mountpoint))
        print("File System: {}".format(partition.fstype))
        print()

    # Create the directory for storing directories and files if it doesn't exist
    target_directory = os.path.join(directory, target_drive.replace(":", ""))
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Step 3: Create a file with the list of all directories and files
    all_files_file = os.path.join(target_directory, "all_files.txt")
    print("Listing directories and files for drive: {}".format(target_drive))

    try:
        list_directory_files(target_drive, all_files_file)
        print("All directories and files are listed in: {}".format(all_files_file))
    except Exception as e:
        print("An error occurred while listing directories and files: {}".format(str(e)))

input("Press Enter to exit...")
