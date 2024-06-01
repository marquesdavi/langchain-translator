import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
from decouple import config

OPENAI_API_KEY = config("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Translator",
    version="1.0",
    description="LangChain translate API",
)

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=OPENAI_API_KEY
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
