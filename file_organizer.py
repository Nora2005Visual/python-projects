import os

Folder = input("Enter Folder path: ")

for file in os.listdir(Folder):
    if os.path.isfile(os.path.join(Folder, file)):
        ext = file.split('.')[-1]
        new_folder = os.path.join(Folder, ext)
        if not os.path.exists(new_Folder):
            os.makedirs(new_Folder)
        os.rename(os.path.join(Folder, file), os.path.join(new_folder, file))

print("Files organized by type!")
