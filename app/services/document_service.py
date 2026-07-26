from sqlalchemy.orm import Session
from app.rag.chunker import chunk_text
from app.model.document import Document as DocumentDB
from app.model import user as userDB
from app.parser import document_parser
from uuid import uuid4
from pathlib import Path
from app.core.config import setting
from app.rag.embedding_service import generate_embeddings
from app.rag.vector_store import store_document_chunks,delete_document_chunks

import logging

logger = logging.getLogger(__name__)


def extract_text(
    contents : bytes,
    content_type : str):
    if content_type == "text/plain":
        return document_parser.extract_txt(contents)

    elif content_type == "application/pdf":
        return document_parser.extract_pdf(contents)

    elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return document_parser.extract_docx(contents)

    raise ValueError("Unsupported document type")

def generate_unique_name(extension:str)-> str:
    unique_id= str(uuid4())
    return unique_id+extension

def upload_document(
        contents : bytes,
        content_type : str,
        filename: str,
        db:Session,
        current_user: userDB):
    text = extract_text(contents,content_type)
    chunks = chunk_text(text)

    # print(f"Extracted character: {len(text)}")
    # print(f"Chunks: {len(chunks)}")

    # for i,chunk in enumerate(chunks):
    #     print(i,len(chunk))

    embeddings = generate_embeddings(chunks)

    extension = Path(filename).suffix.lower()
    unique_filename = generate_unique_name(extension)
    root_path = Path(setting.DOCUMENT_PATH)
    root_path.mkdir(parents=True,exist_ok=True)
    filepath = root_path/unique_filename
    document_to_DB = None
    chroma_save = False
    try:
        with open(filepath,"wb") as f:
            f.write(contents)

        document_metadata = {
            "original_filename":filename,
            "stored_filename":unique_filename,
            "file_size":len(contents),
            "storage_path":str(filepath),
            "uploaded_by": current_user.id
        }


        document_to_DB=DocumentDB(**document_metadata)

        db.add(document_to_DB)

        db.flush()

        store_document_chunks(
            chunks=chunks,
            embeddings=embeddings,
            document_id=document_to_DB.id,
            user_id=document_to_DB.uploaded_by
        )

        db.commit()

        db.refresh(document_to_DB)



    except Exception:
        db.rollback()
        if filepath.exists():
            filepath.unlink()

        try:
            if document_to_DB is not None and document_to_DB.id is not None:
                delete_document_chunks(document_to_DB.id)
        except Exception:
            logger.exception("Failed to delete chroma chunks")

        logger.exception("Failed to save file")

        raise

    return document_to_DB



