import json

from utils.similaridade import similaridade
from utils.portugues_function import (
    verificar_contexto,
    formatar,
    verificar_palavra,
    obter_radical,
    fazer_texto_completo
)

def buscar_registros(palavra, dados):
    resultados = []
    registros_encontrados = set()

    palavra_formatada = formatar(palavra)
    radical = obter_radical(palavra_formatada)

    for registro in dados['data']:

        # Cria uma chave única baseada no conteúdo completo do registro
        chave_unica = json.dumps(registro, sort_keys=True)

        texto_completo = fazer_texto_completo(registro)

        # Verifica se a palavra aparece diretamente no texto completo
        if verificar_palavra(palavra_formatada, texto_completo) and registro['id'] not in registros_encontrados:
            resultados.append(registro)
            registros_encontrados.add(chave_unica)
            continue

        # Calcula a similaridade total com todos os campos de texto do registro
        similaridade_total = sum(
            similaridade(palavra_formatada, str(valor))
            for valor in registro.values()
            if isinstance(valor, (str, int, float))
        )

        # Verifica o contexto com base no radical em todos os campos
        if similaridade_total > 0.5 and verificar_contexto(radical, registro) and registro['id'] not in registros_encontrados:
            resultados.append(registro)
            registros_encontrados.add(chave_unica)

    return resultados