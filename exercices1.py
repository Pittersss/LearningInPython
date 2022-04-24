#Questão 1
#print("alo mundo")
#Questão 2
#numero = input("Escreva um número ")
#print("Esse foi o número que você escreveu: " + numero)
#Questão 3
#numero1 = 0
#numero2 = 0
#soma = 0
#while True:
 #try:
  #numero1 = int(input("Digite um número: "))
  #numero2 = int(input("Digite outro número: "))
  #soma = numero1 + numero2
  #print("A soma desses número é: " + str(soma))
  #break
 #except ValueError:
    #print("Digite apenas números!")
#Questão 4
#notas = []
#i = 0
#bimestre = ""
#soma = 0
#num = 0
#while True:
 #try:
       #while i <= 3:
          #if i == 0:
            #bimestre = "primeiro"
          #if i == 1:
           #bimestre = "segundo"
          #if i == 2:
            #bimestre = "terceiro"
          #if i == 3:
            #bimestre = "quarto"
          #notas.append(int(input("Digite a nota do " + bimestre + " bimestre: ")))
          #i += 1

       #for x in notas:
          #soma += notas[num]
          #num += 1   

       #print("A sua média é: " + str(soma/4))
       #break
 #except ValueError:
     #print("Escreva apenas números!")
#Questão 5
#while True:
 #try:
     # metros = float(input("Escreva quantos metros deseja converter para centrímetros"))
      #centimetros = metros * 100
      #print("{} metros equivale a {} centímetros".format(metros, centimetros))
      #break
 #except ValueError:
    #print("Digite apenas números!")
#Questão 6
#import math
#while True:
 #try:
    #raio = float(input("Digite o raio do círculo: "))
    #area = math.pi * math.pow(raio,2)
    #print("A área do círculo é: " + str(area))
 #except ValueError:
    #print("Digite apenas números!")

#Questão 7
#import math
#while True:
  #try:
   #side = float(input("Digite o lado: "))
   #area = math.pow(side,2)
   #print("O dobro da área do quadrado é: " + str(area * 2))
   #break
  #except:
   #print("Digite apenas números!")

#Questão 8
#value = float(input("Quanto você ganha por hora? "))
#hoursPerMonth = float(input("Quantas horas você trabalha por mês? "))
#print("Você recebe mensalmente: " + str(value * hoursPerMonth))

#Questão 9
#while True:
   #try:
         #f = float(input("Digite a temperatura em Fahrenheit: "))
         #c =  5 * ((f - 32)/9)
         #print(str(f) + "{} equivale a: {}{}".format("°F",c,"°C"))
         #break
   #except ValueError:
      #print("Digite apenas números!")

#Questão 10
#while True:
   #try:
      #c = float(input("Digite a temperatura: "))
      #f = ((c/5) * 9) + 32
      #print(str(c) + "{} equivale a: {}{}".format("°C",f,"°F"))
      #break
   #except ValueError:
      #print("Digite apenas números!")

#Questão 11
#import math
#int1 = int(input("Digite um número inteiro: "))
#int2 = int(input("Digite outro número inteiro: "))
#real = float(input("Digite um número real: "))
#res1 = ((int1 * 2) * (int2/2))
#print("Resultado 1: " + str(res1))
#res2 = ((int1 * 3) + real)
#print("Resultado 2: " + str(res2))
#res3 = math.pow(real,3)
#print("Resultado 3: " + str(res3))

#Questão 12
#while True:
   #try:
     #altura = float(input("Qual é a sua altura "))
     #pesoIdeal = (72.7 * altura) - 58
     #print("O peso ideal para você é: " + str(pesoIdeal.__round__(3)))
     #break
   #except:
     #print("DIGITE APENAS NÚMEROS!")

#Questão 13
#pesoIdeal = 0
#while True:
   #try:
      #altura = float(input("Qual é a sua altura "))
      #sexo = int(input("Digite 1 caso você seja homem ou digite 2 caso seja mulher"))
      #if sexo == 1:
           #pesoIdeal = (72.7 * altura) - 58
      #if sexo == 2:
          #pesoIdeal = (62.1 * altura) - 44.7
      #print("Seu peso ideal é: {}".format(pesoIdeal.__round__(3)))
      #break
   #except:
     #print("DIGITE APENAS NÚMEROS!")

#Questão 14

#while True:
   #try:
    #quilos = float(input("Quantos quilos de peixe você pescou hoje, João?\n"))
    #excesso = 0
    #multa = 0
    #if quilos > 50:
       #excesso = quilos - 50
       #multa = (excesso * 4)
       #print("Você terá que pagar de multa {}$".format(multa))
    #else:
      #print("Você está dentro dos padrões, João. Parabéns! Aproveite o seu dinheiro")
    #break
   #except ValueError:
      #print("Digite apenas números!")

#Questão 15
#while True:
   #rendaBruta = float
   #rendaLiquida = float
   #impostoINSS = round(float,2)
   #ImpostoDeRenda = round(float,2)
   #moneyForSindicato = float
   #try:
       #moneyPerHour = float(input("Quanto você ganha por hora? "))
       #hoursWorkedPerMonth = float(input("Quantas horas você trabalha por mês? "))
       #rendaBruta = moneyPerHour * hoursWorkedPerMonth
       #impostoINSS = (rendaBruta * 0.05)
       #ImpostoDeRenda = (rendaBruta * 0.08)
       #moneyForSindicato = impostoINSS + ImpostoDeRenda
       #rendaLiquida = rendaBruta - moneyForSindicato

       #print("Seu salário bruto é {}$".format(rendaBruta))
       #print("Você pagou ao INSS: {}$".format(impostoINSS))
       #print("Você pagou ao sindicato {}$".format(moneyForSindicato))
       #print("Sua renda líquida é: {}$".format(rendaLiquida))
       #break
   #except ValueError:
      #print("Digite apenas números!")
 
#Questão 16
#import math


#valueLata = 80
#quantityLitros = float
#quantityLatas = float
#while True:  
   #try:
     #mQuad = float(input("Quantos metros quadrados tem a parede que será pintada? "))
     #quantityLitros = mQuad/3
     #if quantityLitros <= 18:
        #print("Você precisará somente de uma lata, vai custar {}$".format(valueLata))
     #else:
        #quantityLatas = quantityLitros/18
        #print("Você precisará de {} latas que custará {}$".format(math.ceil(quantityLatas), math.ceil(math.ceil(quantityLatas) * valueLata)))
     #break
   #except ValueError:
      #print("Tua mãe")

#Questão 17
#import math
#QuantityLlata = 18
#QuantityLgalao = 3.6
#valueLata = 80
#valueGalao = 25
#quantityLitros = float

#while True:
   #try:
      #mQuad = float(input("Quantos metros quadrados você pintará? "))
      #quantityLitros = mQuad/6    
      #print(quantityLitros)
      #print("Você poderá comprar {} {} Custará: {}$ \n".format(math.ceil(quantityLitros/QuantityLlata),"lata(s)", math.ceil((quantityLitros/QuantityLlata)) * valueLata))
      #print("Você poderá comprar {} {} Custará: {}$ \n".format(math.ceil(quantityLitros/QuantityLgalao),"galõe(s)", math.ceil((quantityLitros/QuantityLgalao)) * valueGalao))
      #if(quantityLitros % 18 != 0 and quantityLitros > 18):
         #num = quantityLitros
         #index = 0
        # while(num >= 20): #Folga de, aproximadamente, 10%
            #index += 1
            #num -= 18
         #gal = math.ceil(num/QuantityLgalao)
         #print("Você poderá comprar {} lata(s) e {} galão(ões) Custará: {}$ \n".format(index, gal, (index * valueLata) + (gal * valueGalao)))
   #except  ValueError:
      #print("Ocorreu um erro nos caracteres digitados, tente novamente!")

#Questão 18
#import math
#tamanhoArquivo = float(input("Qual é o tamanho do arquivo em Mb? ")) #MB
#velInternet = float(input("Qual é a velocidade da sua internet em Mbps? ")) #Mbps
#calc = math.ceil((tamanhoArquivo/velInternet)/60)
#print("Seu arquivo vai levar {} minutos, aproximadamente".format(calc))
