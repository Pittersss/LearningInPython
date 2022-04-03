#Como declarar várias variáveis juntas
# ---> name, age, atractive = "Pedro", 18, True
#print("Hellou " + name + ", your age is " + str(age) + ". I can see your kindness is realy " + str(atractive))

#Variáveis com o mesmo valor
#num1 = num2 = num3 = 30

#Como converter para string
#str(variavel)
#*Print não aceita nada sem ser string

#Como pegar o tamanho de uma string(length)
#len(string)
#Contagem igual ao c#, começa no 0,1,2,3...
#nome = "pedroca"
#Pega o index de uma determinada letra
#print(nome.find("p"))
#Result: 0
#Coloca a primeira letra como maiúscula
#print(nome.capitalize())
#Coloca tudo em maiúsculo
#print(nome.upper())


from ast import Break
from datetime import datetime
from mailbox import NotEmptyError
import math

#print(math.ceil(age)) Entrega um número acima desse
#print(abs(age)) Valor absoluto, não aceita negativo
#print(pow(age,2)) Eleva um número ao segundo argumento
#print(math.sqrt(age)) calcula a raiz quadrada de um número

#MANIPULAÇÃO DE STRINGS
#Pegando parte de uma string
#String[start:stop:step]
#String é um array de caracteres, contagem começa do zero
nome = "Pedro Henrique Malaquias da Silva"

#Sobrenome = nome[15:36]
#Firt_name = nome[5::-1]
# MESMA COISA QUE: Firt_name = nome[:6]
#Firt_name = nome[0:6:2]
#Esse step significa pular letra
#Escrever string ao contrário Firt_name = nome[5::-1]
#output = Pdo
#Como cortar uma string?
#Método slice(IndexPositivo, IndexNegativo)
#O index negativo faz a contagem inversa para cortar e o positivo o contrário
#pedaço = slice(0, -28)
#first_name = nome[pedaço]
#idade = int(input("Qual é a sua idade? "))

#if idade > 30:
    #print("Você é velho")
#elif idade >= 18 and idade <= 30:
    #print("Você é um adulto")
#elif idade > 12 and idade < 18:
    #print("Você é um adolecente")
    #elif ----> Mesma coisa que um else if(se caso... tal coisa acontecer)

#Programa para separar o seu primeiro nome, o último e o do meio
#yourName = str(input("Qual é o seu nome? "))
#caracterIndex = len(yourName) - 1
#FirstIndexMidname = 0
#SecoundIndexMidname = 0
#firstname = ""
#last_name = ""

#for i in range(caracterIndex):
    #if yourName[i] !=  " ":
        #firstname += yourName[i]
    #else:
        #FirstIndexMidname +=  i
        #print(FirstIndexMidname)
        #break
#while caracterIndex > 0:
    #if yourName[caracterIndex] != " ":
        #last_name += yourName[caracterIndex]
    #else:
        #SecoundIndexMidname += caracterIndex
        #print(SecoundIndexMidname)
        #break
    #caracterIndex -= 1 

#midName = slice(FirstIndexMidname, SecoundIndexMidname)
#print("Seu primeiro nome é: " + firstname + " e seu último nome é: " + last_name[::-1] + " e seu(s) nome(s) do meio é(são): " + yourName[midName])
#altura = int(input("Fale a altura da figura "))
#comprimento = int(input("Fale o comprimento da figura "))
#simbolo = input("Escolha um simbolo para representar a figura")

#for i in range(comprimento):
    #for j in range(altura):
        #print(simbolo, end="")
    #print() #Isso faz pular a linha


haveGoals = int(input("Você tem algum objetivo que queira listar? 1.Sim 2.Não "))
mygoals = []
checkMoreGoals = 1
while checkMoreGoals == 1:
 if haveGoals == 1:
    othergoal = input("Quais são seus objetivos? ")
    mygoals.append(othergoal)
    checkMoreGoals = int(input("Do you have more goals to write down? 1.Sim 2.Não "))
 else:
    print("Not brabo")

print(mygoals)

        


        


