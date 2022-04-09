#PolarZenit
from dataclasses import replace
from operator import index

password = str(input("Diga a sua senha "))
password = password.upper()
for x in password:
     if x == "P" or "Z":
         if x == "P":
             password = password.replace("P", "Z")
         if x == "Z":
             password = password.replace("Z", "P")
     if x == "O" or "E":
         if x == "O":
             password = password.replace("O", "E")
         if x == "E":
             password = password.replace("E", "O")
     if x == "L" or "N":
         if x == "L":
             password = password.replace("L", "N")
         if x == "N":
             password = password.replace("N", "L")
     if x == "A" or "I":
         if x == "A":
            password = password.replace("A", "I")
         if x == "I":
            password = password.replace("I","A")
     if x == "R" or "T":
         if x == "R":
           password = password.replace("R", "T")
         if x == "T":
             password = password.replace("T", "R")


print(password)


