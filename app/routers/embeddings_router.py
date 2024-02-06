from fastapi import APIRouter

from app.services.embeddings_service import sync_embeddings

router = APIRouter(prefix="/embeddings")


# TODO: Secure this endpoint or implement another private way to create embeddings
@router.post("", response_model=bool)
def post_embeddings() -> bool:
    """Create embeddings"""

    return sync_embeddings()
