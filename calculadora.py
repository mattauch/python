
#Função ou método

def somar(n1, n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1, n2):
    return n1*n2

def dividir(n1, n2):
    return n1/n2

#print(somar(1,2))

while True:

    print("###### Calculadora 0.1 #######")
    print("1 = somar")
    print("2 = subtrair")
    print("3 = multiplicar")
    print("4 = dividir")
    print("5 = sair")

    escolha = int(input("Escolha a operação: "))

    if escolha >=1 and escolha <=4:
        v1 = float(input("Primeiro valor: "))
        v2 = float(input("Segundo valor: "))

    if escolha == 1:
        print(somar(v1,v2))

    elif escolha == 2:
        print(subtrair(v1,v2))

    elif escolha == 3:
        print(multiplicar(v1,v2))

    elif escolha == 4:
        if v2 == 0:
            print("Erro de divisão por zero")
        else:
            print(dividir(v1,v2))
    elif escolha == 5:
        print("Adeus")
        break  #interrompe o loop do while
        
    else:
        print("Operação incorreta")
        
