import os
from PIL import Image
from PIL import ImageFilter


source_dir = 'photos/'
all_files = os.listdir(source_dir)
all_files.sort()

dest_dir = 'cropped_photos/'

left = 1290
top = 625
right = 2100
bottom = 1400
area = (left, top, right, bottom)

total_images = len(all_files)
counter = 0

all_files = all_files[0:4]

print(f'Begin cropping {total_images} images...')
for file in all_files:
    print(f'\nCropping {file}')
    img = Image.open(source_dir + file)
    for _ in range(10):
        img = img.filter(ImageFilter.BLUR)
    cropped_img = img.crop(area)
    cropped_img.save(dest_dir + file.split('.')[0] + '_crop.png', 'PNG')
    counter += 1
    print(f'Cropped {counter} / {total_images}')




#my_name = '1587314824.jpg'
#img = Image.open('photos/' + my_name)
#cropped_img = img.crop(area)
#cropped_img.save('cropped_photos/' + my_name.split('.')[0] + '_crop.png', 'PNG')