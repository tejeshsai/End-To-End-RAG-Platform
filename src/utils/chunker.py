def chunk_text(text : str, chunk_size : int = 500, overlap : int = 50) -> list[str]:
    chunks = []
    words = text.split()
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start +=chunk_size - overlap
    return chunks