name_products = ['Mouse', 'Teclado', 'Mousepad']
price_products = [469.99, 998.00, 120.99]
amount_products = [11, 33, 20]

def index_exists(id, list): 
    return True if id >= 0 and id < len(list) else False

def showProduct (id):
    if(index_exists(id, name_products) and index_exists(id, price_products) and index_exists(id, amount_products)):
        print('Nome: %s; Valor: %.2f; Quantidade: %s' % (name_products[id], price_products[id], amount_products[id]))
    else:
        print('Item não encontrado')

def removeProduct(id):
    if(index_exists(id, name_products) and index_exists(id, price_products) and index_exists(id, amount_products)):
        del name_products[id]
        del price_products[id]
        del amount_products[id]
        print('Produto %s removido' % (id))
    else: 
        print('Item não encontrado')

showProduct(1)
showProduct(4)
showProduct(-4)
showProduct(0)

print(name_products)
removeProduct(1)
removeProduct(-4)
print(name_products)

