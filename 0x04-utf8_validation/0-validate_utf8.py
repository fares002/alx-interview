#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    
    def get_binary_representation(num):
        """Returns the 8-bit binary representation of a number."""
        return format(num, '08b')

    n_bytes = 0

    for num in data:
        bin_rep = get_binary_representation(num)

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if bin_rep[0] == '0':
                # 1-byte character (0xxxxxxx)
                continue
            elif bin_rep[:3] == '110':
                # 2-byte character (110xxxxx)
                n_bytes = 1
            elif bin_rep[:4] == '1110':
                # 3-byte character (1110xxxx)
                n_bytes = 2
            elif bin_rep[:5] == '11110':
                # 4-byte character (11110xxx)
                n_bytes = 3
            else:
                # Invalid first byte pattern for UTF-8
                return False
        else:
            # Check that the byte starts with '10' (10xxxxxx)
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
            n_bytes -= 1

    # All characters should be complete (n_bytes should be 0)
    return n_bytes == 0
