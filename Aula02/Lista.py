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
        currentNode = self.inico 
        prevNode = None
        
        if(self.tamanho == 0):
            return print('Lista Vazia')
        elif self.tamanho == 1:               
            if self.inico.dado == valor:
                self.inico = None
                self.tamanho -= 1
            else:
                print('Valor não encontrado')
        else: 
            while(currentNode):
                if(currentNode.dado == valor):
                    if(prevNode):
                        prevNode.proximo = currentNode.proximo
                        self.tamanho -= 1
                    else:
                        self.inico = currentNode.proximo
                        self.tamanho -= 1
                prevNode = currentNode
                currentNode = currentNode.proximo

        
                
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
