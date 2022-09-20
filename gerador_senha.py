import random
def maiusc():
    num = random.randrange(65,91)
    letra = chr(num)
    print(letra, end="")
    
def minusc():
    num = random.randrange(97,123)
    letra = chr(num)
    print(letra, end="")


for x in range(5):
    maiusc()
    minusc()
