
import os

list_shop = [] 

def encerrarApp():
  print('App Encerrado')
  exit()

def loadList():
  try:  
    file = open("list_shop.txt", "r")
    content = file.read()
    
    data = None
    if(len(content) == 0):
      data = []
    else:
      data = content.split(',')
      
    file.close()
    return data
    
  except Exception as error:
    print(error.args[1])
    return []
  
def removerItem():
  global list_shop
    
  imprimirLista()
  
  if(len(list_shop) == 0):
    return False
  
  index = int(input('Qual item você quer remover?'))
  while(True):
    if 0 <= index < len(list_shop):
      del list_shop[index]
      gravaItem(list_shop)
      os.system('clear')
      break
    else:
      index = int(input("Selecione uma opção válida: "))
  
def imprimirLista():
  list_shop = loadList()
  print("\n ----- MINHA LISTA ----- \n")
  if(len(list_shop) == 0):
    print('Lista vazia')
  else:
    for i in range(len(list_shop)):
      print('{} - {}'.format(i, list_shop[i]))
    
  print("\n ----------------------- \n")

def gravaItem(list_shop):
  
  separator = ','
  data = separator.join(list_shop).strip()
       
  try:  
    file = open("list_shop.txt", "w")
    file.write(data.strip())
    file.close()
  except Exception as error:
    print(error.args[1])
    

def adicionarItem(item): 
  list_shop.append(item.strip())
  gravaItem(list_shop)
  
def menu():
 
  print('--------------- MENU ---------------')
  print('[1] - Add Item')
  print('[2] - Remove Item')
  print('[3] - Print List')
  print('[0] - Exit')
  print('\n')
  index = int(input('Selecione uma opção: '))
  
  while (True):
    if 0 <= index <= 3:
      if(index == 0):
        encerrarApp()
      elif(index == 1):
        adicionarItem(input("Item: "))
      elif(index == 2):
        removerItem()
      else:
        imprimirLista()
        
      init()
      
    else:
      index = int(input("Selecione uma opção válida: "))


def init():
  global list_shop
  list_shop = loadList()
  menu()

os.system('clear')
init()
