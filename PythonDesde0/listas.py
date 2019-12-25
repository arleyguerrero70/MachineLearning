sabores = ["chocolate","crema americana","vainilla"]
sabores2 = ["lima","crema colombiana","arequipe"]

# Estoy agregando la info de sabores2 a sabores
sabores.extend(sabores2)
print(sabores)

#Estoy eliminando un string una lista
sabores2.remove("crema colombiana")
print(sabores)

"""
# En este caso estoy indicando con el append
# que lo que haya entre parentesis ocupara el ultimo lugar
sabores.append("Este es el último valor")
print(sabores[3])
print(sabores)
"""

"""
# La funcion insert me esta insertando
# La nuea fraccion en donde yo le indique
sabores.insert(0,"objeto insertado")
print(sabores[0])
print(sabores)
"""