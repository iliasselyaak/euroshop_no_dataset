import os
import random
import glob

# Set the directory paths
image_dir = 'euroshop/euroshop_dataset/images'
label_dir = 'euroshop/euroshop_dataset/labels'
output_dir = 'euroshop/euroshop_dataset'

# Get all image file paths
image_paths = glob.glob(os.path.join(image_dir, '*.jpg'))

# Shuffle the dataset
random.shuffle(image_paths)

# Split the dataset
total_images = len(image_paths)
train_split = int(0.7 * total_images)
val_split = int(0.2 * total_images)

train_images = image_paths[:train_split]
val_images = image_paths[train_split:train_split + val_split]
test_images = image_paths[train_split + val_split:]

# Function to save the file paths to a text file with the required format
def save_file_paths(file_paths, filename):
    with open(filename, 'w') as f:
        for path in file_paths:
            relative_path = './images/' + os.path.basename(path)
            f.write(relative_path + '\n')

# Save the file paths to train.txt, val.txt, and test.txt
save_file_paths(train_images, os.path.join(output_dir, 'train.txt'))
save_file_paths(val_images, os.path.join(output_dir, 'val.txt'))
save_file_paths(test_images, os.path.join(output_dir, 'test.txt'))

print(f"Total images: {total_images}")
print(f"Training images: {len(train_images)}")
print(f"Validation images: {len(val_images)}")
print(f"Testing images: {len(test_images)}")
