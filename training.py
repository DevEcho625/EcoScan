import os
import shutil
import random

# Set your paths here
original_data_path = 'images\images'  # Folder with subfolders for each class
output_path = 'Dataset'  # Where train, test, val folders will be created

# Define the folder names
train_folder = os.path.join(output_path, 'train')
test_folder = os.path.join(output_path, 'test')
val_folder = os.path.join(output_path, 'val')

# Create train, test, val directories if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# Function to move images from default and real_world into class folders
def consolidate_images(original_path):
    for class_folder in os.listdir(original_path):
        class_path = os.path.join(original_path, class_folder)

        # Only proceed if it's a directory
        if not os.path.isdir(class_path):
            continue

        # Paths to the 'default' and 'real_world' subfolders
        default_path = os.path.join(class_path, 'default')
        real_world_path = os.path.join(class_path, 'real_world')

        # Check and move images from 'default' folder
        if os.path.exists(default_path):
            for image in os.listdir(default_path):
                shutil.move(os.path.join(default_path, image), os.path.join(class_path, image))

            # Optionally remove the empty 'default' folder
            os.rmdir(default_path)

        # Check and move images from 'real_world' folder
        if os.path.exists(real_world_path):
            for image in os.listdir(real_world_path):
                shutil.move(os.path.join(real_world_path, image), os.path.join(class_path, image))

            # Optionally remove the empty 'real_world' folder
            os.rmdir(real_world_path)

# Function to split the dataset into train, test, val
def split_data(original_path, train_folder, test_folder, val_folder, split_ratio=(0.7, 0.2, 0.1)):
    for class_folder in os.listdir(original_path):
        class_path = os.path.join(original_path, class_folder)

        # Only consider directories
        if not os.path.isdir(class_path):
            continue

        # Create corresponding class folders in train, test, val
        os.makedirs(os.path.join(train_folder, class_folder), exist_ok=True)
        os.makedirs(os.path.join(test_folder, class_folder), exist_ok=True)
        os.makedirs(os.path.join(val_folder, class_folder), exist_ok=True)

        # Get list of all images in class folder
        images = os.listdir(class_path)
        random.shuffle(images)  # Shuffle images for randomness

        # Calculate number of images for train, test, val
        train_size = int(split_ratio[0] * len(images))
        test_size = int(split_ratio[1] * len(images))
        val_size = len(images) - train_size - test_size

        # Split images
        train_images = images[:train_size]
        test_images = images[train_size:train_size + test_size]
        val_images = images[train_size + test_size:]

        # Move images to respective folders
        for image in train_images:
            shutil.move(os.path.join(class_path, image), os.path.join(train_folder, class_folder, image))

        for image in test_images:
            shutil.move(os.path.join(class_path, image), os.path.join(test_folder, class_folder, image))

        for image in val_images:
            shutil.move(os.path.join(class_path, image), os.path.join(val_folder, class_folder, image))

# Step 1: Consolidate images from 'default' and 'real_world' into their respective class folders
consolidate_images(original_data_path)

# Step 2: Split the data into train, test, val
split_data(original_data_path, train_folder, test_folder, val_folder)

print("Images moved and data split complete!")
