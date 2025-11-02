"""
This script encodes the input string and saves the encoded image as 'output.png'.
Just run the script to encode the string.
"""

"""
    In the assignment description, image width and height are intermixed.
    width --> columns
    height --> rows
    But in specifying the bar height, it uses the word row, which is incorrect.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Encoder:
    def __init__(self):
        self.columns = 800
        self.rows = 400
        self.pixel_space_between_bars = 9
        self.bar_column = self.get_1d_array_for_individual_bar()
        self.space_column = self.get_1d_array_for_whitespace()

    def get_letter_position(self, letter:str) -> int:
        """
        This function accepts a letter as input and gives its position in the alphabet.
        The position is determined irrespective of the case.
        If the input is not a valid English letter, it prints the appropriate message.
        Inputs:
            alphabet: str -> The English alphabet.
        Outputs:
            letter_position: int -> The position of the input letter in the alphabet.
        """

        # Check if the input letter is indeed an English letter
        if not ((97<=ord(letter)<=122) or (65<=ord(letter)<=90)):
            print(f"The letter `{letter}` is not a valid English letter. Please check your input.")
            return -1
        return (ord(letter.lower()) - ord('a') + 1)
    
    def get_1d_array_for_individual_bar(self):
        """
        This function creates 1D arrays for individual bars.
        """
        bar_h1 = 10
        bar_h2 = 325
        bar_column = np.full(shape=(self.rows), fill_value=255, dtype=np.uint8)
        bar_column[bar_h1:bar_h2] = 0
        return bar_column
    def get_1d_array_for_whitespace(self):
        """
        This function creates 1D arrays for whitespace character.
        """
        space_h1 = 150
        space_h2 = 250
        space_column = np.full(shape=(self.rows), fill_value=255, dtype=np.uint8)
        space_column[space_h1:space_h2] = 0
        return space_column

    def encode_string(self):
        """
        This function encodes the input string.
        """
        
        # Create the empty canvas
        canvas = np.full((self.rows,self.columns),255, dtype=np.uint8)
        
        column_current_position = 0
        for letter in self.input_string:
            if letter == " ": # If it is a space
                canvas[:,column_current_position] = self.space_column
                # Update the column_current_position
                column_current_position = column_current_position + self.pixel_space_between_bars
                print("Encoded the space")
                continue
            else:
                letter_position = self.get_letter_position(letter)
                if letter_position == -1:
                    print(f"You have entered an invalid letter in the input '{self.input_string}'. Please try again with a valid input.")
                    return None
            canvas[:,column_current_position:column_current_position+letter_position+1] = np.tile(self.bar_column[:, np.newaxis], (1, letter_position+1))
            # Update the column_current_position
            column_current_position = column_current_position + self.pixel_space_between_bars + letter_position + 2
            print(f"Encoded the letter '{letter}'")
        return canvas
    
    def print_and_save_encoded_image(self):
        """
        This function prints and saves the encoded image.
        """
        canvas = self.encode_string()
        if canvas is None:
            return None
        
        plt.imshow(canvas,cmap='gray', vmin=0, vmax=255, origin='upper')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        # Save the image
        Image.fromarray(canvas).save("output.png")
        print("The string has been encoded and the resultant image has been saved as 'output.png'")
    
    def encode(self, input_string:str):
        self.input_string = input_string
        self.print_and_save_encoded_image()



if __name__ == "__main__":
    encoder = Encoder()
    encoder.encode("Abbas Cheddad")
