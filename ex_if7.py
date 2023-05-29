pontos = float (input("Digite a sua pontuação: "))
 
if pontos <= 50:
    print ("Você receberá um Certificado de Participação")
elif pontos <= 60:
    print ("Você receberá um Certificado de Menção Honrosa")
elif pontos <= 70:
    print ("Medalha de Bronze")
elif pontos <= 90:
    print ("Medalha de Prata")
else:
    print ("Medalha de Ouro")