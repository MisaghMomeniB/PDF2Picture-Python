import tkinter as tk  # Import the Tkinter library for GUI
from tkinter import filedialog, messagebox  # Import file dialog and message box from Tkinter
from pdf2image import convert_from_path  # Import convert_from_path from pdf2image for PDF conversion
import os  # Import os for file path operations
from tkinter import ttk  # Import themed Tkinter widgets

# Initialize the main window
tk_root = tk.Tk()
tk_root.title("PDF to Image Converter")  # Set window title
tk_root.geometry("400x525")  # Set window size

# Define Tkinter StringVar for storing paths and file types
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()
file_type_var = tk.StringVar(value="PNG")  # Default file type is PNG

# Create a progress bar
progress_bar = ttk.Progressbar(tk_root, length=300, mode="determinate")
progress_bar.pack(pady=5)  # Add padding around the progress bar

# Function to convert PDF to images
def convert_pdf_to_images(pdf_path, output_folder, file_type):
    try:
        images = convert_from_path(pdf_path)  # Convert PDF to a list of images
        total_pages = len(images)
        progress_bar["maximum"] = total_pages  # Set progress bar maximum
        for i, image in enumerate(images):
            # Save each page as an image in the specified format
            output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
            image.save(output_path, file_type.upper())
            progress_bar["value"] = i + 1  # Update progress bar
            tk_root.update_idletasks()  # Update the GUI
        messagebox.showinfo("Success", "PDF successfully converted to images!")  # Success message
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")  # Error message if conversion fails

# Function to open a file dialog and select the PDF file
def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Select PDF File")
    if file_path:
        pdf_path_var.set(file_path)  # Store the selected PDF path

# Function to select the output folder
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)  # Store the selected output folder path

# Function to start the conversion process
def start_conversion():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()
    if not pdf_path or not output_folder:
        messagebox.showwarning("Warning", "Please select a PDF file and an output folder!")
        return
    if file_type not in ["PNG", "JPEG", "BMP", "TIFF"]:
        messagebox.showwarning("Warning", "Unsupported file type selected!")
        return
    convert_pdf_to_images(pdf_path, output_folder, file_type)  # Call the conversion function

# Function to exit the application
def exit_application():
    tk_root.quit()  # Quit the Tkinter application

# Create GUI components for selecting PDF, output folder, and conversion
# PDF Selection
tk.Label(tk_root, text="PDF File:").pack(pady=5)
tk.Entry(tk_root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)
tk.Button(tk_root, text="Select PDF File", command=select_pdf).pack(pady=5)

# Output Folder Selection
tk.Label(tk_root, text="Output Folder:").pack(pady=5)
tk.Entry(tk_root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)
tk.Button(tk_root, text="Select Output Folder", command=select_output_folder).pack(pady=5)

# File Type Selection
tk.Label(tk_root, text="Select Image Format:").pack(pady=5)
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]
file_type_menu = tk.OptionMenu(tk_root, file_type_var, *file_type_options)
file_type_menu.pack(pady=5)

# Buttons for starting conversion and exiting
tk.Button(tk_root, text="Convert to Images", command=start_conversion).pack(pady=20)
tk.Button(tk_root, text="Exit", command=exit_application).pack(pady=5)

# Start the Tkinter event loop
tk_root.mainloop()