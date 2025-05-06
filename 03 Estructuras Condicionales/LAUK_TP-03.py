#Trabajo práctico 3 - Estructura condicional
#Ejercicios:
#1) Mayor de edad:
#edad = int(input("Ingrese su edad: "));
#if edad >= 18:
#    print("Eres mayor de edad.");
#else:
#    print("Eres menor de edad.");

#2) Notas:
#nota = int(input("Ingresa su nota: "));
#if nota >= 6:
#    print("Aprobado");
#else:
#    print("Desaprobado");

#3) Números pares
#n = int(input("Ingrese un número par: "));
#if n % 2 == 0:
#    print("Ha ingresado un número par.");
#else:
#    print("Por favor, ingrese un número par");

#4) Categoria de edad
#edad = int(input("Ingresa su edad: "));
#if edad >= 12 and edad < 18:
#    print("Eres un adolescente.")
#elif edad < 12:
#    print("Eres un niño/a.");
#elif edad >= 18 and edad < 30:
#    print("Eres un adulto/a joven.");
#elif edad >= 30:
#    print("Eres un adulto/a.");

#5) Contraseña
#contra = input("Ingrese una contraseña entre 8 y 14 caracteres: ");
#if 8 <= len(contra) <= 14:
#    print("Ha ingresado una contraseña correcta.")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) Listas
#import random
#from statistics import mean, median, mode
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#moda = mode(numeros_aleatorios)
#print("Números aleatorios:", numeros_aleatorios)
#print(f"Media: {media}")
#print(f"Mediana: {mediana}")
#print(f"Moda: {moda}")
#if media > mediana > moda:
#    print("Distribución con sesgo positivo (a la derecha).")
#elif media < mediana < moda:
#    print("Distribución con sesgo negativo (a la izquierda).")
#elif media == mediana == moda:
#    print("Distribución sin sesgo.")
#else:
#    print("La distribución no cumple estrictamente con ninguno de los tres sesgos descritos.")

#7) Frase/palabra con terminación vocal
#frase = input("Ingrese una frase o palabra: ");
#if frase[-1].lower() in "aeiou":
#    frase += "!";
#print("Resultado:", frase);

#8) Nombre y opción 1,2,3:
#nombre=str(input("Ingrese un nombre: "));
#print("Seleccione una opción: ");
#print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.");
#print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro");
#print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.");
#opcion = input("Ingrese la opción elegida (1,2,3): ");
#if opcion == "1":
#    print("Resultado:", nombre.upper())
#elif opcion == "2":
#    print("Resultado:", nombre.lower())
#elif opcion == "3":
#    print("Resultado:", nombre.title())
#else:
#    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#9) Magnitud de terremoto
#magnitud = int(input("Ingrese la magnitud de un terremoto: "));
#if magnitud < 3:
#    print("Muy leve.");
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve");
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado.");
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte.");
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy fuerte")
#elif magnitud >= 8:
#    print("Extremo.")

#10) Estaciones del año
hemisferio = input("Ingrese en qué hemisferio se encuentra (n/s): ").strip().upper()
mes = int(input("Ingrese el mes qué estás (1-12): "));
dia = int(input("Ingrese el día actual (1-31): "));
if hemisferio not in ("N", "S"):
    print("Hemisferio no válido. Debe ingresar 'N' o 'S'.")
else:
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        print("Fecha inválida.")
        exit()
    if hemisferio == "N":
            print(f"En el hemisferio norte es {estacion_norte}.")
    else:
        print(f"En el hemisferio sur es {estacion_sur}.")





