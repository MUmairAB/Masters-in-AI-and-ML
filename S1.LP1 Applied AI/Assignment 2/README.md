# Assignment 2: Barcode Encoding and Decoding System

This assignment implements a simplified barcode encoding and decoding system using computer vision techniques. The system converts text strings into visual barcode representations and reconstructs the original text from barcode images.

## Background

Barcodes are widely used in product packaging to enable quick data retrieval (e.g., price, URL, expiration date, product origin) through scanning systems. This assignment simulates a simplified barcode reader that encodes and decodes text strings using a custom encoding scheme.

<figure>
  <img src="./output.png" alt="Barcode Example" />
  <figcaption><b>Figure 1:</b> Example barcode encoding the string "Abbas Cheddad". The barcode consists of vertical bars of varying widths representing different characters, with spaces between bars.</figcaption>
</figure>

## Part 1: Encoder

The encoder converts an input string into a barcode image using a custom encoding scheme based on character positions in the alphabet.

### Implementation Steps

**Step 1: Canvas Creation**
- Create an empty canvas of size **400 × 800 pixels** (rows × columns)
- Canvas initialized with white pixels (value 255)

**Step 2: Encoding Specifications**

- **Step Size**: 9 pixels (spacing between bars)
- **Bar Height**: 
  - Full bars: From row 10 to row 350 (340 pixels tall)
  - Space bars: From row 150 to row 250 (100 pixels tall, shorter for visual distinction)
- **Bar Width**:
  - Empty space: Fixed width of 1 pixel
  - Alphabetic characters: Width = alphabet position + 1
    - Example: 'A' or 'a' → width = 2 pixels (position 1 + 1)
    - Example: 'S' or 's' → width = 20 pixels (position 19 + 1)
    - Characters are case-insensitive

**Step 3: Encoding Process**
- Loop through each character in the input string
- For each character:
  - If space: Draw a shorter bar (1 pixel wide, rows 150-250)
  - If letter: Draw a full bar with width = (alphabet position + 1) pixels
- Add 9-pixel spacing between each bar

**Step 4: Output**
- Save the encoded image as `output.png` (PNG format, not JPG/JPEG)

### Implementation Details

The encoder is implemented in [encoder.py](./encoder.py) with the following key components:

- **`Encoder` class**: Main encoder class handling the encoding process
- **`get_letter_position()`**: Converts a character to its alphabet position (case-insensitive)
- **`get_1d_array_for_individual_bar()`**: Creates the full-height bar template
- **`get_1d_array_for_whitespace()`**: Creates the shorter space bar template
- **`encode_string()`**: Processes the input string and generates the barcode canvas
- **`encode()`**: Main function that accepts input string and saves the output image

**Usage**:
```python
encoder = Encoder()
encoder.encode('Abbas Cheddad')  # Writes "output.png" to disk
```

<figure>
  <img src="./output.png" alt="Encoded Barcode" />
  <figcaption><b>Figure 2:</b> Encoded barcode image (400×800 pixels) representing the string "Abbas Cheddad". Each character is represented by a vertical bar whose width corresponds to its position in the alphabet.</figcaption>
</figure>

## Part 2: Decoder

The decoder reconstructs the original text string from a barcode image by analyzing bar widths along a horizontal scan line.

### Implementation Steps

**Step 1: Image Reading**
- Read the `output.png` image file
- Convert to grayscale for processing

**Step 2: Decoding Algorithm**

The decoder scans the image horizontally at **row 200** (middle line) and reconstructs the string:

```python
Set string Str = ""
Scan the middle line (row 200) and calculate the width (w) of each bar
IF w == 1:  # Empty space (short bar)
    Append space to Str
ELSE:  # Character
    Match character corresponding to width
    Append character to Str
END IF
```

**Decoding Logic**:
- Scan row 200 pixel by pixel
- Count consecutive black pixels (value 0) to determine bar width
- If width = 1 pixel → space character
- If width = w pixels → character at position (w - 1) in alphabet
  - Example: width = 2 → 'A' (position 1)
  - Example: width = 20 → 'S' (position 19)

### Implementation Details

The decoder is implemented in [decoder.py](./decoder.py) with the following key components:

- **`Decoder` class**: Main decoder class handling the decoding process
- **`decode()`**: Scans row 200, calculates bar widths, and reconstructs the original string

**Usage**:
```python
decoder = Decoder()
decoded_string = decoder.decode()  # Returns the decoded string
```

### Decoding Example

<figure>
  <img src="./Abbas Own Barcode-3.png" alt="Barcode Breakdown" />
  <figcaption><b>Figure 3:</b> Detailed breakdown of the barcode structure. The image shows how each character in "Abbas Cheddad" is represented by bars of different widths based on their alphabet positions. The space between words is represented by a shorter bar.</figcaption>
</figure>

## Key Features

- **Case-Insensitive Encoding**: Characters 'A' and 'a' are encoded identically
- **Visual Distinction**: Spaces use shorter bars (rows 150-250) vs. full bars (rows 10-350)
- **Robust Decoding**: Uses middle scan line (row 200) to avoid edge detection issues
- **PNG Format**: Ensures lossless image quality for accurate decoding

## How to Run

1. Clone the repository and navigate to this directory.
2. Ensure you have the required dependencies installed:
   - Python 3.x
   - numpy
   - matplotlib
   - PIL (Pillow)
3. **Encode a string**:
   ```bash
   python encoder.py
   ```
   This will encode "Abbas Cheddad" and save it as `output.png`

4. **Decode the barcode**:
   ```bash
   python decoder.py
   ```
   This will read `output.png` and print the decoded string

## Output

**Encoder Output**:
- Generates `output.png` image file (400×800 pixels)
- Displays the barcode visualization
- Prints encoding progress for each character

**Decoder Output**:
- Prints the decoded string to console
- Example: `The decoded string is: 'abbas cheddad'`

## Technical Specifications

| Parameter | Value |
|-----------|-------|
| Canvas Size | 400 × 800 pixels (rows × columns) |
| Bar Spacing | 9 pixels |
| Full Bar Height | Rows 10-350 (340 pixels) |
| Space Bar Height | Rows 150-250 (100 pixels) |
| Space Width | 1 pixel |
| Character Width Range | 2-26 pixels (A-Z) |
| Decoding Scan Line | Row 200 (middle) |
