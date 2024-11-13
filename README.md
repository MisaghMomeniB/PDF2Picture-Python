__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# PDF2Picture-Python🐍
I Wrote a Program Using ***Python*** and Tkinter That Allows You to Convert PDF Files Into Images.

# Does It Require Any Installation Steps or Prerequisites?
`` pip install pdf2image Pillow `` <br>
`` sudo apt-get install poppler-utils `` <br>

# Line-by-line Code Analysis

### 1. Importing Required Modules
```python
import tkinter as tk  # Tkinter for creating the GUI
from tkinter import filedialog, messagebox  # File dialog and messagebox for interaction with the user
from pdf2image import convert_from_path  # pdf2image to convert PDF pages to images
import os  # os module for file path operations
```
- **tkinter**: Used to create the graphical user interface (GUI).
- **filedialog, messagebox**: Used for file selection and displaying messages (success or error).
- **pdf2image**: Used for converting PDF pages to images.
- **os**: Used for file path operations (like combining paths).

### 2. Function to Convert PDF to Images
```python
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
```
- This function is responsible for converting each page of a PDF into an image. It first uses `convert_from_path` to convert the PDF into images.
- Then, for each image (representing a page), it generates an output path based on the selected image format (`PNG`, `JPEG`, `BMP`, `TIFF`).
- If the conversion is successful, it shows a success message. If there's an error (e.g., the PDF can't be read), it shows an error message.

### 3. Function to Select the PDF File
```python
def select_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],  # Limit file selection to PDF files only
        title="Select PDF File"  # Dialog title
    )
    if file_path:
        pdf_path_var.set(file_path)
```
- This function opens a file dialog that allows the user to select a PDF file. Only PDF files are shown in the dialog.
- When the user selects a file, its path is stored in the `pdf_path_var` variable.

### 4. Function to Select the Output Folder
```python
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)
```
- This function opens a directory dialog that lets the user choose an output folder to save the converted images.
- The selected folder path is stored in the `output_folder_var` variable.

### 5. Function to Start the Conversion
```python
def start_conversion():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()  # Standardize the file type to uppercase
    
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file!")
        return
    if not output_folder:
        messagebox.showwarning("Warning", "Please select an output folder!")
        return
    
    if file_type not in ["PNG", "JPEG", "BMP", "TIFF"]:
        messagebox.showwarning("Warning", "Unsupported file type selected!")
        return

    convert_pdf_to_images(pdf_path, output_folder, file_type)
```
- This function retrieves the file paths and the selected image format from the variables. It ensures that the user has selected both a PDF file and an output folder, and that the selected image format is valid.
- If any validation fails (e.g., no PDF or output folder selected, or unsupported file type), a warning message is shown.
- If everything is valid, the `convert_pdf_to_images` function is called to start the conversion process.

### 6. Function to Exit the Application
```python
def exit_application():
    root.quit()
```
- This function is used to close the application when the user clicks the "Exit" button.

### 7. Setting Up the GUI
```python
root = tk.Tk()  # Create a Tkinter window
root.title("PDF to Image Converter")  # Set the window title
root.geometry("400x525")  # Set the window size (width x height)
```
- Here, the main window for the application is created using Tkinter. The title and size of the window are set.

### 8. Variables for Storing File Paths and Image Format
```python
pdf_path_var = tk.StringVar()  # Variable to store the selected PDF file path
output_folder_var = tk.StringVar()  # Variable to store the selected output folder path
file_type_var = tk.StringVar(value="PNG")  # Variable to store the selected image format (default is PNG)
```
- These variables are used to store the selected PDF file path, the output folder path, and the selected image format.

### 9. GUI Components (Labels, Entry Boxes, Buttons)
```python
tk.Label(root, text="PDF File:").pack(pady=5)  # Label for the PDF file input
tk.Entry(root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)  # Display the PDF file path in a readonly entry box
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)  # Button to open file dialog for PDF selection

tk.Label(root, text="Output Folder:").pack(pady=5)  # Label for the output folder input
tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)  # Display the output folder path in a readonly entry box
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)  # Button to open folder dialog for output folder selection

tk.Label(root, text="Select Image Format:").pack(pady=5)  # Label for the image format selection
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]  # List of supported image formats
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options).pack(pady=5)

tk.Button(root, text="Convert to Images", command=start_conversion).pack(pady=20)  # Button to initiate the PDF to image conversion

tk.Button(root, text="Exit", command=exit_application).pack(pady=5)  # Button to exit the application
```
- **Labels, Entry Boxes, and Buttons**: These components are added to the window for user interaction. 
  - Labels display the text for various fields (PDF file, output folder, image format).
  - Entry boxes display the paths of the selected PDF and output folder (in a read-only mode).
  - Buttons allow the user to select a PDF file, select an output folder, choose an image format, start the conversion, and exit the application.

### 10. Starting the GUI Event Loop
```python
root.mainloop()
