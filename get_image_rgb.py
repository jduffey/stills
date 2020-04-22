from PIL import Image
import numpy as np
import scipy.cluster
import binascii


#IMAGE_DIRECTORY = 'images'
NUM_CLUSTERS = 5


def get_dominant_RGB_values(image):
    im = Image.open(image)
    im = im.resize((150, 150))  # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, _ = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, _ = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _ = np.histogram(vecs, len(codes))       # count occurrences

    index_max = np.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    hex_color = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')

    h = hex_color
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)

    return r, g, b


def is_red(image):
    r, g, b = get_dominant_RGB_values(image)

    return r > 160 and g < 100 and b < 140


def is_green(image):
    r, g, b = get_dominant_RGB_values(image)

    return r < 100 and g > 160 and b > 80


def is_blue(image):
    r, g, b = get_dominant_RGB_values(image)

    return r < 100 and g < 100 and b > 200


def is_white(image):
    r, g, b = get_dominant_RGB_values(image)

    return r > 180 and g > 180 and b > 180