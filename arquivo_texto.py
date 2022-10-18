import sys

#Podemos abrir um arquivo nos seguintes modos:
#'r' = read = somente para leitura
#'w' = write = somente para gravação, mas apaga o conteúdo existente
#'a'= append = gravação, mas não apaga o conteúdo existente

#Tipo de arquivo:
#texto ou binário ('b')

#Função para gravar
def gravar():
    frutas = ['banana', 'morango', 'kiwi']
    #abre o arquivo para escrita
    arquivo = open('frutas.txt', 'w')

    #gravando o arquivo
    for f in frutas:
        arquivo.write(f + '\n')

    #fecha o arquivo
    arquivo.close()

#Função para ler
def ler():
    #abre o arquivo
    arquivo = open('frutas.txt','r')
    #lê cada linha do arquivo
    for linha in arquivo:
        print(linha, end='')
    #fecha o arquivo
    arquivo.close()


#Função para anexar
def anexar():
    arquivo = open('frutas.txt', 'a')
    arquivo.write('manga\n')
    arquivo.write('mamão\n')
    
    arquivo.close()


def ler_csv():
    arquivo = open('california_housing_train.csv') #modo'r'

    i = 0 # i = linha
    total = 0
    for linha in arquivo:
        if (i==0):
            total_col = len(linha.split(','))
        else: 
            valor = linha.split(',')[total_col-1]
            total += float(valor)
        i += 1
        
    print('Total de linhas: ', i)
    print('Valor total:', total)
    print('Valor Médio:R$ %.2f '% (total / i))   
    arquivo.close()



#Função Principal
if (__name__ == '__main__'):
    #gravar()
    ler_csv()
    #anexar()
