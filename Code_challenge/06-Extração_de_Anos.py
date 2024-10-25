def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    lista_ano = []
    
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    for data in lista_datas:
        data = str(data)
        ano = data[:4]
        lista_ano.append(ano)
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(lista_ano)


entrada = input()

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)
print(saida)