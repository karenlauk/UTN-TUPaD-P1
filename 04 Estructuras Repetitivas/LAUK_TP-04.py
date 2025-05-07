#Trabajo práctico N°4 - Estructuras repetitivas
#Ejercicios:
#1)
#num = 0;
#for num in range(101):
#    print(num);

#2)
#num = input("Ingresa un número entero: ");
#dig = len(num.strip("-"));

#3)
#num1 = int(input("Ingresa el primer número: "));
#num2 = int(input("Ingresa el segundo número: "));
#if num1 > num2:
#    num1, num2 = num2, num1;
#suma = 0;
#for i in range(num1 + 1, num2):
#    suma += i;
#print("La suma de los números entre", num1, "y", num2, "es:", suma);

#4)
#total = 0;
#while True:
#    num = int(input("Ingresa un número entero (0 para terminar): "));
#    if num == 0:
#        break;
#    total += num;
#print("La suma total es:", total);

#5)
#import random
#secreto = random.randint(0, 9);
#intentos = 0;
#while True:
#    intento = int(input("Adivina el número (entre 0 y 9): "));
#    intentos += 1;
#    if intento == secreto:
#        print("¡Correcto! Lo lograste en", intentos, "intento(s).");
#        break;
#    else:
#        print("Incorrecto. Intenta de nuevo.");

#6)
#for i in range(100, -1, -2):
#    print(i);

#7)
#num = int(input("Ingresa un número entero positivo: "));
#suma = 0;
#for i in range(num + 1):
#    suma += i;
#print("La suma desde 0 hasta", num, "es:", suma);

#8)
#cant = 5;  
#par = impar = positivos = negativos = 0;
#for _ in range(cant):
#    num = int(input("Ingresa un número entero: "));
#    if num % 2 == 0:
#        par += 1;
#    else:
#        impar += 1;
#    if num > 0:
#        positivos += 1;
#    elif num < 0:
#        negativos += 1;
#print("cant de números par:", par);
#print("cant de números impar:", impar);
#print("cant de números positivos:", positivos);
#print("cant de números negativos:", negativos);

#9)
#cant = 100;
#suma = 0;
#for _ in range(cant):
#    num = int(input("Ingresa un número entero: "));
#    suma += num;
#media = suma / cant;
#print("La media de los", cant, "números es:", media);

#10)
num = input("Ingresa un número entero: ");
if num.startswith('-'):
    invertido = '-' + num[:0:-1];
else:
    invertido = num[::-1];
print("Número invertido:", invertido);

