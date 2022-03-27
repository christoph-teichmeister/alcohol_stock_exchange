import random


def get_random_hex_code():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    return "#" + hex_number[2:]
