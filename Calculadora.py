print("Primera calculadora")
print("Operaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = input("Elige la operacion (1/2/3/4): ")

numeros = input("Introduce los dos valores separados por espacio: ").split()

num1, num2 = float(numeros[0]), float(numeros[1])

if operacion == '1':
    resultado = num1 + num2
elif operacion == '2':
    resultado = num1 - num2
elif operacion == '3':
    resultado = num1 * num2
elif operacion == '4':
    if num2 == 0:
        print("Error: Divides por zero")
    else:
        resultado= num1 / num2
else:
    print("Operacion no valida")

# Redondeo optimizado
if 'resultado' in locals():
    if resultado % 1 == 0:
        print(f"El resultado es: {int(resultado)}")
    else:
        print(f"El resultado es: {round(resultado, 2)}")