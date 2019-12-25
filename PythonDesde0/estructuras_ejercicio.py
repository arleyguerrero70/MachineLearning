"""
70% Helado
20% Pastel
10% Flan
"""

stock = input("ingrese el postre")

if stock == "helado":
    print("Comprar cucharas, platos, hielo.")
elif stock == "pastel":
    print("Elegir entre sanor de chocolate o vainilla")
elif stock == "flan":
    print("Que buena elección") 
else:
    print("Solo tenemos, *helado *pastel *flan")      