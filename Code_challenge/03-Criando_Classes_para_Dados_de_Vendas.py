class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = str(produto)
        self.quantidade = int(quantidade)
        self.valor = float(valor)

    def to_dict (self):
        return {"Produto": self.produto, "Quantidade": self.quantidade, "Valor": self.valor}

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance (venda, Venda):
            self.vendas.append(venda.to_dict())

        else:
            print("Erro: objeto não é uma instância da classe Venda.")
      
    def calcular_total_vendas(self, venda):
        total = float(0)
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
             # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda["Quantidade"] * venda["Valor"]
            
        return total
    
    def __str__ (self):
        return f"Total de Vendas: {self.calcular_total_vendas(Venda)}"


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)

    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    relatorio.calcular_total_vendas(venda)

    print(relatorio)
    


if __name__ == "__main__":
    main()