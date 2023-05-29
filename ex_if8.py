valor1 = float (input ("Digite o primeiro valor: "))
valor2 = float (input ("Digite o segundo valor: "))
op = "Adição", "Subtração", "Multiplicação", "Divisão"
op = input ("Escolha a operação desejada: \n" "Adição", "Subtração", "Multiplicação", "Divisão")

if op == "Adição":
    print ("O resultado é", valor1 + valor2)
elif op == "Subtração":
    print ("O resultado é", valor1 - valor2)
elif op == "Multiplicação":
    print ("O resultado é", valor1 * valor2)
elif op == "Divisão":
    if valor2 == 0:
        print ("Não é possível dividir por 0")
    else:
        print ("O resultado é", valor1 / valor2)