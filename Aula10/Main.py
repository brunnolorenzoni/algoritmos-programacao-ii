from Veiculo import Veiculo
from Automovel import Automovel
from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta


moto = Moto('Harley Davidson', 2, 'Fat Boy', 94, True)
carro = Carro('Chevrolet', 4, 'Astra', 112, 2)
bicicleta = Bicicleta('Caloi', 2, 'Ceci', 7, False)

moto.imprimirInformacoes()
#carro.imprimirInformacoes()
#bicicleta.imprimirInformacoes()

moto.acelerar(110)

moto.imprimirInformacoes()