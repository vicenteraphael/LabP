class ItemCardapio:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        
    def detalhes(self):
        return (f"Nome: {self.nome}\nDescrição: {self.descricao}\nPreco: {self.preco}")
    
class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def detalhes(self):
        return (f"Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.status = "Aberto"

    def adicionar(self, item_cardapio):
        self.itens.append(item_cardapio)

    def total(self):
        soma = 0
        for item in self.itens:
            soma += item.preco
        return (f"R$ {soma}")

    def resumo(self):
        print (f"-----------------\nRESUMO DO PEDIDO:\n\nCLIENTE:\n\n{self.cliente.detalhes()}\n\nPEDIDO:\n")
        for i, item in enumerate (self.itens):
            print(f"Pedido {i+1}:\n{item.detalhes()}\n")
        print (f"TOTAL: {self.total()}\n\nSTATUS: {self.status}\n------------------")

    def finalizar_pedido(self):
        self.status = "Finalizado"
        
cardapio = {
    "Hamburguer" : ItemCardapio("Hamburguer", "carne, cheddar, salada", 13.90),
    "Coca Cola" : ItemCardapio("Coca cola", "coca cola espumante", 100),
    "Batata Frita" : ItemCardapio("Batata Frita", "Batatas macias e crocantes", 30),
    "Coxinha" : ItemCardapio("Coxinha", "frango", 6),
    "Esfiha": ItemCardapio("Esfiha", "carne", 6),
    "Hamburguer de Siri" : ItemCardapio("Hamburguer de Siri", "carne, salada, siri, queijo", 99999999999999)
}

beto = Cliente("Roberto", "+55 (11) 98477-0597", "R. Erastótenes, 531")
pedido = Pedido(beto)

pedido.adicionar(cardapio["Hamburguer"])
pedido.adicionar(cardapio["Coca Cola"])
pedido.adicionar(cardapio["Batata Frita"])

pedido.resumo()
pedido.finalizar_pedido()
pedido.resumo()