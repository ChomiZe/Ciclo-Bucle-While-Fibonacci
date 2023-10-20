# Desarrollar un programa que imprima en pantalla la Sucesion de Fibonacci desde
#el numero 0 hasta 1597 de manera horizontal con espacios
#tener un maximo de 7 lineas de codigo

num_uno, num_dos = 0, 1
while num_dos<=1597:
    print(num_uno, num_dos, end=" ")
    num_uno= num_uno + num_dos
    num_dos= num_uno+ num_dos 
