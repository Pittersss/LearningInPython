name = input("Qual é o seu nome: ")
fist_name = ""
last_name = ""
midnameAbv = ""
mid_name = ""
index1 = int(0)

elementsMidname = []
y = int(len(name)) - 1
z = True
num = 0
index2 = int(0)  

while y > 0 and z == True:
    if(name[y] != " "):
        last_name += name[y]
    else:
        z = False
        index2 = y
        break
    y -= 1

last_name = last_name[::-1]
   
for x in name:
    if x  != " ":
        fist_name += x
    else:
        break
    index1 += 1

mid_name = name[index1:index2]
omega = len(mid_name) - 1

while  num < omega:
    if mid_name[num] == " ":
        elementsMidname.append(num)
    num += 1

for u in elementsMidname:
    midnameAbv += mid_name[u +1] + ". "

print("Olá senhor(a) " + fist_name + " " + midnameAbv + last_name)