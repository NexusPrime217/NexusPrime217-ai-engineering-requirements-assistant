from email_validator.syntax import check_unsafe_chars


def chunk_text(
        text:str,
        chunk_size: int =1000,
        overlap:int = 200
)->list[str]:

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")

    if overlap < 0:
        raise ValueError("Overlap can't be negative")

    chunks = []
    start=0
    step = chunk_size - overlap
    while start<len(text):
        end = start+chunk_size
        chunks.append(text[start:end])
        start+=step

    return chunks
