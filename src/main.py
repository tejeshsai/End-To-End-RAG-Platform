from fastapi import FastAPI
from src.routes import pdf_routes

app = FastAPI(title="RAG PDF project")

app.include_router(pdf_routes.router)

# if __name__ == "__main__":
#     with PdfReader("data/sample-local-pdf.pdf") as r:
#         print(r.get_page(0))
#         print("Length of the pdf is ",r.get_page_count())
#         r.save_json("data/sample.json")
