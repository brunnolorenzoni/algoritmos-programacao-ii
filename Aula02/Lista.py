from No import No

class Lista:
    def __init__(self):
        self.inico = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, valor):
        if(self.inico):
            aux = self.inico
            while(aux.proximo) :
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inico = No(valor)
        
        self.tamanho = self.tamanho + 1

    def inserir(self, posicao, valor):
        if(posicao == 0):
            no = No(valor)
            no.proximo = self.inico
            self.inico = no
        else:
            anterior = self.inico
            for i in range (posicao - 1):
                if(anterior):
                    anterior = anterior.proximo
            no = No(valor)
            no.proximo = anterior.proximo
            anterior.proximo = no
            
            self.tamanho = self.tamanho + 1
    
    def excluir(self, valor):
        if self.tamanho == 0:
            print('Lista vazia')
        elif self.tamanho == 1:               
            if self.inico.dado == valor:
                self.inico = None
                self.tamanho -= 1
            else:
                print('Valor não encontrado')
        else: 
            if(self.inico.dado == valor):
                self.inico = self.inico.proximo
            else:
                ant = self.inico
                aux = ant.proximo
                while(aux):
                    if(aux.dado == valor):
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                    ant = aux
                    aux = aux.proximo
                
    def imprimir(self):
        aux = self.inico
        print('Lista', '\n')
        while(aux):
            print(aux.dado, '\n')
            aux = aux.proximo

    def addAscOrder(self, value):
        if(self.tamanho > 0) :
            current = self.inico
            position = 0
            while(current):
                if(current.dado < value):
                    position += 1
                    if(current.proximo):
                        current = current.proximo
                    else:
                        break
                else:
                    break

            self.inserir(position, value)
                    
        else:
            self.adicionar(value)
