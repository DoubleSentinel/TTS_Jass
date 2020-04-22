from PIL import Image
import os


def crop(input_path, output_path, height, width):
    im = Image.open(input_path)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            cropped = im.crop(box)
            cropped.save(os.path.join(output_path, f"img-{i}-{j}.png"), "PNG")


def hard_coded_crop(input_path, output_path, height, width):
    im = Image.open(input_path)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        # ignoring first 3 cards
        for j in range(510, imgwidth, width):
            box = (j, i, j + width, i + height)
            cropped = im.crop(box)
            cropped.save(os.path.join(output_path, f"img-{i + 1}-{j + 1}.png"), "PNG")


if __name__ == '__main__':
    crop("./assets/aligned_cards.png", "./assets/cut", 265, 171)
    hard_coded_crop("./assets/first_row_cards.png", "./assets/cut", 265, 171)
