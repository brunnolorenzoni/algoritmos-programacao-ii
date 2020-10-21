from Automovel import Automovel

class Moto(Automovel):
  def __init__(self, marca, qtdRodas, modelo, potenciaMotor, partidaEletrica):
    Automovel.__init__(self, marca, qtdRodas, modelo, potenciaMotor)
    self.__partidaEletrica = partidaEletrica
  
  def imprimirInformacoes(self):
    print('Moto')
    print(self.__dict__)