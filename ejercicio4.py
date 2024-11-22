#################################################################################
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
#################################################################################

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num2 == 0:
    print("Error: No se puede dividir por cero.")

else:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es {division:.2f}")
    
    