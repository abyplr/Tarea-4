#Variables globales
a = 0
b = 0
c = 0
#Se define la función "heron"
def heron():
    #variables locales
    a = int(input("Ingrese la longitud del lado 'a': "))
    b = int(input("Ingrese la longitud del lado 'b': "))
    c = int(input("Ingrese la longitud del lado 'c': "))
    #Se realiza el ciclo por si hay valores negativos o valores positivos que no cumplan la deigualdad del triángulo
    while (a<=0 or b<=0 or c<=0) or ((a>0 and b>0 and c>0) and not (a + b > c and b + c > a and a + c> b)):
        if a<=0 or b<=0 or c<=0: #Caso donde hay valores negativos
            print("Has ingresado un valor negativo")
            a=int(input("Ingrese nuevamente la longitud del lado 'a': "))
            b=int(input("Ingrese nuevamente la longitud del lado 'b': "))
            c=int(input("Ingrese nuevamente la longitud del lado 'c': "))
        elif (a>0 and b>0 and c>0) and not (a + b > c and b + c > a and a + c> b): #Caso donde son positivos y no cumplen la desiguadad
            print("Valores incorrectos, no forman un triángulo. Ingrese nuevos valores")
            a=int(input("Ingrese nuevamente la longitud del lado 'a': "))
            b=int(input("Ingrese nuevamente la longitud del lado 'b': "))
            c=int(input("Ingrese nuevamente la longitud del lado 'c': "))
        else: #Caso donde son valores positivos que cumplen la desigualdad
            break
    s = (a + b + c)/2 #Se calcula el semiperímetro
    A = (s * (s - a) * (s - b) * (s - c)) ** (1/2) #Se calcula el área
    print("El área del triángulo determinada por la fórmula de Herón es: ", A)
heron() #Se llama a la función
