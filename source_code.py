import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os

# Function to convert each page of a PDF to an image and save in the specified folder
def convert_pdf_to_images(pdf_path, output_folder):
    try:
        # Convert each page of the PDF to an image
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            output_path = os.path.join(output_folder, f"page_{i + 1}.png")
            image.save(output_path, 'PNG')
        messagebox.showinfo("Success", "PDF successfully converted to images!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")