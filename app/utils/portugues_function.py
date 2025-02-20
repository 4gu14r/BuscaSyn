import unicodedata
import re

from spellchecker import SpellChecker
from nltk.stem import RSLPStemmer

# Função para corrigir a ortografia em português
def corrigir_palavra(palavra):
    spell = SpellChecker(language='pt')
    palavra_corrigida = spell.correction(palavra)
    return palavra_corrigida if palavra_corrigida is not None and palavra_corrigida != palavra else palavra

# Função para processar a entrada do usuário, corrigindo palavras e juntando com '_'
def processar_entrada(entrada):
    if " " in entrada:
        tokens = entrada.split()
        tokens_corrigidos = [corrigir_palavra(token) for token in tokens]
        return "_".join(tokens_corrigidos)
    else:
        return corrigir_palavra(entrada)


# Função para obter texto completo do registro (todos os campos como texto)
def fazer_texto_completo(registro):
    return " ".join(str(valor) for valor in registro.values() if isinstance(valor, (str, int, float)))


# Função para normalizar a palavra (remover acentos, transformar em minúsculas e remover '_')
def formatar(palavra):
    palavra = unicodedata.normalize('NFD', palavra).encode('ascii', 'ignore').decode('utf-8')
    return palavra.replace('_', '').lower()


# Função para obter o radical da palavra
def obter_radical(palavra):
    stemmer = RSLPStemmer()
    return stemmer.stem(formatar(palavra))


# Função para verificar se a palavra aparece diretamente no texto
def verificar_palavra(word, text):
    return word in re.findall(r'\w+', text.lower())


# Função para verificar se o radical da palavra aparece em qualquer campo do registro
def verificar_contexto(radical, registro):
    campos = [str(valor) for valor in registro.values() if isinstance(valor, (str, int, float))]
    return any(obter_radical(palavra) == radical for campo in campos for palavra in campo.split())