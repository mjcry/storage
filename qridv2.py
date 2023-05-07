#!/usr/bin/python3

import sqlite3
import qrcode
import json
from PIL import Image

# Get personal details from user input
personal_details = {
    "name": input("Enter your name: "),
    "surname": input("Enter your surname: "),
    "id_number": input("Enter your ID number: "),
    "class_number": input("Enter your class number: "),
    "sex": input("Enter your sex: "),
    "parents_number": input("Enter your parents' number: ")
}

# Encode personal details as JSON string
json_data = json.dumps(personal_details)

# Generate the QR code data
code = qrcode.QRCode(version=1, box_size=10, border=5)
code.add_data(json_data)
code.make(fit=True)

# Create an image from the QR code data
img = code.make_image(fill_color="black", back_color="white")

# Save the image with a unique name based on the student ID
id_number = input("Enter your 13-digit student ID number: ")
img.save(f"{id_number}.jpeg")

# Connect to database and insert personal details
conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS students (id_number TEXT, personal_details TEXT)")
c.execute("INSERT INTO students (id_number, personal_details) VALUES (?, ?)", (id_number, json_data))
conn.commit()
conn.close()

