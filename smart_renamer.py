import os

#Ask user input folder name
folder_path = input("Enter folder name: ")

#Ask user input filename
prefix = input("Enter new filename prefix: ")

files = os.listdir(folder_path)

for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    
    #Only process files (skip subfolders)
    if os.path.isfile(old_path):
        extension = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{index+1}{extension}"
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        
print("Remaining completed successfully!")
