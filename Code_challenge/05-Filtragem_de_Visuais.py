def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    visuais_final = []
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    for visual in visuais:
        visual = visual.title()
        visuais_final.append(visual)
    
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = list(set(visuais_final))
    lista_final = sorted(lista_final)
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)