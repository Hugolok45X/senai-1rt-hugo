from time import sleep

def contagem_regressiva (num):
    for num in range (num, 0, -1):
        print (num)
        sleep (1)

nr = int (input("Digite a contagem regressiva: "))
contagem_regressiva (nr)
