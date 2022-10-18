#leitor_csv

#biblioteca para leitura de arquivo csv do excel
import csv

def gravar_csv():
    tabela = ( ('PRODUTO', 'UNIDADE', 'PREÇO UNITÁRIO', 'QUANTIDADE ESTOQUE', 'VALOR TOTAL'),
               ('Açucar', '2 kg', '3.59', '10', '35.90'),
               ('Biscoito', '200 g', '1.19', '10', '11.90'),
            
        )

    #cria arquivo para gravação
    saida = csv.writer(open('tabela.csv', 'w', newline=''))

    #escreve as tuplas no arquivo
    saida.writerows(tabela)


def ler_csv():
    arquivo = open('tabela.csv')
    tabela = csv.reader(arquivo)

    for linha in tabela:
        print (linha)


if (__name__ == '__main__'): #variável interna
    #gravar_csv()
    ler_csv()
