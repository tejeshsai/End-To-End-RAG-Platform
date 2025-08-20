**Week-wise learning path (RAG + CI/CD integration)**.

---

## 🗓 4 Weeks Full Map with CI/CD

### ✅ Week 1 – Python Foundations - Done

**Goal**: Clean scripts + test coverage ready for CI

* **Learn**:

  * Python OOP (classes, inheritance)
  * File I/O (PDF → JSON)
  * Context managers, decorators
  * Error handling, logging
  * Unit Testing (`pytest`)

* **Project work**:

  * Script: *Read PDF → Extract text → Save JSON*
  * Write 2–3 pytest unit tests (ex: check JSON format, text not empty)

* **CI/CD**:

  * Create GitHub repo
  * Add `.github/workflows/ci.yml` → run pytest on every push

---

### ✅ Week 2 – FastAPI Basics

**Goal**: Serve your PDF extraction as API

* **Learn**:

  * FastAPI routes (GET/POST)
  * Request/Response models (Pydantic)
  * Async routes
  * Testing APIs with Postman

* **Project work**:

  * `/upload-pdf` → upload PDF & return text
  * `/search` → dummy search (return hardcoded JSON)

* **CI/CD**:

  * Extend workflow: run FastAPI test cases
  * Deploy automatically to **Railway/Render** on `main` branch merge

    * GitHub Actions → Railway deploy

---

### ✅ Week 3 – Embeddings + Vector DB

**Goal**: Semantic search powered by embeddings

* **Learn**:

  * Embeddings concept
  * OpenAI embeddings API (`text-embedding-3-small`)
  * Vector search (cosine similarity)
  * Use **ChromaDB** locally

* **Project work**:

  * Extracted PDF text → create embeddings → store in ChromaDB
  * `/semantic-search` API → input query → return top 3 chunks

* **CI/CD**:

  * Add step to workflow → run **embedding tests** (mock OpenAI API calls)
  * Use `.env` secrets in GitHub Actions (store OPENAI\_API\_KEY safely)

---

### ✅ Week 4 – LangChain + Retrieval QA

**Goal**: End-to-end RAG system

* **Learn**:

  * LangChain basics: loaders, vectorstore, retriever
  * RetrievalQA chain (PDF → question answering)
  * Connect with OpenAI model

* **Project work**:

  * Upload PDF → embed → store → ask question → return LLM answer
  * Final API endpoints:

    * `/upload` (PDF)
    * `/semantic-search` (vector search)
    * `/ask` (RAG answer)

* **CI/CD**:

  * Add staging + production workflows (two environments)
  * Automatic deployment on merge
  * Add code formatter (black) + linting (flake8) in pipeline
  * Optional: Dockerize app → push to DockerHub → deploy with Actions

---

📌 **End Result after 4 Weeks:**

* 🚀 Full RAG pipeline (upload → embed → search → answer)
* ✅ Tested with pytest
* 🔄 CI/CD pipeline with GitHub Actions (test + lint + deploy)
* 🌍 Live FastAPI app hosted (Railway/Render/Docker)
* 🏆 Industry-ready project for portfolio

---
