"""
This script decodes the encoded image and prints the decoded string.
Just run the script to decode the image.
"""


import numpy as np
from PIL import Image


class Decoder:
    def __init__(self):
        # Read the encoded image and convert it to grayscale
        self.encoded_image = np.array(Image.open("output.png").convert("L"))
        #self.encoded_image = np.array(Image.open("Abbas Own Barcode-3.png").convert("L"))

    def decode(self):
        encoded_string = ""
        black_pixel_count = 0
        for pixel_number in range(self.encoded_image.shape[1]):
            pixel_value = self.encoded_image[200, pixel_number]
            if pixel_value == 0:
                black_pixel_count += 1
            # Check if the next pixel is different from the current pixel
            if pixel_number < self.encoded_image.shape[1]-1:
                if (pixel_value == 0) and (self.encoded_image[200, pixel_number+1] != pixel_value):
                    # Check if it is a space
                    if np.count_nonzero(self.encoded_image[:, pixel_number] == 255) == 300:
                        #print("Space")
                        encoded_string += " "
                        black_pixel_count = 0
                        continue
                    encoded_string += chr(black_pixel_count-2 + ord('a'))
                    black_pixel_count = 0
        print(f"The decoded string is: '{encoded_string}'")
        return encoded_string

if __name__ == "__main__":
    decoder = Decoder()
    decoder.decode()