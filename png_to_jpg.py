import os
import sys
import glob
import argparse
from PIL import Image


def get_png_image_list(source):
    extensions = ['png', 'PNG']
    image_list = []
    for extension in extensions:
        image_list += glob.glob1(source, '*.' + extension)
    return image_list


def store_jpg_images(source, destination, image_list):
    if not source.endswith('/'):
        source += '/'
    if not destination.endswith('/'):
        destination += '/'

    for image in image_list:
        im = Image.open(source + image)
        im.save(destination + image[0:-3] + 'jpg')


def run(args):
    if not os.path.isdir(args.source):
        print('The source folder ' + args.source + ' does not exist!')
        sys.exit()
    if not os.path.isdir(args.source):
        print('The destination folder ' + args.destination + ' does not exist!')
        sys.exit()
    image_list = get_png_image_list(args.source)
    store_jpg_images(args.source, args.destination, image_list)


def main_func():
    parser = argparse.ArgumentParser(description='Convert PNG to JPG images.', )
    parser.add_argument(
            '-s',
            '--source',
            action='store',
            dest='source',
            help='The source folder of the images.',
            required=True
    )

    parser.add_argument(
            '-d',
            '--destination',
            action='store',
            dest='destination',
            help='The destination folder of the images.',
            required=True
    )

    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main_func()
