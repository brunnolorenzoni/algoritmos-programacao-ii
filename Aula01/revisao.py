def imprimirPi():
    print('Valor do Pi:', '3.14' )
imprimirPi()

def getSalario():
    return 1045.0
print(getSalario())

def calcular_imprimir_area(l, c):
    area = float(l) * float(c)
    print(area)
calcular_imprimir_area(2, 3)

def calcular_area(l, c):
    area = float(l) * float(c)
    return area
print(calcular_area(2 , 3))

altura = 5
volume = altura * calcular_area(4, 6)
print(volume)

def calcular_volume (l, c, a):
    volume = float(l) * float(c) * float(a)
    return volume

def calcular_volume2 (l, c, a):
    volume = calcular_area(l, c) * float(a)
    return volume
