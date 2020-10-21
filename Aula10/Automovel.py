from Veiculo import Veiculo

class Automovel(Veiculo):
  def __init__(self, marca, qtdRodas, modelo, potenciaMotor):
    Veiculo.__init__(self, marca, qtdRodas, modelo)
    self.__potenciaMotor = potenciaMotor
  
  def imprimirInformacoes(self):
    print('Automovel')
    print(self.__dict__)