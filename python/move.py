import os
import shutil
import glob

# Set the source folder path
source_folder = 'C:\\Users\\sarah\\OneDrive\\Desktop\\python'

# Define the destination folders
destination_folders = ['folder1', 'folder2', 'folder3', 'folder4', 'folder5']

# Create the destination folders if they don't exist
for folder in destination_folders:
    os.makedirs(folder, exist_ok=True)

# Get a list of image files in the source folder
image_files = glob.glob(os.path.join(source_folder, '*.*'))

# Calculate how many images each folder should receive
images_per_folder = len(image_files) // len(destination_folders)

# Move images sequentially to the destination folders
for i, folder in enumerate(destination_folders):
    start_idx = i * images_per_folder
    end_idx = start_idx + images_per_folder

    # Move images from start_idx to end_idx to the current destination folder
    for image in image_files[start_idx:end_idx]:
        shutil.move(image, os.path.join(folder, os.path.basename(image)))

print("Images have been moved to destination folders.")
