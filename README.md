### Importing Libraries
```python
import tkinter as tk  # Tkinter for creating the GUI
from tkinter import filedialog, messagebox  # File dialog and messagebox for interaction with the user
from pdf2image import convert_from_path  # pdf2image to convert PDF pages to images
import os  # os module for file path operations
```
- **tkinter**: Importing the `tkinter` library as `tk` for creating a GUI.
- **filedialog, messagebox**: Importing `filedialog` (for file/folder selection dialogs) and `messagebox` (for pop-up messages).
- **pdf2image**: Importing the `convert_from_path` function to convert PDF pages into image objects.
- **os**: Importing the `os` module to work with file and folder paths.

---

### Function to Convert PDF Pages to Images
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
1. **Function Definition**: Defines `convert_pdf_to_images`, which takes the path of a PDF file (`pdf_path`), an output folder (`output_folder`), and a desired image format (`file_type`).
2. **PDF Conversion**: `convert_from_path` converts each page of the PDF into an image and returns a list of images.
3. **Saving Images**: Loops through each image, setting a filename with a page number and the selected file type, and saves it to the specified folder.
4. **Error Handling**: Uses `try...except` to show a success message on completion or an error message if any error occurs during the conversion process.

---

### PDF File Selection
```python
def select_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select PDF File"
    )
    if file_path:
        pdf_path_var.set(file_path)
```
- **select_pdf**: Function to open a dialog box to select a PDF file.
- **`filedialog.askopenfilename`**: Opens a file selection dialog restricted to PDF files. If the user selects a file, its path is saved in `pdf_path_var`.

---

### Output Folder Selection
```python
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)
```
- **select_output_folder**: Function to open a dialog to select a folder where converted images will be saved.
- **`filedialog.askdirectory`**: Opens a folder selection dialog, and the selected folder path is stored in `output_folder_var`.

---

### Start Conversion Process
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
1. **start_conversion**: Main function to start the PDF-to-image conversion.
2. **Get Paths**: Retrieves the PDF path, output folder path, and file type from their respective variables.
3. **Validation**: Checks if both the PDF path and output folder are selected and verifies that the file type is supported.
4. **Conversion**: Calls `convert_pdf_to_images` if all inputs are valid.

---

### Exit the Application
```python
def exit_application():
    root.quit()
```
- **exit_application**: Exits the application by stopping the Tkinter main loop.

---

### Setting Up the GUI Window
```python
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("400x525")
```
- **root = tk.Tk()**: Creates the main Tkinter window.
- **title**: Sets the window title.
- **geometry**: Sets the window size to 400 pixels wide by 525 pixels high.

---

### Defining GUI Variables
```python
pdf_path_var = tk.StringVar()
output_folder_var = tk.StringVar()
file_type_var = tk.StringVar(value="PNG")
```
- **Variables**: Defines Tkinter `StringVar` variables to hold values for PDF path, output folder, and image format.
- **Default Format**: Sets `file_type_var` to default as "PNG".

---

### GUI Components for PDF File Selection
```python
tk.Label(root, text="PDF File:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select PDF File", command=select_pdf).pack(pady=5)
```
1. **Label**: Displays the label "PDF File".
2. **Entry Box**: Shows the selected PDF file path in a read-only entry box.
3. **Button**: A button to open the PDF selection dialog.

---

### GUI Components for Output Folder Selection
```python
tk.Label(root, text="Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly').pack(padx=10)
tk.Button(root, text="Select Output Folder", command=select_output_folder).pack(pady=5)
```
1. **Label**: Displays the label "Output Folder".
2. **Entry Box**: Shows the selected output folder path in a read-only entry box.
3. **Button**: Opens the output folder selection dialog.

---

### Image Format Selection Dropdown
```python
tk.Label(root, text="Select Image Format:").pack(pady=5)
file_type_options = ["PNG", "JPEG", "BMP", "TIFF"]
file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options)
file_type_menu.pack(pady=5)
```
1. **Label**: Displays "Select Image Format".
2. **Dropdown Menu**: An option menu to select the image file type. Options are defined in `file_type_options`.

---

### Conversion and Exit Buttons
```python
tk.Button(root, text="Convert to Images", command=start_conversion).pack(pady=20)
tk.Button(root, text="Exit", command=exit_application).pack(pady=5)
```
1. **Convert Button**: Starts the conversion by calling `start_conversion`.
2. **Exit Button**: Exits the application by calling `exit_application`.

---

### Running the Main Loop
```python
root.mainloop()
```
- **root.mainloop()**: Runs the Tkinter main event loop, allowing the GUI to function and respond to user actions.
