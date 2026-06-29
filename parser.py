import re

def find_strings(data):

    strings = re.findall(rb"[ -~]{6,}", data)

    out = []

    for s in strings:
        try:
            out.append(s.decode())
        except:
            pass

    return out