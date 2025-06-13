# 🖼️ PDF2Picture (Python)

A lightweight Python tool to **convert PDF documents into images** (per‑page JPG or PNG). Ideal for document previews, thumbnail generation, or embedding pages as images in web and mobile apps.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Code Structure](#code-structure)  
7. [Implementation Details](#implementation-details)  
8. [Enhancement Ideas](#enhancement-ideas)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## 💡 Overview

PDF2Picture converts each page of a PDF into high-quality image files. It uses libraries like **pdf2image** or **PyMuPDF** to render pages and supports batch conversions, DPI control, and format options (JPG/PNG).

---

## ✅ Features

- 📄 Convert all pages in a PDF to image(s)
- ⚙️ Configure DPI (e.g., 150–300) for resolution control  
- 🗂️ Supports output formats `.jpg` and `.png`  
- 🔁 Batch process multiple PDFs in a folder  
- 🧰 Easy CLI and importable library interface

---

## 🛠️ Prerequisites

- Python **3.7+**  
- System dependency: **Poppler** tools (e.g., `pdftoppm`) installed and available in `PATH`  
- Python libraries:

```bash
pip install pdf2image
````

Or for enhanced rendering using PyMuPDF:

```bash
pip install PyMuPDF
```

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/PDF2Picture-Python.git
cd PDF2Picture-Python
pip install -r requirements.txt  # includes pdf2image
```

Ensure `pdftoppm` is set up on your system.

---

## 🚀 Usage

### CLI Example

Convert a PDF to PNG images at 200 DPI:

```bash
python pdf2picture.py \
  --input doc.pdf \
  --output-dir pages/ \
  --dpi 200 \
  --format png
```

This produces:

* `pages/doc_page_1.png`
* `pages/doc_page_2.png`
* …

### Python Module

```python
from pdf2picture import convert_pdf_to_images

images = convert_pdf_to_images(
    pdf_path="doc.pdf",
    output_dir="out/",
    dpi=150,
    fmt="jpg"
)
print(f"Converted {len(images)} pages")
```

---

## 📁 Code Structure

```
PDF2Picture-Python/
├── pdf2picture.py         # CLI interface & wrapper logic
├── pdf2picture_lib.py     # Core conversion functions
├── requirements.txt
└── README.md              # This file
```

* `convert_pdf_to_images(...)`: handles conversion and returns file paths
* CLI parses options via `argparse` and calls conversion logic

---

## 🔍 Implementation Details

* Uses `pdf2image.convert_from_path(...)` with DPI and format options
* Creates output directory if missing and saves images with page index
* Handles errors for invalid PDFs and missing Poppler tools

---

## 💡 Enhancement Ideas

* ✅ Add **PDF page range** selection (e.g., pages 1–5)
* 🗜️ Support **image compression** or resizing
* ☁️ Integrate with **web frameworks** (Flask/FastAPI) for upload/download
* 📦 Export images to **PDF or thumbnails** in a ZIP
* 🧪 Add **unit tests** and error-handling improvements

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a `feature/...` branch
3. Add clean, documented code
4. Open a Pull Request

---

## 📄 License

Released under the **MIT License** — see `LICENSE` for details.
