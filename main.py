from kpa import KPAFile

filename = input("KPA file: ")

kpa = KPAFile(filename)

kpa.info()
kpa.extract_pngs("output")