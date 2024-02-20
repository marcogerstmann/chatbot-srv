from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.sync_embeddings_schema import SyncEmbeddingsSchema
from app.services.embeddings_service import EmbeddingsService

router = APIRouter(prefix="/embeddings")


# TODO: Secure these endpoints or implement another private way to create embeddings
@router.post("/embeddings", response_model=bool)
def post_embeddings(
    request: SyncEmbeddingsSchema,
    db_service: Annotated[EmbeddingsService, Depends(EmbeddingsService)],
) -> bool:
    """Create embeddings"""

    return db_service.sync_embeddings(request.chatbot_id)