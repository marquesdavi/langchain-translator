from pydantic import BaseModel

class Request(BaseModel):
    sentence: str

class Response(BaseModel):
    output: str
