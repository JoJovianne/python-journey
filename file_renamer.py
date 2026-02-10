import os

#Target files
folder_path = "test_files"

files = os.listdir(folder_path)

for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
<<<<<<< HEAD
    
=======

>>>>>>> 73b0974ce2127bec3015cc3678f5bb69854cc74b
    #Get file extension (.jpg .png etc)
    extension = os.path.splitext(filename)[1]
    
    #New File Name
    new_name = f"file_{index+1}{extension}"
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    
print("All files renamed successfully!")
