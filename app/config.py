import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    OPENAI_MODEL = 'gpt-4o-mini'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
