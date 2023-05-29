def verificar_var (num):
    if num % 2 == 0:
        return True
    else:
        return False
    
n = int (input("Digite um valor: "))
print (verificar_var(n))