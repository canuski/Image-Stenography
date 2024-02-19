from PIL import Image

# Function to encode a message into an image


# Function to encode a message into an image
def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b')
                             for char in message)  # Convert message to binary
    # Append null terminator to the binary message
    binary_message += '00000000'

    index = 0
    encoded_pixels = []
    for pixel in img.getdata():
        if index < len(binary_message):
            red, green, blue = list(pixel)
            red = red & ~1 | int(binary_message[index])
            index += 1
            if index < len(binary_message):
                green = green & ~1 | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                blue = blue & ~1 | int(binary_message[index])
                index += 1
            encoded_pixels.append((red, green, blue))
        else:
            encoded_pixels.append(pixel)

    # Create a new image with the encoded pixels
    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(encoded_pixels)
    encoded_img.save(output_path)
    print("Message encoded successfully")

bug_fix='............'

if __name__ == "__main__":
    # Encode message into an image
    encode_image('image.png', f"{bug_fix}Hello! This is a secret message!",
                 "encoded_image.png")
