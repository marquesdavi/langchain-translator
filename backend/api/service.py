from fastapi import HTTPException
from api.settings import client, logger
from api.models import Response
import re

def validate_sentence(sentence: str):
    if not sentence:
        logger.error("Validation Error: The sentence cannot be empty.")
        raise HTTPException(status_code=400, detail="The sentence cannot be empty.")
    if len(sentence) < 3:
        logger.error("Validation Error: The sentence is too short.")
        raise HTTPException(status_code=400, detail="The sentence is too short.")
    if len(sentence) > 500:
        logger.error("Validation Error: The sentence is too long.")
        raise HTTPException(status_code=400, detail="The sentence is too long.")
    if not re.match(r"^[a-zA-Z0-9\s,.?!'\"-]+$", sentence):
        logger.error("Validation Error: The sentence contains invalid characters.")
        raise HTTPException(status_code=400, detail="The sentence contains invalid characters.")

def get_translation(sentence: str) -> Response:
    validate_sentence(sentence)

    try:
        response = client.invoke(f"Translate the following sentence to Portuguese: {sentence}")
        return Response(output=response.content)
    except Exception as e:
        logger.error(f"Translation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
