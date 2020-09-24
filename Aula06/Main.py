# Construa um algoritmo que possua uma tupla com os números
# escritos por extenso de “zero” a “nove”. Peça ao usuário para digitar
# um nome de 0 a 9 e retorne a ele o número por extenso, sem usar
# estruturas condicionais (if e switch).

tupleNumebersFullText = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

index = int(input("Digite um número entre 0 e 9:"))
while True:
  if 0 <= index <= 9:
    print(tupleNumebersFullText[index])
    break
  else:
    index = int(input("Fora do range, digite um número entre 0 e 9:"))

# Construa um algoritmo que peça ao usuário para informar o nome, a
# nota01 e a nota02 de um aluno. Guarde estas informações em um
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02)/2] 
# e adicione ao dicionário. Ao final, imprima todos os dados do
# dicionário.

student_dict = {
  "nome": input("Digite seu nome: "),
  "nota_1": float(input("Digite a nota 1: ")),
  "nota_2": float(input("Digite a nota 2: "))
}

student_dict['media'] = ((student_dict["nota_1"] + student_dict["nota_2"]) / 2)

print('\n ----------- DICIONÁRIO  ----------')
for x, y in student_dict.items():
  print(x + ':', y)