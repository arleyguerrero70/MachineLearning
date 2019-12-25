"""
def calcula (mensaje):
    calculo = 43 * 12 * 80
    calculo = calculo / 7 
    coeficiente = 45 * 3.1416
    calculo = calculo * coeficiente
    calculo = mensaje + str(calculo)
    print(calculo)

calcula("Impresion 1 -->")
calcula("Impresion 2 -->")
calcula("Impresion 3 -->")
"""
#funcion recibe parametros
def calcula_valor1(mensaje1, num1, num2):
    total = num1 + num2
    print(mensaje1 + str(total))

#funcion que recibe y devuelve parámetros
def calcula_valor(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

suma = calcula_valor(10,55)   
print(suma*2)
