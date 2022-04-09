#PolarZenit
password = str(input("Escreva algo para encriptar: "))
password = password.upper()
characters = []
encryptWord =  ""
for x in password:
    characters.append(x)
dex = len(characters)
x = 0
while x < dex:
    #P e Z
    if characters[x] == "P" or "Z":
        if characters[x] == "P":
            characters[x]  = "Z"
        elif characters[x] == "Z":
            characters[x] = "P"
    #O e E
    if characters[x] == "O" or "E":
        if  characters[x] == "O":
            characters[x] = "E"
        elif characters[x] ==  "E":
            characters[x] = "O"
    
    #L e N
    if characters[x] == "L" or "N":
        if characters[x] == "L":
            characters[x] = "N"
        elif characters[x] == "N":
            characters[x] = "L"
    
    #A e I
    if characters[x] == "A" or "I":
        if characters[x] == "A":
            characters[x] = "I"
        elif characters[x] == "I":
            characters[x] = "A"

    #R e T
    if characters[x] == "R" or "T":
        if characters[x] == "R":
            characters[x] = "T"
        if characters[x] == "T":
            characters[x] = "R"
    x += 1
for z in characters:
    encryptWord += z
print(encryptWord)
