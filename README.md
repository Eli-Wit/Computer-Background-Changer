#Computer Background Changer

A lightweight Python utility that automatically updates your Windows desktop wallpaper by selecting random images from a folder. The script avoids recently used images, supports several common formats, and runs continuously at a configurable interval.

Features

Automatically changes your wallpaper on a timed cycle

Randomly selects images from a folder of your choice

Avoids repeating wallpapers by tracking recently used images

Resets history automatically when all images have been used

Supports PNG, JPG, JPEG, and BMP files

Runs until you manually stop it

Simple setup and minimal configuration

Requirements

Windows operating system

Python 3.8 or later

The Pillow library (PIL) must be installed

Setup

Download the script.

Choose a folder containing your images.

Either set that folder path inside the script or leave the value blank to be prompted at runtime.

Adjust the wallpaper change interval if desired.

(Optional) Modify how many recent images the script should remember before allowing repeats.

How It Works

The script scans the specified folder and collects all supported image files.

It filters out images that were used recently.

It selects one random image from the remaining pool.

If every image was used recently, the history resets and all images become eligible again.

The Windows wallpaper is updated using a system API call.

The script waits for the specified interval, then repeats the process.

Usage

Run the script from a terminal.
If the folder path was left blank, the script will prompt you for one.
The wallpaper will begin cycling automatically and will continue until you close the terminal or interrupt execution.

Customization

You can customize:

The folder where your images are stored

How often the wallpaper changes

How many recent images should be avoided before repeats are allowed

These values are set near the top of the script for easy adjustment.

Notes

This tool works only on Windows.

Ensure your image folder contains at least one supported file type.

Closing the terminal stops the wallpaper rotation.

License

You may modify or use this project freely. If desired, add your own license to the repository.
