# PDF Upload API - Quick Start Guide

## 🚀 How to Run the Server

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server:**
   ```bash
   uvicorn src.main:app --reload
   ```

3. **Access the API documentation:**
   - Open your browser and go to: http://localhost:8000/docs
   - This will show you the interactive Swagger UI

## 📁 PDF Upload Endpoint

### Endpoint Details
- **URL:** `POST /pdf/uploadpdf/`
- **Content-Type:** `multipart/form-data`
- **Parameter:** `file` (PDF file)

### Features
- ✅ Validates PDF file type
- ✅ Limits file size to 10MB
- ✅ Creates `uploads/` directory automatically
- ✅ Returns detailed response with file info

## 🧪 How to Test PDF Upload

### Method 1: Using the Test Script
```bash
python test_upload.py
```

### Method 2: Using curl
```bash
curl -X POST -F "file=@data/sample-local-pdf.pdf" http://localhost:8000/pdf/uploadpdf/
```

### Method 3: Using Python requests
```python
import requests

with open('data/sample-local-pdf.pdf', 'rb') as f:
    files = {'file': ('sample.pdf', f, 'application/pdf')}
    response = requests.post('http://localhost:8000/pdf/uploadpdf/', files=files)
    print(response.json())
```

### Method 4: Using the Swagger UI
1. Go to http://localhost:8000/docs
2. Find the `/pdf/uploadpdf/` endpoint
3. Click "Try it out"
4. Upload your PDF file
5. Click "Execute"

## 📋 Expected Response

**Success Response (200):**
```json
{
  "message": "PDF uploaded successfully",
  "filename": "sample-local-pdf.pdf",
  "file_path": "uploads/sample-local-pdf.pdf",
  "file_size": 12345
}
```

**Error Response (400):**
```json
{
  "detail": "Only PDF files are allowed"
}
```

## 🔧 API Endpoints

- `GET /pdf/` - Test endpoint
- `POST /pdf/uploadpdf/` - Upload PDF file
- `GET /pdf/uploadpdf/` - Info message (use POST for upload)

## 📂 File Storage

Uploaded PDFs are stored in the `uploads/` directory in your project root. The directory is created automatically when the first file is uploaded.


