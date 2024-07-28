#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    :param data: List[int] - list of integers representing bytes
    :return: bool - True if data is a valid UTF-8 encoding, else False
    """
    
    n_bytes = 0

    # Masks to check the most significant bits (MSB)
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Check if the number is within the byte range
        if num > 255:
            return False

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # If no leading 1's, it's a single-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            # Check that the byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    # All characters should be complete (n_bytes should be 0)
    return n_bytes == 0
