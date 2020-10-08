class Aluno:
  def __init__(self, cod, nome, matricula):
    self.codigo = cod
    self.nome = nome
    self.matricula = matricula
    
  def print_me(self):
    print(self.__dict__)
      
class AlunoEnsMedio(Aluno):
  def __init__(self, cod, nome, matricula, ano):
    Aluno.__init__(self, cod, nome, matricula)
    self.ano = ano
    
class AlunoGraduacao(Aluno):
  def __init__(self, cod, nome, matricula, semestre):
    Aluno.__init__(self, cod, nome, matricula)
    self.semestre = semestre
      
aluno = Aluno(1, 'João', 123)
alunoEM = AlunoEnsMedio(1, 'João', 123, 3)
alunoG = AlunoGraduacao(1, 'João', 123, 6)

aluno.print_me()
alunoEM.print_me()
alunoG.print_me()