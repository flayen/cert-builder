# Flayen's Certificate Builder
This is a simple certificate builder that uses the `Pillow` library to create certificates. It is a simple script that reads a CSV file, certificate image, and font then creates a certificate for each row in the CSV file.
The generated certificates are saved in a paginated pdf via `PyPDF2` inside the `output` folder.

The goal is to support other paper sizes and add more features in the future.

> This script currently supports paper size of 8.5x13 inches

## How to use
> This guide assumes that you have Python installed on your machine
1. Clone the repository
```bash
git clone https://github.com/flayen/cert-builder
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Prepare the certificate image, font and csv file
4. Run the script
```bash
python main.py
```
5. Check the `output` folder for the generated .pdf file