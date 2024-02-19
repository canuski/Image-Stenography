from PIL import Image

# Function to decode a message from an image

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Extract the length of the message from the first 32 bits
    message_length_bin = ''
    for i in range(32):
        red, green, blue = pixels[i]
        message_length_bin += str(red & 1)
        message_length_bin += str(green & 1)
        message_length_bin += str(blue & 1)

    # Split the binary message length into 32-bit chunks
    message_length_chunks = [message_length_bin[i:i+32]
                             for i in range(0, len(message_length_bin), 32)]

    # Convert each chunk to an integer
    message_length = int(''.join(message_length_chunks), 2)


    binary_message = ''
    byte_chunks = []

    index = 32  # Skip the first 32 bits (message length)
    for _ in range(message_length):
        # Extract LSB from each color channel
        red, green, blue = pixels[index]
        binary_message += str(red & 1)
        binary_message += str(green & 1)
        binary_message += str(blue & 1)

        # Check if we have accumulated 8 bits (1 byte)
        if len(binary_message) >= 8:
            byte_chunks.append(binary_message[:8])
            binary_message = binary_message[8:]

            # Convert binary message to string
            message = ''.join(chr(int(chunk, 2)) for chunk in byte_chunks)

            # Check if the null terminator is found in the message
            if message.endswith('\x00'):
                return message.rstrip('\x00')

        index += 1

    return "End of message not found"  # If null terminator is not found

if __name__ == "__main__":
    # Decode message from the encoded image
    decoded_message = decode_image("encoded_image.png")
    print("Decoded message:", decoded_message)
