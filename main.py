from image_processing import open_image, resize_image, convert_grayscale, load_pixels, should_invert
from ascii_converter import ascii_convert
from file_manager import select_image, save_file
import os

def main():
    img_select = select_image()
    print(f"Processando: {os.path.basename(img_select)}")
    img_open = open_image(img_select)
    img_resized = resize_image(img_open)
    img_width, img_height = img_resized.size
    img_convert = convert_grayscale(img_resized)
    img_load_pixel = load_pixels(img_convert)
    invert_contrast = should_invert(img_load_pixel, img_width, img_height)
    img_ascii = ascii_convert(img_load_pixel, img_width, img_height, invert_contrast)
    save_file(img_ascii)

main()