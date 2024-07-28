#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        bin_rep = format(num, "08b")
        if n_bytes == 0:
            if bin_rep[0] == "0":
                n_bytes = 0
            elif bin_rep[:3] == "110":
                n_bytes = 1
            elif bin_rep[:4] == "1110":
                n_bytes = 2
            elif bin_rep[:5] == "11110":
                n_bytes = 3
            else:
                return False
        else:
            if not (bin_rep[0] == "1" and bin_rep[1] == "0"):
                return False
            n_bytes = n_bytes - 1
    return n_bytes == 0
