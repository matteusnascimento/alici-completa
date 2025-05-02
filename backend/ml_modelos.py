import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def resposta_ia(mensagem_usuario):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é a Alici, uma assistente simpática e prestativa."},
                {"role": "user", "content": mensagem_usuario}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return resposta.choices[0].message["content"].strip()
    except Exception as e:
        return f"Erro: {e}"