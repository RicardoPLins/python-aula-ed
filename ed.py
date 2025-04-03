class Node:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

class ListaSimplesmenteEncadeada:
  def __init__(self):
    self.cabeca = None
  def inserir(self, valor):
    novo_no = Node(valor)
    if not self.cabeca:
      self.cabeca= novo_no
    else:
      no_atual = self.cabeca
      while no_atual.proximo: # 1 2 3 4 5 6
        no_atual = no_atual.proximo
      no_atual.proximo = novo_no

  def percorrer(self):
    valores = []
    no_atual = self.cabeca
    while no_atual:
      valores.append(no_atual.valor)
      no_atual = no_atual.proximo
    return valores
  


lista = ListaSimplesmenteEncadeada()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
print("Percorrendo a lista..", lista.percorrer())