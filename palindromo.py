#Esta versión ya incluye el último merge
c='c'
while (c != 's'):
    print("Palindromo")
    palabra=input("Ingresa una palabra: ")
    palabra=palabra.replace(" ","")
    y=palabra.isalpha()
    if y:
        palabra=palabra.lower()
        reversa=palabra[::-1]
        if palabra==reversa:
            print("Positivo")
        else:
            print("Negativo")
    c=input("¿Deseas salir?, presiona la letra s: ")
