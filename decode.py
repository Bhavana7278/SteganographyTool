import cv2
from crypto_utils import decrypt_message

def decode_text(image_path, password):
    img = cv2.imread(image_path)

    binary_data = ""

    for row in img:
        for pixel in row:
            for i in range(3):
                binary_data += format(pixel[i], '08b')[-1]

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    extracted_data = bytearray()

    for byte in all_bytes:
        extracted_data.append(int(byte, 2))

        # Stop when marker found
        if extracted_data[-5:] == b"#####":
            break

    extracted_data = extracted_data[:-5]  # remove marker

    try:
        secret = decrypt_message(bytes(extracted_data), password)
        print("✅ Hidden Message Found:")
        print(secret)

    except:
        print("❌ Wrong password or no hidden message found!")


if __name__ == "__main__":
    decode_text("output_images/encoded.png", "mypassword")
