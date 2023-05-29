lg = float (input ("Informe a largura: "))
cm = float (input ("Informe o comprimento: "))

def area(largura, comprimento):
    total = largura * comprimento
    return total

print ("A área total é de", area (lg, cm), "metros quadrados." )