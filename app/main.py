import json
import re
from utils.similaridade import similaridade
from utils.dicionario import obter_sinonimos  
from layout.resultados import exibir_resultados

def carregar_dados():
    with open('app/data/dados.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def obterTexto(registro):
    return f"{registro['local']} {registro['titulo']} {registro['descricao']}"

def palavra_texto(word, text):
    return word.lower() in re.findall(r'\w+', text.lower())

def buscar_registros(palavra, dados):
    resultados = []
    ids_encontrados = set()  

    print(f"\n🔍 Buscando registros para: {palavra}") 

    for registro in dados:
        texto_completo = obterTexto(registro)

        # Palavra exata
        if palavra_texto(palavra, texto_completo):
            if registro['id'] not in ids_encontrados:
                resultados.append(registro)
                ids_encontrados.add(registro['id'])
            continue

        # Similaridade
        sim_categoria = similaridade(palavra, registro['categoria'])
        sim_titulo = similaridade(palavra, registro['titulo'])
        sim_descricao = similaridade(palavra, registro['descricao'])

        if sim_categoria > 0.5 or sim_titulo > 0.5 or sim_descricao > 0.5:
            if registro['id'] not in ids_encontrados:
                print(f"✅ Adicionado por similaridade: {registro['titulo']}")
                resultados.append(registro)
                ids_encontrados.add(registro['id'])

    return resultados




def main():
    dados = carregar_dados()
    
    while True:
        palavra = input("Digite uma palavra para buscar (ou 'sair' para encerrar): ").strip()
        if palavra.lower() == 'sair':
            print("Encerrando a busca.")
            break

        sinonimos = obter_sinonimos(palavra)
        resultados = {} 

        for p in sinonimos:
            for registro in buscar_registros(p, dados):
                resultados[registro['id']] = registro

        exibir_resultados(list(resultados.values()))  #


if __name__ == "__main__":
    main()
