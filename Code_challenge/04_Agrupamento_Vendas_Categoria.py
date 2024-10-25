class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = str(produto)
        self.quantidade = int(quantidade)
        self.valor = float(valor)

    def to_dict (self):
        return {"Produto": self.produto, "Quantidade": self.quantidade, "Valor": self.valor}

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self, venda):
        if isinstance (venda, Venda):
            vendas = self.vendas.append(venda.to_dict())
            return vendas


        else:
            print("Erro: objeto não é uma instância da classe Venda.")

    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def calcular_total_vendas(self, venda):
        total = float(0)
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
             # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total +=  venda["Valor"]   
            #Está errado, o certo seria multiplicar pelas quantidades
            

        return total
    
    def __str__(self):
        return f"{self.nome}"

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())
            produto = str(produto.strip())

            venda = Venda(produto , quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            vendas = categoria.adicionar_venda(venda)
            
    
        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # TODOS: Exibir o total de vendas usando o método total_vendas:

        total = categoria.calcular_total_vendas(venda)
        print(f"Vendas em {categoria}: {total}")

if __name__ == "__main__":
    main()  