# 📄 PDF to Image Converter

🚀 Welcome to the **PDF to Image Converter**! Transform your PDF files into high-quality images with just a few clicks. This tool is built with a clean and intuitive GUI, making the conversion process simple and hassle-free. 🌟

---

## ✨ Features

- **🖥️ User-Friendly Interface:** Easy-to-navigate GUI powered by Tkinter.
- **🎨 Multi-Format Support:** Export images in PNG, JPEG, BMP, or TIFF formats.
- **📂 Custom Output Folder:** Select any folder for saving the images.
- **📜 Batch Processing:** Converts all pages of a PDF into separate images.
- **⚠️ Error Handling:** User-friendly alerts for unsupported formats or missing files.

---

## 🔧 Prerequisites

Before using the application, ensure the following requirements are met:

1. **Python 3.x** installed on your system.
2. Install the required Python modules:
   - `tkinter` (comes pre-installed with Python)
   - `pdf2image` (install via `pip install pdf2image`)
   - `Pillow` (install via `pip install Pillow`)

Additionally, ensure `poppler` is installed for PDF rendering:

- **Windows:** Download from [Poppler Windows](http://blog.alivate.com.au/poppler-windows/), extract it, and add the `bin` folder to your PATH.
- **macOS:** Install via Homebrew (`brew install poppler`).
- **Linux:** Install via your package manager (`sudo apt install poppler-utils`).

---

## 🛠️ How to Use

1. **Run the Application:** Launch the script using Python.
2. **Select a PDF File:** Click the "Select PDF File" button to choose the file you want to convert.
3. **Choose an Output Folder:** Select where the output images will be saved.
4. **Pick an Image Format:** Use the dropdown menu to select your preferred image format (PNG, JPEG, BMP, or TIFF).
5. **Start Conversion:** Hit the "Convert to Images" button to begin the process.
6. **Success Message:** A popup will notify you when the conversion is complete. 🎉

---

## 🧠 Code Analysis (Line-by-Line)

### 🚪 Imports
```python
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os
```
- **`tkinter`**: Used to create the graphical user interface.
- **`filedialog` & `messagebox`**: For file selection dialogs and user notifications.
- **`pdf2image`**: Converts PDF pages into images.
- **`os`**: Handles file and directory operations.

### 📷 Function: `convert_pdf_to_images`
```python
def convert_pdf_to_images(pdf_path, output_folder, file_type):
    try:
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
            image.save(output_path, file_type.upper())
        messagebox.showinfo("Success", "PDF successfully converted to images!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
```
- Converts PDF pages into images and saves them in the chosen format.
- Displays a success message or an error popup depending on the outcome.

### 📂 Function: `select_pdf`
```python
def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Select PDF File")
    if file_path:
        pdf_path_var.set(file_path)
```
- Allows users to select a PDF file and stores the file path.

### 🗂️ Function: `select_output_folder`
```python
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)
```
- Lets users choose an output directory for saving images.

### ✅ Function: `start_conversion`
```python
def start_conversion():
    pdf_path = pdf_path_var.get()
    output_folder = output_folder_var.get()
    file_type = file_type_var.get().upper()
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
- Ensures all inputs are valid before calling the conversion function.
- Alerts users if any inputs are missing or incorrect.

### ❌ Function: `exit_application`
```python
def exit_application():
    root.quit()
```
- Closes the application.

### 🖥️ GUI Setup
```python
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("400x525")
```
- Initializes the main application window.

### 🖊️ GUI Components
#### File Selection
```python
tk.Label(root, text="PDF File:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)
```
- Provides a field and button to select a PDF file.

#### Output Folder
```python
tk.Label(root, text="Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)
```
- Allows users to select where the images will be saved.

#### Image Format Dropdown
```python
tk.Label(root, text="Select Image Format:").pack(pady=5)
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.pack(pady=5)
```
- Dropdown menu to select the image format.

#### Action Buttons
```python
tk.Button(root, text="Convert to Images", command=start_conversion).pack(pady=20)
tk.Button(root, text="Exit", command=exit_application).pack(pady=5)
```
- Buttons for starting the conversion and exiting the application.

### 🔁 Event Loop
```python
root.mainloop()
```
- Runs the main application loop to keep the GUI active.

---

## 📸 Screenshots
_(Add your application screenshots here for a visual showcase!)_

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and enhance it as you wish!

---

💡 **We welcome contributions!** Fork this repository, submit pull requests, or open issues to help improve the project. Let us know your thoughts! 💬
