RnaMensager = input("Digite a sequência de bases nitrogenadas do DNA que será traduzida: ")
RnaMensager = RnaMensager.upper()
traduzido = ""
y = 0
RnaTranslator = []
for x in RnaMensager:
    RnaTranslator.append(x)
dex = len(RnaTranslator)

while y < dex:
    if RnaTranslator[y] == "A" or "U":
        if RnaTranslator[y] == "A":
            RnaTranslator[y] = "U"
        elif RnaTranslator[y] == "A":
            RnaTranslator[y] =  "U"
    if RnaTranslator[y] == "T":
        RnaTranslator[y] = "A"
    if RnaTranslator[y] == "C" or "G":
        if RnaTranslator[y] == "C":
            RnaTranslator[y] = "G"
        elif RnaTranslator[y] == "G":
            RnaTranslator[y] =  "C"
    y += 1

for z in RnaTranslator:
    traduzido += z
print(traduzido)

        
