
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Modelos disponíveis:\n")

for modelo in cliente.models.list():
    nome = modelo.name

    if "gemini" in nome.lower():
        print(nome)
