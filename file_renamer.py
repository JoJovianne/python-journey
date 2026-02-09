import os

#Target files
folder_path = "test_files"

files = os.listdir(folder_path)

for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    
    extension = os.path.splitext(filename)[1]
    
    #New File Name
    new_name = f"file_{index+1}{extension}"
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    
print("All files renamed successfully!")