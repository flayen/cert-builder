import csv
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def add_text_to_image(image_path, text, font_path, font_size, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    image_width, image_height = image.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    draw.text((x, y), text, font=font, fill="black")

    image.save(output_path, format='PNG')
    return output_path

def save_images_to_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    for image_path in image_paths:
        image = Image.open(image_path)
        image_width, image_height = image.size
        c.setPageSize((image_width, image_height))
        c.drawImage(image_path, 0, 0, width=image_width, height=image_height)
        c.showPage()
    c.save()

def generate_certificates(csv_path, image_template_path, font_path, font_size, output_pdf_path):
    image_paths = []
    os.makedirs('generated', exist_ok=True)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            output_image_path = os.path.join('generated', f'output_{name.replace(" ", "_")}.png')
            add_text_to_image(image_template_path, name, font_path, font_size, output_image_path)
            image_paths.append(output_image_path)

    save_images_to_pdf(image_paths, output_pdf_path)

if __name__ == "__main__":
    generate_certificates('assets/data.csv', 'assets/certificate.png', 'assets/font/Roboto-Regular.ttf', 50, 'generated/output_certificates.pdf')