import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os

# Function to convert each page of a PDF to an image and save in the specified folder
def convert_pdf_to_images(pdf_path, output_folder, file_type):
    try:
        # Convert each page of the PDF to an image
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
            image.save(output_path, file_type.upper())
        messagebox.showinfo("Success", "PDF successfully converted to images!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a file dialog to select a PDF file
def select_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")], 
        title="Select PDF File"
    )
    if file_path:
        pdf_path_var.set(file_path)

# Function to open a directory dialog to select the output folder
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)

# Function to start the conversion process after verifying paths and file type
def start_conversion():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()  # Get the selected file type and standardize to uppercase
    
    # Verify if both PDF file and output folder are selected
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file!")
        return
    if not output_folder:
        messagebox.showwarning("Warning", "Please select an output folder!")
        return
    if file_type not in ["PNG", "JPEG", "BMP", "TIFF"]:
        messagebox.showwarning("Warning", "Unsupported file type selected!")
        return

    # Perform the PDF to image conversion
    convert_pdf_to_images(pdf_path, output_folder, file_type)

# Function to close the application
def exit_application():
    root.quit()

# Setup the main GUI window
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("400x525")

# Variables to store file paths and image format
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()
file_type_var = tk.StringVar(value="PNG")  # Default to PNG

# PDF file selection label and button
tk.Label(root, text="PDF File:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)

# Output folder selection label and button
tk.Label(root, text="Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)

# Dropdown menu for selecting the file type
tk.Label(root, text="Select Image Format:").pack(pady=5)
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.pack(pady=5)

# Button to start PDF to image conversion
tk.Button(root, text="Convert to Images", command=start_conversion).pack(pady=20)

# Button to exit the application
tk.Button(root, text="Exit", command=exit_application).pack(pady=5)

# Run the Application
root.mainloop()