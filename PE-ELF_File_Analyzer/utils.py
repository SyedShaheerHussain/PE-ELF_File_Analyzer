import string

def extract_strings(data, min_len=4):
    result = []
    current = ""

    for b in data:
        c = chr(b) if b < 128 else " "

        if c in string.printable:
            current += c
        else:
            if len(current) >= min_len:
                result.append(current)
            current = ""

    if len(current) >= min_len:
        result.append(current)

    return "\n".join(result)


def to_hex(data):
    lines = []
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_bytes = " ".join(f"{b:02X}" for b in chunk)
        lines.append(f"{i:08X}  {hex_bytes}")
    return "\n".join(lines)


def file_stats(text):
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines())
    }