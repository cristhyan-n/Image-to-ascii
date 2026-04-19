

def ascii_convert(pixels, width, heigth, invert=False):
    result = ""
    density = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^ '
    if invert:
        density = density[::-1]
    for y in range(heigth):
        for x in range(width):
            shine = pixels[x, y]
            index = int((shine / 255) * (len(density) - 1))
            result += density[index]
        result += '\n'
    return result