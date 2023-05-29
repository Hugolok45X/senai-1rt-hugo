def somar(n1, n2):
    total = n1 + n2
    return total
def multiplicar(n1, n2):
    total = n1 * n2
    return total
def maior(n1, n2):
    num = n1, n2
    return max(num)
def menor(n1, n2):
    num = n1, n2
    return min(num)

print("somar", "multiplicar", "maior numero", "menor numero")
op = input ("Informe a operação: ")
n1 = int (input("Valor 1: "))
n2 = int (input("Valor 2: "))

if op == "somar":
    print (somar(n1, n2))
elif op == "multiplicar":
    print (multiplicar (n1, n2))
elif op == "maior numero":
    print (maior (n1,n2))
elif op == "menor numero":
    print (menor (n1, n2))