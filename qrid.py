#!/usr/bin/python3

import qrcode

def generate_qr_code(student_id):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(student_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Prompt the user to enter their student ID
while True:
    student_id = input("Enter your student ID (13 numbers only): ")
    if len(student_id) == 13 and student_id.isdigit():
        break
    else:
        print("Invalid input. Please enter 13 numbers only.")

# Generate the QR code for the student ID and save it as a JPEG file
img = generate_qr_code(student_id)
img.save(f"{student_id}.jpg")

