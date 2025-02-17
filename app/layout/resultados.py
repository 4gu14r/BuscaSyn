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