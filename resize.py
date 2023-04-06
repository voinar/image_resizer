from PIL import Image
import glob, os

size = 1440, 1440
folder = (r"C:\Users\zzx\Desktop\photos\*.*")
count = 0
quality = 70

for infile in glob.glob(folder):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(str(count) + ".jpg", "JPEG", quality=quality)
    count = count + 1
    print(str(count))

#import os
#path = (r"C:/Users/zzx/Desktop/urodziny_jacka_33/")
#files = os.listdir(path)

#for index, file in enumerate(files):
#    os.rename(os.path.join(path, file), os.path.join(path, '_urodziny_33 _jacka_2020_06'.join([str(index), '.jpg'])))