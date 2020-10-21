from Veiculo import Veiculo

class Bicicleta(Veiculo):
  def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
    Veiculo.__init__(self, marca, qtdRodas, modelo)
    self.__numMarchas = numMarchas
    self.__bagageiro = bagageiro
    
  def imprimirInformacoes(self):
    print('Bicicleta')
    print(self.__dict__)
    