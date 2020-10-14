class Pessoa:
  def __init__(self, cod, nome, endereco, telefone):
    self.__codigo = cod
    self.nome = nome
    self._endereco = endereco
    self.__telefone = telefone
    
  def imprimeNome(self):
    print(self.nome)
    
  def __imprimeTelefone(self):
    print(self.__telefone)

class Fisica(Pessoa):
  def __init__(self, cod, nome, endereco, telefone, cpf, idade, peso, altura):
    Pessoa.__init__(self, cod, nome, endereco, telefone)
    self.__cpf = cpf
    self.idade = idade
    self.peso = float(peso)
    self.altura = float(altura)
    
  def imprimeCPF(self):
    print(self.__cpf)
    
  def __calculaIMC(self):
    return float(self.peso / pow(self.altura, 2))
  
  def getIMC(self):
    return(self.__calculaIMC())
      
class Juridica(Pessoa):
  def __init__(self, cod, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
    Pessoa.__init__(self, cod, nome, endereco, telefone)
    self.__cnpj = cnpj
    self.__inscricaoEstadual = inscricaoEstadual
    self.quantidadeFuncionarios = quantidadeFuncionarios
    
  def imprimeCNPJ(self):
    print(self.__cnpj)
    
  def __emitirNotaFiscal(self):
    print(self.__inscricaoEstadual)
    
  def getNotaFiscal(self):
    return (self.__emitirNotaFiscal())

p = Pessoa(1, 'João', 'Rua X', 555)
pf = Fisica(1, 'João', 'Rua X', '+55 51 9 9999-9999', 11111111111, 18, 90.1, 1.70)
pj = Juridica(1, 'João', 'Rua X', '+55 51 9 9999-9999', 00000000000000, 12345, 10)

print(pf.getIMC())
pj.imprimeCNPJ()