import os
import glob
import subprocess


os.chdir('/home/vlad/Desktop/Sucessful_Osprey_February/result')

# Function to find all files matching the pattern "bbkstar*.py"
def find_bbkstar_files(directory):
    bbkstar_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("bbkstar") and file.endswith(".py"):
                bbkstar_files.append(os.path.join(root, file))
    return bbkstar_files

# Get the current directory
current_directory = os.getcwd()

# Find all "bbkstar*.py" files in the current directory and its subdirectories
bbkstar_files_list = find_bbkstar_files(current_directory)

# Loop through each path, run the Python scripts, and create a txt file with the filename
for path in bbkstar_files_list:
    folder_name = os.path.dirname(path)
    file_name = os.path.splitext(os.path.basename(path))[0]
    
    os.chdir(folder_name)
        
    # Run the Python script using subprocess
    command = f"python3.9 {path}"
    subprocess.run(command, shell=True)
    
#     # Create a txt file with the filename inside the same folder as the Python script
#     with open(os.path.join(folder_name, f"{file_name}.txt"), "w") as f:
#         f.write(file_name)
