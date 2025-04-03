class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, item):
        self.itens.insert(0, item)
    
    def desempilhar(self):
        if not self.estavazia():
            return f"O elemento: {self.itens.pop(0)} foi desempilhado"
        return None
    
    def estavazia(self):
        return len(self.itens) == 0
    
    def topo(self):
        if not self.estavazia():
            return self.itens[0]
        return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
    

pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print(pilha.topo()) #3
pilha.empilhar(4)
pilha.empilhar(5)
print(pilha)
pilha.desempilhar()
print("O topo agora é: ")
print(pilha.topo()) #
        
        