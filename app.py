import os
import time
import glob
from totp import generate_digest
import collections


def synchronize_time():
    command = 'sudo ntpdate -s'
    target = 'time.nist.gov'
    print(f'Syncing time with {target}')
    os.system(command + ' ' + target)


def get_color(digit_to_use_for_color):
    return number_color_dict[int(digit_to_use_for_color, 16) % 4]


def take_photos(num_photos=1):
    take_times = []
    for i in range(num_photos):
        print('Taking photo...')
        start = time.time()
        os.system('./takephoto.sh')
        duration = time.time() - start
        print(duration)
        take_times.append(duration)
        print('Done taking photo.')
    print(f'\nTake times: {take_times}')
    print(f'\nAvg take time: {sum(take_times) / len(take_times)}')


def generate_filename_msgs():
    photo_files = os.listdir('photos/')
    print(f'\nPhoto files:\n{photo_files}')

    filenames = [int(file.split('.')[0]) for file in photo_files]
    filenames.sort()
    print(f'\nFilenames\n{filenames}')

    return filenames


def round_down(num, divisor):
    return num - (num % divisor)


number_color_dict = {
    0: 'RED',
    1: 'GREEN',
    2: 'BLUE',
    3: 'WHITE',
}


secret = 'bbb'

synchronize_time()

take_photos()

filenames = generate_filename_msgs()

expected_colors = {}

avg_time_for_picamera_to_take_pic = 6

for filename in filenames:
    time_msg = round_down(filename + avg_time_for_picamera_to_take_pic, 5)
    expected_colors[f'{filename}.jpg'] = \
    (get_color(generate_digest(time_msg, secret, 1)), time_msg)

print(f'\nExpected colors - {len(expected_colors)} image(s):')
for k, v in expected_colors.items():
    print(f'{k} : {v}')


#os.system('sudo shutdown now')