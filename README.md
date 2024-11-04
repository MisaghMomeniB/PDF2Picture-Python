__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# PDF2Picture-Python🐍
I Wrote a Program Using ***Python*** and Tkinter That Allows You to Convert PDF Files Into Images.

# Does It Require Any Installation Steps or Prerequisites?
`` pip install pdf2image Pillow `` <br>
`` sudo apt-get install poppler-utils `` <br>

# Line-by-line Code Analysis

1. **Importing Libraries**:
   ```python
   import tkinter as tk
   from tkinter import filedialog, messagebox
   from pdf2image import convert_from_path
   import os
   ```
   - This section imports the necessary libraries for creating a graphical user interface (GUI) using `tkinter` and for converting PDF files to images using `pdf2image`. The `os` library is imported for handling file paths.

2. **Defining the Function to Convert PDF to Images**:
   ```python
   def convert_pdf_to_images(pdf_path, output_folder, file_type):
   ```
   - This function is responsible for converting each page of a PDF file into an image and saving them in the specified output folder.

3. **Converting PDF Pages to Images**:
   ```python
   images = convert_from_path(pdf_path)
   ```
   - Here, `convert_from_path` is used to convert all pages of the PDF into images.

4. **Saving the Images**:
   ```python
   for i, image in enumerate(images):
       output_path = os.path.join(output_folder, f"page_{i + 1}.{file_type.lower()}")
       image.save(output_path, file_type.upper())
   ```
   - In this loop, each image is saved with a specified name (e.g., `page_1.png`) in the output folder. The name of the image is based on the page number.

5. **Success or Error Message**:
   ```python
   messagebox.showinfo("Success", "PDF successfully converted to images!")
   ```
   - If the conversion is successful, a success message is displayed. If an error occurs, an error message is shown.

6. **Selecting a PDF File**:
   ```python
   def select_pdf():
       file_path = filedialog.askopenfilename(
           filetypes=[("PDF Files", "*.pdf")], 
           title="Select PDF File"
       )
       pdf_path_var.set(file_path)
   ```
   - This function allows the user to select a PDF file and sets the path in a variable.

7. **Selecting Output Folder**:
   ```python
   def select_output_folder():
       folder_path = filedialog.askdirectory(title="Select Output Folder")
       output_folder_var.set(folder_path)
   ```
   - This function allows the user to select a folder for saving the images and sets the path in a variable.

8. **Starting the Conversion Process**:
   ```python
   def start_conversion():
   ```
   - This function is called to initiate the conversion process. It first checks the inputs (whether the PDF file and output folder have been selected) and then calls the conversion function.

9. **Setting Up the GUI**:
   ```python
   root = tk.Tk()
   root.title("PDF to Image Converter")
   root.geometry("400x350")
   ```
   - This section creates the main application window with a title and specified dimensions.

10. **Defining Variables to Store Paths and Image Format**:
    ```python
    pdf_path_var = tk.StringVar()
    output_folder_var = tk.StringVar()
    file_type_var = tk.StringVar(value="PNG")  # Default to PNG
    ```
    - Variables are created to hold the paths of the PDF file, output folder, and the selected image format.

11. **Creating GUI Elements**:
    - Labels and input fields for each input (PDF file, output folder, and image format) are created. Buttons for selecting the file and folder, as well as a button to start the conversion, are also included.

12. **Running the Application**:
    ```python
    root.mainloop()
    ```
    - Finally, the program enters the main loop to be ready for user interaction.

### Purpose of the Code
The overall purpose of this code is to provide a user-friendly interface for converting PDF files into image formats (like PNG, JPEG, BMP, and TIFF) using a graphical interface, allowing users to easily select a PDF file and an output folder for the converted images.
