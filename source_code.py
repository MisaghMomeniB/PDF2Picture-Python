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

# Function to open a file dialog to select a PDF file
def select_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")], 
        title="Select PDF File"
    )
    pdf_path_var.set(file_path)

# Function to open a directory dialog to select the output folder
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(folder_path)

# Function to start the conversion process after verifying paths
def start_conversion():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    
    # Verify if both PDF file and output folder are selected
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file!")
        return
    if not output_folder:
        messagebox.showwarning("Warning", "Please select an output folder!")
        return

    # Perform the PDF to image conversion
    convert_pdf_to_images(pdf_path, output_folder)

# Setup the main GUI window
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("400x300")

# Variables to store file paths
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()