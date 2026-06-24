import os

folder_path = input("enter folder path: ")

# Check whether the folder exists
if os.path.exists(folder_path):

    # Get all files from the folder
    files = os.listdir(folder_path)

    count = 1

    # Rename each file one by one
    for file in files:

        old_path = os.path.join(folder_path, file)

        if os.path.isfile(old_path):

            file_extension = os.path.splitext(file)[1]

            new_name = f"file_{count}{file_extension}"

            new_path = os.path.join(folder_path, new_name)

            # Rename file
            os.rename(old_path, new_path)

            print(f"{file} renamed to {new_name}")

            count += 1
        
    print("All files renamed successfully.")

else:
    print("Folder does not exist.")