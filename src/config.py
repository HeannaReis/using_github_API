import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_USER or not TOKEN:
    raise ValueError("❌ ERRO: Variáveis de ambiente GITHUB_USER e GITHUB_TOKEN não foram encontradas!")

API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
    