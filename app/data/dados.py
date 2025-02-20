import json
import sys

def carregar_dados(caminho_arquivo):
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            if isinstance(dados, list):
                return {
                    "status": "success",
                    "data": dados,
                    "message": "Dados carregados com sucesso"
                }
            
            # Qualquer outro formato
            return {
                "status": "error",
                "data": None,
                "message": "Formato do arquivo Json inválido"
            }
    
    except FileNotFoundError:
        return {
            "status": "error",
            "data": None,
            "message": f"Arquivo {caminho_arquivo} não encontrado"
        }
    
    except json.JSONDecodeError:
        return {
            "status": "error",
            "data": None,
            "message": "Arquivo JSON inválido ou corrompido"
        }