#!/usr/bin/python3

import qrcode
import pyzbar.pyzbar as pyzbar
import cv2
import tkinter as tk
from tkinter import filedialog

# Initialize the QR code scanner
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

# Initialize the text editor object
root = tk.Tk()
root.withdraw()

# Prompt the user to select a file to write the extracted data to
file_path = filedialog.asksaveasfilename(defaultextension=".txt")

# Continuously scan for QR codes and extract the data
while True:
    _, frame = cap.read()
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        cv2.putText(frame, qr_data, (50, 50), font, 2, (255, 0, 0), 3)
        cv2.imshow("QR Code Scanner", frame)
        
        # Prompt the user to confirm the extracted data
        confirm = input("Extracted data: {}. Confirm? (y/n) ".format(qr_data))
        if confirm.lower() == "y":
            # Write the extracted data to a plain text file
            with open(file_path, "w") as f:
                f.write(qr_data)
            print("Data saved to file: {}".format(file_path))
            cap.release()
            cv2.destroyAllWindows()
            root.quit()
            break
        else:
            continue

