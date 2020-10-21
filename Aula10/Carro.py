from Automovel import Automovel

class Carro(Automovel):
  def __init__(self, marca, qtdRodas, modelo, potenciaMotor, qtdPortas):
    Automovel.__init__(self, marca, qtdRodas, modelo, potenciaMotor)
    self.__qtdPortas = qtdPortas
  
  def imprimirInformacoes(self):
    print('Carro')
    print(self.__dict__)