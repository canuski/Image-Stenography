# Image Steganography Application

This application allows users to encode and decode secret messages within images using steganography techniques. Steganography is the practice of concealing messages or information within other non-secret text or data.

## Features:

Encode Message: Users can encode a secret message into an image by selecting an image file and entering the message to be encoded. The application embeds the message into the least significant bits of the image pixels.

Decode Message: Users can decode a hidden message from an encoded image. The application extracts the hidden message from the least significant bits of the image pixels.

## Usage:

Encode Message:

Click on the "Encode" button to open the encoding window.
Enter the message to be encoded in the provided text input field.
Click on the "Select Image" button to choose an image file to encode the message into.
Click on the "Encode" button to initiate the encoding process.
Once the message is successfully encoded, a confirmation message will be displayed.

Decode Message:

Click on the "Decode" button to open the decoding window.
Click on the "Select Image" button to choose the encoded image file.
Click on the "Decode" button to initiate the decoding process.
If a hidden message is found in the image, it will be displayed in a message box. Otherwise, a warning message will be displayed indicating no message found.

## Additional Information:

The application utilizes PyQt5 for the graphical user interface.
It includes external CSS styling for enhancing the visual appearance of the interface.
The encoding and decoding functionalities are implemented using the Python Imaging Library (Pillow).
The application is packaged as a standalone executable using PyInstaller for easy distribution and deployment.

## Requirements:

- Python 3.x
- nPyQt5
- Pillow

## Installation:

1. Clone or download the repository to your local machine.
2. Install the required dependencies using pip:
```pip install PyQt5 Pillow```
3. Run the application by executing the main.py script.

## Note:

- For optimal performance and compatibility, it is recommended to use images in common formats such as PNG, JPEG, or BMP.
- Ensure that the message to be encoded is not too large to avoid distortion of the image.
- This application is intended for educational and recreational purposes only. Ensure compliance with applicable laws and regulations when using steganography techniques.
