
import pdfplumber
import json
import os
import io

class PdfReader():
    def __init__(self, pdf_bytes : io.BytesIO):
        self.text = None
        self.pdf_bytes = pdf_bytes
        self.pages = []

    def __enter__(self):
        self.read_pdf()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pages = []
        self.text = None
        self.pdf_bytes = None
    
    def read_pdf(self):
        try:
            with pdfplumber.open(self.pdf_bytes) as pdf:
                self.pages = [page.extract_text() for page in pdf.pages]
            self.text = "/n".join(self.pages)
    
        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")
        
    def get_text(self):
        return self.text or ""
    
    def get_page(self, page_number : int) -> str:
        if page_number < 0 or page_number >= len(self.pages):
            raise IndexError(f"Page number {page_number} is out of range")
        
        return self.pages[page_number]  
    
    def get_pages(self, page_number_start : int, page_number_end : int) -> list[str]:
        if not self.pages:
            raise Exception("Call read pdf method first!")
        if page_number_start < 0 or page_number_end < 0 or page_number_start >= len(self.pages) or page_number_end >= len(self.pages):
            raise IndexError(f"Page number {page_number_start} or {page_number_end} is out of range")
        if page_number_start > page_number_end:
            raise ValueError(f"Page number {page_number_start} is greater than {page_number_end}")
        if page_number_start == page_number_end:
            return [self.pages[page_number_start]]
        
        return self.pages[page_number_start:page_number_end+1]
    
    def get_page_count(self) -> int:
        return len(self.pages) or 0
    
    def save_json(self, json_path : str):
        json_data = {
            "length" : self.get_page_count(),
            "pages" : []
        }

        parent_dir = os.path.dirname(json_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
            
        for page_number, page in enumerate(self.pages):
            json_data["pages"].append({
                "page_number" : page_number,
                "page_text" : page.strip()
            })

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)