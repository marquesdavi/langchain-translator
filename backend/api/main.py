from api.settings import app
from api.service import get_translation
from api.models import *

@app.post("/translate", response_model=Response)
def translate(request: Request):
    return get_translation(request.sentence)
