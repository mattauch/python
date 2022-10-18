#objetivo: converter uma lista de strings para inteiros

lista = ['2', '4', '6','8']
nova_lista = []

#1. Usando o loop for
for x in lista:
    nova_lista.append(int(x))
print('Ciclo do for: ', nova_lista)
    #print(int(x) + 1)

#2. Usando compreensão de lista (lista comprehention)

retorno = [int (x) for x in lista]
print('List comprehention: ', retorno)

#3. Usando map com função nomeada
def conv (x):
    return int(x)

nova_lista = list(map(conv, lista))
print('Usando função nomeada: ',nova_lista)

#4. Usando map com função anônima (lambda)
nova_lista = list(map(lambda x: int(x), lista))
print('Usando lambda: ', nova_lista)

#5. Outro exemplo com lambda
lista2 = ['1.0', '3.1', '5.5', '7.7', '8.2']
nova_lista = list(map(lambda x,y: [int(x), float(y)], lista, lista2))
print('Exemplo 2 lambda: ', nova_lista)

#6. Outro exemplo com lambda
numeros = (1,2,3)
resultado = list(map(lambda a: a+a, numeros))
print('Exemplo 3 lambda: ', resultado)

#7. soma numeros com numeros2
numeros2 = [4,5,6]
resultado = list(map(lambda a,b : a+ b, numeros, numeros2))
print('Exemplo 4 lambda: ', resultado)


