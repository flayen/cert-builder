import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    read_csv('assets/data.csv')