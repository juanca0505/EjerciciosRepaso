cadena = str(input("Ingrese una frase palindroma :"))
if cadena == ''.join(reversed(cadena)):
    print("es palindroma")
else:
    print("No es palindroma")