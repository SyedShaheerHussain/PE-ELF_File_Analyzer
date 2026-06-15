import math
from collections import Counter


def entropy(data: bytes):
    if not data:
        return 0.0

    counter = Counter(data)
    length = len(data)

    result = 0.0
    for count in counter.values():
        p = count / length
        result -= p * math.log2(p)

    return result


def entropy_label(value):
    if value > 7:
        return "HIGH (packed/suspicious)"
    elif value > 5:
        return "MEDIUM"
    else:
        return "LOW"