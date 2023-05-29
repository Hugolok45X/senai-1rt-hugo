nota1 = float (input ("Insira a primeira nota: "))
nota2 = float (input ("Insira a segunda nota: "))
nota3 = float (input ("Insira a terceira nota: "))

ntfinal = ((nota1 + nota2 + nota3) /3)

if  ntfinal >= 7:
    print ("Você foi aprovado!")
else:
    if ntfinal > 5:
        print ("Você está de recuperação!")
    else:
        print ("Você foi reprovado!")



print (f"Sua media foi {ntfinal:.2f}")