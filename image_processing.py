from PIL import Image

def open_image(img_path):
    return Image.open(img_path)

def resize_image(img, width=120):
    original_width, original_height = img.size
    height = int((original_height / original_width) * width / 1.5)

    return img.resize((width, height))

def convert_grayscale(img):
    return img.convert("L")

def load_pixels(img):
    return img.load()

def should_invert(pixels, width, heigth):
    pixel_sum = 0
    for y in range(heigth):
        for x in range(width):
           pixel_sum += pixels[x, y]
    pixel_div = pixel_sum / (width * heigth)
    return pixel_div > 127