km = float (input("Qual a distância de sua viagem? \n"))

if km <= 200:
    print ("A sua passagem custará", km * 0.5, "reais.")
else:
    print ("A sua passagem custará", km * 0.45, "reais.")