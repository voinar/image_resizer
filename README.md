#image_resizer 📷📏🤏

## 🤔 Purpose:
A script for batch image processing with Python and Pillow. Use cases:
- compression 
- resizing

## 🧐 How to use it:
1. Place all your original size JPEG images in folder.
2. Update the path in resize.py by editing "folder" variable.
3. Save and run the script from the command line with Python.
4. Output images will be placed in the original folder. By default images will be named as increments of 1 starting from 0 (eg.: 0.jpg, 1.jpg, 2.jpg, 3.jpg etc).

## 🔮 Optional settings:
- "size" variable: Set image dimensions. Defaults to 1440x1440px. Original image proportions are conserved, so the resizing will default to 1440px at the longer edge of the resized image.
- "count" variable: Output files are named after auto-increment number values. By default starting from 0. Can be changed to any other number.
- "quality" variable: Set the compression level on the output JPG's. Defaults to 70. Any number between 1 and 100.
