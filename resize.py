from PIL import Image
import glob, os

size = 1440, 1440
folder = (r"C:\[enter_your_images_folder_path]\*.*")
count = 0
quality = 70

for infile in glob.glob(folder):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(str(count) + ".jpg", "JPEG", quality=quality)
    count = count + 1
    print(str(count))
