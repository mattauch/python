qlinhas = int(input('Digite a quantidade de linhas: '))
qcolunas = int(input('Digite a quantidade de colunas: '))

linha = [7] * qcolunas
matriz = [linha] * qlinhas

soma= 0
for lin in matriz:
    soma += sum(lin)
print(soma)
