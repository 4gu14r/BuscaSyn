import sys
import json
import argparse

from functions.semantica import buscar_registros
from data.dados import carregar_dados
from utils.dicionario import obter_sinonimos
from utils.portugues_function import processar_entrada

class MeuArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'Erro: {message}\n')
        self.print_help()
        sys.exit(2)

def config():
    # Utiliza a classe personalizada MeuArgumentParser
    parser = MeuArgumentParser(description='Programa para carregar dados de um JSON e buscar registros.')
    parser.add_argument('--arquivo', type=str, required=True, help='Caminho para o arquivo JSON.')
    parser.add_argument('--termo', type=str, required=True, help='Termo para buscar nos registros.')
    
    args = parser.parse_args()

    # Carrega os dados do arquivo
    registros = carregar_dados(args.arquivo)
    if registros["status"] != "success":
        print(json.dumps(registros, indent=4, ensure_ascii=False))
        sys.exit(1)
    
    return args, registros

if __name__ == "__main__":
    args, dados = config()

    palavra_corrigida = processar_entrada(args.termo)

    resultados = list()

    sinonimos = obter_sinonimos(palavra_corrigida) or []

    if sinonimos:
        for p in sinonimos:
            resultados.extend(buscar_registros(p, dados))
    else:
        resultados.extend(buscar_registros(palavra_corrigida, dados))

    
    # Remove duplicatas
    resultados_unicos = []
    chaves_vistas = set()
    for registro in resultados:
        chave = json.dumps(registro, sort_keys=True)
        if chave not in chaves_vistas:
            resultados_unicos.append(registro)
            chaves_vistas.add(chave)

    resposta = {
        "status": "success",
        "data": resultados_unicos,
        "message": f"Foram encontrados {len(resultados_unicos)} registros para o termo '{args.termo}'"
    }

    print(json.dumps(resposta, indent=4, ensure_ascii=False))