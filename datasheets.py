#Ficha para listar pessoas
from asyncio.windows_events import NULL
import os

fileName = input("Diga o nome do arquivo que deseja criar: \n") + ".txt"
arquivo = open(fileName, 'w+')
texto = arquivo.readlines()
if texto == " ":
 newName = input("Qual é o seu nome: \n")
 print("\n")
 
 texto.append(newName)
 arquivo.writelines("Nome: " + newName + "\n")
 
 newAge = input("Qual é a sua idade: \n")
 print("\n")
 texto.append(str(newAge))
 arquivo.writelines("Idade: " + newAge + "\n")

 newID = input("Qual é o seu CPF: \n")
 print("\n")
 texto.append(str(newID))
 arquivo.writelines("CPF: " + newID + "\n")
else:
    print("Essa ficha já foi preenchida!")
arquivo.close()
try:
  os.replace(fileName, "C:\\Users\\Pedro\\Desktop\\SQL TEST\\" + fileName)
except PermissionError:
  print("Você não tem permissão para fazer isso!")    