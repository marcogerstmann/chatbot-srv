from fastapi import APIRouter

from app.services.embeddings_services import create_embeddings

router = APIRouter(prefix="/embeddings")


# TODO: Secure this endpoint or implement another private way to create embeddings
@router.post("", response_model=bool)
def post_embeddings() -> bool:
    """Create embeddings"""

    return create_embeddings()
