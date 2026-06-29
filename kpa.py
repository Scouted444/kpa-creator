import os
from parser import find_strings
from extractor import extract_pngs

class KPAFile:

    def __init__(self, filename):
        self.filename = filename

        with open(filename, "rb") as f:
            self.data = f.read()

    def info(self):

        print("==========")
        print("KPA INFO")
        print("==========")

        print("File:", self.filename)
        print("Size:", len(self.data), "bytes")
        print("Magic:", self.data[:6])

        print("\nStrings:")

        for s in find_strings(self.data):
            print(" ", s)

    def extract_pngs(self, folder):
        os.makedirs(folder, exist_ok=True)
        extract_pngs(self.data, folder)