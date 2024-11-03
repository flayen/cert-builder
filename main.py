import csv
from PIL import Image, ImageDraw, ImageFont

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)


def add_text_to_image(image_path, text, font_path, font_size, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)
    image_width, image_height = image.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    draw.text((x, y), text, font=font, fill="black")

    image.save(output_path)

if __name__ == "__main__":
    read_csv('assets/data.csv')