import json
import re
from similaridade import similaridade
from dicionario import obter_sinonimos  

def carregar_dados():
    with open('app/dados.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_text_from_registro(registro):
    return f"{registro['local']} {registro['titulo']} {registro['descricao']}"

# Função auxiliar para verificar se uma palavra aparece como palavra inteira em um texto
def word_in_text(word, text):
    # Aqui usamos re.findall para obter todas as palavras e checamos se a palavra desejada está entre elas
    return word.lower() in re.findall(r'\w+', text.lower())

def buscar_registros(palavra, dados):
    resultados = []
    
    sinonimos = obter_sinonimos(palavra)
    print(f"Sinônimos de '{palavra}': {sinonimos}")
    
    for registro in dados:
        texto_completo = get_text_from_registro(registro)
        
        # Palavra
        if word_in_text(palavra, texto_completo):
            resultados.append(registro)
            continue
        
        # Sinonimos
        if any(word_in_text(sinonimo, texto_completo) for sinonimo in sinonimos):
            resultados.append(registro)
            continue
        
        # Similaridade
        sim_categoria = similaridade(palavra, registro['categoria'])
        sim_titulo = similaridade(palavra, registro['titulo'])
        sim_descricao = similaridade(palavra, registro['descricao'])
        if sim_categoria > 0.275 or sim_titulo > 0.4 or sim_descricao > 0.3:
            resultados.append(registro)
    
    return resultados

def exibir_resultados(resultados):
    if resultados:
        for registro in resultados:
            print(f"ID: {registro['id']}")
            print(f"Título: {registro['titulo']}")
            print(f"Descrição: {registro['descricao']}")
            print(f"Categoria: {registro['categoria']}")
            print(f"Local: {registro['local']}")
            print("-" * 40)
    else:
        print("Nenhum resultado encontrado.")

def main():
    dados = carregar_dados()
    
    while True:
        palavra = input("Digite uma palavra para buscar (ou 'sair' para encerrar): ").strip()
        if palavra.lower() == 'sair':
            print("Encerrando a busca.")
            break
        resultados = buscar_registros(palavra, dados)
        exibir_resultados(resultados)

if __name__ == "__main__":
    main()
