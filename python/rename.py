import os

# Set the folder path containing your images
folder_path = 'C:\\Users\\sarah\\OneDrive\\Desktop\\python'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image based on its extension
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')):
        # You can customize the new filename as per your requirements.
        # In this example, we're simply adding a prefix 'image_' to each file.
        new_filename = f'image_{filename}'
        
        # Create the full path to the new filename
        new_filepath = os.path.join(folder_path, new_filename)
        
        #
import os

# Set the folder path containing your images
folder_path = 'your_folder_path_here'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(foldeC:\Users\\sarah\\OneDrive\\Desktop\\pythonr_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'))]

# Sort the image files to ensure they are processed in order
image_files.sort()

# Initialize a counter for renaming
counter = 1

# Iterate through the image files and rename them sequentially
for old_filename in image_files:
    # Determine the file extension
    file_extension = os.path.splitext(old_filename)[-1]
    
    # Create the new filename with a prefix and the counter
    new_filename = f'image_{counter}{file_extension}'
    
   

