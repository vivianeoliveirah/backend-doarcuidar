import os
from dotenv import load_dotenv

# 🔥 força carregar .env da raiz do projeto
load_dotenv()

class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")