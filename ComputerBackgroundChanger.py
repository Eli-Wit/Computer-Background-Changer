import os
import random
import time
import ctypes
from PIL import Image

# You can paste the file path of your image folder inside these quotations.
# Otherwise you will prompted to provide one.
selected_folder = r"" 

recent_images = []
change_interval = 60  # Time in seconds between changes
max_recent = 20  # Max number of recent images to store

def get_image_path(selected_folder):
    # Get a list of all image files in the folder
    try:
        images = [f for f in os.listdir(selected_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    except:
        print('\nError: Could not find file path "' + selected_folder + '".')
        time.sleep(1)
        return 'error'
    
    # Filter out recently used images
    available_images = [img for img in images if os.path.join(selected_folder, img) not in recent_images]

    if available_images:
        random_image = random.choice(available_images)
    else:
        # If all images were recently used, allow selecting from full list
        random_image = random.choice(images)
        print("All images have been used recently. Resetting history.")

    return os.path.join(selected_folder, random_image)

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    print(f"Wallpaper changed to: {image_path}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    
    while selected_folder == '' or get_image_path(selected_folder) == 'error':        
        selected_folder = input(str('\nPlease enter a folder path for the images you would like to use:\n\n--> '))
            
    image = get_image_path(selected_folder)
    
    if image == 'error':
        break

    # Ensure recent_images list does not exceed max size
    if len(recent_images) >= max_recent:
        recent_images.pop(0)  # Remove the oldest entry

    recent_images.append(image)  # Store the new image
    
    change_wallpaper(image)
    
    time.sleep(change_interval)
