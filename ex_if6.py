km = float (input ("Qual foi a velocidade do carro: "))

if km > 80:
    print ("VOCÊ FOI MULTADO! \n" "VOCÊ TEM 24 HORAS PARA PAGAR A MULTA \n" "A multa é de", (km - 80) * 7)
else:
    print ("Você está na velocidade padrão! \n" "PARABÉNS!!!")