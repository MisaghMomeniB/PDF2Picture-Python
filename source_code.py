# Import necessary modules for GUI, file handling, PDF to image conversion
import tkinter as tk  # Tkinter for creating the GUI
from tkinter import filedialog, messagebox  # File dialog and messagebox for interaction with the user
from pdf2image import convert_from_path  # pdf2image to convert PDF pages to images
import os  # os module for file path operations

# Function to convert each page of a PDF to an image and save in the specified folder
def convert_pdf_to_images(pdf_path, output_folder, file_type):
    try:
        # Convert each page of the PDF to an image using convert_from_path (returns a list of images)
        images = convert_from_path(pdf_path)
        
        # Loop through each image (each page of the PDF)
        for i, image in enumerate(images):
            # Define the output file path for each image with the specified file type (e.g., PNG, JPEG)
            output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
            
            # Save the image in the specified format (file_type.upper() ensures it's in uppercase)
            image.save(output_path, file_type.upper())
        
        # Show a success message once the conversion is done
        messagebox.showinfo("Success", "PDF successfully converted to images!")
    
    except Exception as e:
        # In case of an error (e.g., if PDF cannot be read), show an error message
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a file dialog to select a PDF file
def select_pdf():
    # Ask the user to select a PDF file from their system using a file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],  # Limit file selection to PDF files only
        title="Select PDF File"  # Dialog title
    )
    # If the user selects a file, store its path in the pdf_path_var variable
    if file_path:
        pdf_path_var.set(file_path)

# Function to open a directory dialog to select the output folder
def select_output_folder():
    # Ask the user to select an output folder using a directory dialog
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    # If the user selects a folder, store its path in the output_folder_var variable
    if folder_path:
        output_folder_var.set(folder_path)

# Function to start the conversion process after verifying paths and file type
def start_conversion():
    # Retrieve the file paths and the selected image format from the variables
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()  # Standardize the file type to uppercase
    
    # Verify if both the PDF file and output folder are selected
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file!")
        return
    if not output_folder:
        messagebox.showwarning("Warning", "Please select an output folder!")
        return
    
    # Verify if the selected file type is one of the supported formats (PNG, JPEG, BMP, TIFF)
    if file_type not in ["PNG", "JPEG", "BMP", "TIFF"]:
        messagebox.showwarning("Warning", "Unsupported file type selected!")
        return

    # If all validations are passed, call the function to convert the PDF to images
    convert_pdf_to_images(pdf_path, output_folder, file_type)

# Function to close the application
def exit_application():
    # Exit the Tkinter application
    root.quit()

# Setup the main GUI window
root = tk.Tk()  # Create a Tkinter window
root.title("PDF to Image Converter")  # Set the window title
root.geometry("400x525")  # Set the window size (width x height)

# Variables to store the file paths and the selected image format
pdf_path_var = tk.StringVar()  # Variable to store the selected PDF file path
output_folder_var = tk.StringVar()  # Variable to store the selected output folder path
file_type_var = tk.StringVar(value="PNG")  # Variable to store the selected image format (default is PNG)

# PDF file selection label and entry box
tk.Label(root, text="PDF File:").pack(pady=5)  # Label for the PDF file input
tk.Entry(root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)  # Display the PDF file path in a readonly entry box
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)  # Button to open file dialog for PDF selection

# Output folder selection label and entry box
tk.Label(root, text="Output Folder:").pack(pady=5)  # Label for the output folder input
tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)  # Display the output folder path in a readonly entry box
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)  # Button to open folder dialog for output folder selection

# Dropdown menu for selecting the image format
tk.Label(root, text="Select Image Format:").pack(pady=5)  # Label for the image format selection
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]  # List of supported image formats
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)  # Dropdown menu for image format selection
file_type_menu.pack(pady=5)

# Button to start the conversion process
tk.Button(root, text="Convert to Images", command=start_conversion).pack(pady=20)  # Button to initiate the PDF to image conversion

# Button to exit the application
tk.Button(root, text="Exit", command=exit_application).pack(pady=5)  # Button to exit the application

# Run the main GUI event loop to display the window
root.mainloop()