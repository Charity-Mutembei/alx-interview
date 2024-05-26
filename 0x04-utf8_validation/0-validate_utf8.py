#!/usr/bin/python3
'''
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding,
else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer
'''


def validUTF8(data):
    '''
    Number of bytes in the current UTF-8 character
    '''
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer in the data list
    for byte in data:
        # Extract the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (ASCII)
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                return False
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2 | (1 << 5)):
                # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (mask1 | mask2 | (1 << 5) | (1 << 4)):
                # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & mask1) or (byte & mask2):
                return False
            num_bytes -= 1

    # If there are leftover bytes expected, the sequence is incomplete
    return num_bytes == 0
