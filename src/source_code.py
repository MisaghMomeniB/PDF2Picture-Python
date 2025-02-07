import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf2image import convert_from_path
import os

# Initialize the main window
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("400x525")

# Variables to store paths and file type
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()
file_type_var = tk.StringVar(value="PNG")  # Default file type is PNG

# Progress bar
progress_bar = ttk.Progressbar(root, length=300, mode="determinate", orient=tk.HORIZONTAL)
progress_bar.pack(pady=5)

# Function to convert PDF to images
def convert_pdf_to_images(pdf_path, output_folder, file_type):
    """
    Convert a PDF file to images and save them in the specified output folder.
    """
    try:
        # Convert PDF to a list of images
        images = convert_from_path(pdf_path, dpi=300)  # Use 300 DPI for better image quality
        total_pages = len(images)
        progress_bar["maximum"] = total_pages  # Set progress bar maximum value

        for i, image in enumerate(images):
            # Save each page as an image in the specified format
            output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
            image.save(output_path, file_type.upper())
            progress_bar["value"] = i + 1  # Update progress bar
            root.update_idletasks()  # Refresh the GUI

        messagebox.showinfo("Success", "PDF successfully converted to images!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a file dialog and select the PDF file
def select_pdf():
    """
    Open a file dialog to select the input PDF file.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")], title="Select PDF File"
    )
    if file_path:
        pdf_path_var.set(file_path)

# Function to select the output folder
def select_output_folder():
    """
    Open a file dialog to select the output folder.
    """
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)

# Function to start the conversion process
def start_conversion():
    """
    Validate inputs and start the PDF-to-image conversion process.
    """
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()

    # Input validation
    if not pdf_path or not output_folder:
        messagebox.showwarning("Warning", "Please select a PDF file and an output folder!")
        return

    if file_type not in ["PNG", "JPEG", "BMP", "TIFF"]:
        messagebox.showwarning("Warning", "Unsupported file type selected!")
        return

    # Start the conversion process
    convert_pdf_to_images(pdf_path, output_folder, file_type)

# Function to exit the application
def exit_application():
    """
    Exit the application gracefully.
    """
    root.quit()

# Create GUI components
# PDF Selection
tk.Label(root, text="PDF File:").pack(pady=5)
pdf_entry = tk.Entry(root, textvariable=pdf_path_var, width=40, state="readonly")
pdf_entry.pack(padx=10)
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)

# Output Folder Selection
tk.Label(root, text="Output Folder:").pack(pady=5)
output_entry = tk.Entry(root, textvariable=output_folder_var, width=40, state="readonly")
output_entry.pack(padx=10)
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)

# File Type Selection
tk.Label(root, text="Select Image Format:").pack(pady=5)
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.pack(pady=5)

# Buttons for starting conversion and exiting
tk.Button(root, text="Convert to Images", command=start_conversion, bg="#4CAF50", fg="white").pack(pady=20)
tk.Button(root, text="Exit", command=exit_application, bg="#f44336", fg="white").pack(pady=5)

# Start the Tkinter event loop
root.mainloop()