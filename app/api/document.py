from http import HTTPStatus
from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.model import user as userDB
from app.schemas.document import DocumentResponse
from app.services import document_service
from app.schemas.search import SearchRequest
from app.services import search_service
import logging

from app.services.rag_service import answer_question

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix = "/documents",
    tags=["Documents"]
)

ALLOWED_MIME_TYPES = {"application/pdf",
                      "text/plain",
                      "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                     }
@router.post("/upload",response_model=DocumentResponse)
async def upload_document(
        file : UploadFile,
        current_user:userDB = Depends(get_current_user),
        db:Session = Depends(get_db)):

    if file.content_type not in ALLOWED_MIME_TYPES:
        logger.warning("Unsupported file type uploaded: %s",
                    file.content_type)
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="Invalid file type uploaded")

    contents = await file.read()

    return document_service.upload_document(
        contents,
        file.content_type,
        file.filename,
        db,
        current_user
    )


    # {
    #     "filename": file.filename,
    #     "content_type": file.content_type,
    #     "size": len(contents)
    # }

@router.post("/search")
def search_in_file(
        request : SearchRequest,
        user : userDB = Depends(get_current_user)
):
    answer = answer_question(
        request.query,
        user.id
    )

    return {
        "answer": answer
    }
