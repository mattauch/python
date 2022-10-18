#programação_funcional

#funções normais

def transformar(x, y):
    return x * y

def iguais(x, y):
    #operador ternário
    return "Sim" if x == y else "Não"

    if x == y:
        return "Sim"
    else:
        return "Não"

#funções anônimas
multiplicar = lambda x, y: x * y

iguais2 = lambda x, y: "Sim" if x == y else "Não"



if __name__ == '__main__':
    print(transformar(2,3))

    print(multiplicar(2,3))

    print(iguais(2,3))

    print(iguais2("Sim","Sim"))
