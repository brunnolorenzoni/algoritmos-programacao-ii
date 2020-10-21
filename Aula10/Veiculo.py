class Veiculo:
  def __init__(self, marca, qtdRodas, modelo):
    self.__marca = marca
    self.__qtdRodas = qtdRodas
    self.__modelo = modelo
    self.__velocidade = 0
    
  def imprimirInformacoes(self):
    print(self.__dict__)
  
  def acelerar(self, valor):
    if valor > 0:
      self.__velocidade += valor
  
  def frear(self, valor):
    if valor > 0:
      self.__velocidade -= valor
      if self.__velocidade < 0:
        self.__velocidade = 0