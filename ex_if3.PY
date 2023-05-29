salario = float (input("DIgite o valor do seu salário: "))

if salario <= 8250:
    print("O seu novo salário é", salario + (salario * 0.10))
else:
    print("O seu novo salario é", salario + (salario * 0.15))