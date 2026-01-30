import cv2
from crypto_utils import encrypt_message

def encode_text(image_path, secret_text, password, output_path):
    img = cv2.imread(image_path)

    encrypted = encrypt_message(secret_text, password)

    # Convert encrypted message into binary
    data = encrypted + b"#####"
    binary_data = ''.join(format(byte, '08b') for byte in data)

    data_index = 0

    for row in img:
        for pixel in row:
            for i in range(3):
                if data_index < len(binary_data):
                    pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_data[data_index], 2)
                    data_index += 1

    cv2.imwrite(output_path, img)
    print("✅ Message hidden successfully in:", output_path)


if __name__ == "__main__":
    encode_text(
        "input_images/sample.png",
        "Hello Bhavana! Secret message here.",
        "mypassword",
        "output_images/encoded.png"
    )

