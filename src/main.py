from pdfReader import PdfReader

if __name__ == "__main__":
    with PdfReader("data/sample-local-pdf.pdf") as r:
        print(r.get_page(0))
        print("Length of the pdf is ",r.get_page_count())
        r.save_json("data/sample.json")

