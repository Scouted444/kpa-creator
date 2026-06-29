PNG = b"\x89PNG\r\n\x1a\n"

def extract_pngs(data, folder):

    pos = 0
    count = 0

    while True:

        start = data.find(PNG, pos)

        if start == -1:
            break

        end = data.find(b"IEND", start)

        if end == -1:
            break

        end += 8

        with open(f"{folder}/image_{count}.png", "wb") as f:
            f.write(data[start:end])

        print("Extracted image", count)

        count += 1
        pos = end