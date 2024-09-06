numero1= float(input("Ingresar un numero: "))
operador=input("Elige un operador (+ , -, *, /): ")
numero2= float(input("Ingrese un numero: "))

if operador == "+":
    resultado = numero1+numero2
    print("Resultado: ", resultado)
elif operador == "-":
    resultado= numero1-numero2
    print("Resultado",resultado)
elif operador == "*":
    resultado= numero1*numero2
    print("Resultado:",resultado)
elif operador == "/":
    if numero2 != 0:
     resultado= numero1/numero2
     print("Resultado:", resultado)
    else: 
     print("Error: no se puede dividir entre cero")
else:
   print("Operador no valido")


