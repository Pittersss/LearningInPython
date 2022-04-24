#Exercícios Estruturas de Decisão
#1)
#try:
 #numOne = float(input("Digite um número "))
 #numTwo = float(input("Digite outro número "))
 #if(numOne > numOne):
    #print("O número {} é o maior".format(numOne))
 #else:
    #print("O número {} é o maior".format(numTwo))
#except ValueError:
   #print("Digite apenas números!")

#2)
#try:
 #num = float(input("Digite um número: "))
 #if num > 0:
    #print("Ele é positivo")
 #else:
     #print("Ele é negativo")
#except ValueError:
    #print("Digite apenas números!")

#3)
#try:
 #sex = str(input("Qual é o seu sexo? F - Feminino ou M - Masculino ")).upper()
 #if(sex != "M" and sex != "F"):
    #print("Sexo inválido")
 #elif(sex == "M"):
    #print("Masculino")
 #elif(sex == "F"):
    #print("Feminino")
#except:
    #print("Digite apenas letras!")

#4)
#try:
 #char = str(input("Digite uma letra: ")).upper()
 #print(char[0])
 #if(char != "A" and  char != "E" and char != "I" and char != "O" and char != "U"):
    #print("Essa letra é uma consoante")
 #else:
    #print("É uma vogal")
#except ValueError:
    #print("Digite apenas caracteres")

#5)
#try:
 #nota1 = float(input("Digite a sua primeira nota: "))
 #nota2 = float(input("Digite a sua segunda nota: "))
 #media = (nota1 + nota2)/2

 #if(media >= 7 and media < 10):
    #print("Aprovado")
 #elif media == 10:
    #print("Aprovado com Distinção")
 #else:
    #print("Reprovado")
#except ValueError:
    #print("Digite apenas números!")

#6)
#try:
#try:
 #numOne = float(input("Digite um número "))
 #numTwo = float(input("Digite outro número "))
 #numThree = float(input("Digite mais um número "))
 #if(numOne > numTwo and numTwo > numThree):
   #  print("O número {} é o maior".format(numOne))
 #elif(numOne > numThree and numThree > numTwo):
  #   print("O número {} é o maior".format(numOne))
 #if(numTwo > numOne and numOne > numThree):
     #print("O número {} é o maior".format(numTwo))
# elif(numTwo > numThree and numThree > numOne):
   #  print("O número {} é o maior".format(numTwo))
 #if(numThree > numOne and numOne > numTwo):
   #  print("O número {} é o maior".format(numThree))
 #elif(numThree > numTwo and numTwo > numOne):
   #  print("O número {} é o maior".format(numThree))
#except ValueError:
  # print("Digite apenas números!")

#7)
#try:
 #numOne = float(input("Digite um número "))
 #numTwo = float(input("Digite outro número "))
 #numThree = float(input("Digite mais um número "))

 #if(numOne > numTwo and numTwo > numThree):
     #print("O número {} é o maior".format(numOne))
     #print("O menor número é o {}".format(numThree))
 #elif(numOne > numThree and numThree > numTwo):
     #print("O número {} é o maior".format(numOne))
     #print("O menor número é o {}".format(numTwo))
 #if(numTwo > numOne and numOne > numThree):
     #print("O número {} é o maior".format(numTwo))
    # print("O menor número é o {}".format(numThree))
 #elif(numTwo > numThree and numThree > numOne):
     #print("O número {} é o maior".format(numTwo))
    # print("O menor número é o {}".format(numOne))
 #if(numThree > numOne and numOne > numTwo):
    # print("O número {} é o maior".format(numThree))
     #print("O menor número é o {}".format(numTwo))
 #elif(numThree > numTwo and numTwo > numOne):
     #print("O número {} é o maior".format(numThree))
     #print("O menor número é o {}".format(numOne))
#except ValueError:
   #print("Digite apenas números!")

#8)
#produto1 = float(input("Digite o preço de um produto "))
#produto2 = float(input("Digite outro preço de um produto "))
#produto3 = float(input("Digite o preço de mais um produto "))

#if(produto1 < produto2 and produto1 < produto3):
    #print("Escolha o produto de: {}$".format(produto1))
#if(produto2 < produto1 and produto2 < produto3 and produto2):
    #print("Escolha o produto de: {}$".format(produto2))
#if(produto3 < produto2 and produto3 < produto1):
   #print("Escolha o produto de: {}$".format(produto3))

#9)
import math


numeros = []
numeros.append(float(input("Escreva um números ")))
numeros.append(float(input("Escreva um números ")))
numeros.append(float(input("Escreva um números ")))
#if(numeros[0] > numeros[1] and numeros[1] > numeros[2]):
    #print(numeros[0])
    #print(numeros[1])
    #print(numeros[2])
#if(numeros[0] > numeros[1] and numeros[2] > numeros[1]):
    #print(numeros[0])
    #print(numeros[2])
    #print(numeros[1])
#-----------------------------------------------------------------
if(numeros[1] > numeros[0] and numeros[0] > numeros[2]):
    print(numeros[1])
    print(numeros[0])  
    print(numeros[2])
if(numeros[1] > numeros[0] and numeros[2] > numeros[0]):
    print(numeros[1])
    print(numeros[2])
    print(numeros[0]) 
#-----------------------------------------------------------
#if(numeros[2] > numeros[0] and numeros[0] > numeros[1]):
    #print(numeros[2])
    #print(numeros[0]) 
    #print(numeros[1])
#if(numeros[2] > numeros[0] and numeros[1] > numeros[0]):
    #print(numeros[2])
    #print(numeros[1]) 
    #print(numeros[0])

