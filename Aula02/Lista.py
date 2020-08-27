from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, valor):
        if(self.inicio):
            aux = self.inicio
            while(aux.proximo) :
                aux = aux.proximo
            aux.proximo = No(valor)
        else:
            self.inicio = No(valor)
        
        self.tamanho = self.tamanho + 1

    def inserir(self, posicao, valor):
        if(posicao == 0):
            no = No(valor)
            no.proximo = self.inicio
            self.inicio = no
        else:
            anterior = self.inicio
            for i in range (posicao - 1):
                if(anterior):
                    anterior = anterior.proximo
            no = No(valor)
            no.proximo = anterior.proximo
            anterior.proximo = no
            
            self.tamanho = self.tamanho + 1
    
    def excluir(self, valor):
        temp = self.inicio 
        prev = None
        counterDelete = 0

        if(self.tamanho == 0):
            return print('Lista vazia')
    
        while (temp != None and temp.dado == valor): 
            self.inicio = temp.proximo
            temp = self.inicio
            counterDelete += 1
        
        while (temp != None): 
            while (temp != None and temp.dado != valor): 
                prev = temp 
                temp = temp.proximo
            
            if (temp == None): 
                return self.inicio
    
            prev.proximo = temp.proximo
            temp = prev.proximo
            counterDelete += 1

        if(counterDelete == 0):
            return print('Valor não encontrado')
        else:
            self.tamanho -= counterDelete
            return print('Valor deletado')
        
                
    def imprimir(self):
        aux = self.inicio
        print('Lista', '\n')
        while(aux):
            print(aux.dado, '\n')
            aux = aux.proximo

    def addAscOrder(self, value):
        if(self.tamanho > 0) :
            current = self.inicio
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
