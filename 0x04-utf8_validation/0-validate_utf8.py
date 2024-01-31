#!/usr/bin/python3
"""
UTF-8 Validation task for interview preparation
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    The validation must take care of all edge cases
    """
    bytes_num = 0
    for byte in data:
        mask = 1 << 7
        if not bytes_num:
            while byte & mask:
                bytes_num += 1
                mask >>= 1
            if not bytes_num:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        bytes_num -= 1
    return bytes_num == 0
