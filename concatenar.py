with open('Original.txt') as file: #abro el archivo original
    lines1 = file.readlines()
with open('concatenado.txt') as file2: #abro el archivo de copia especificando que voy a escribir
    lines2 = file2.readlines()

print(len(lines1))
print(len(lines2))

for i in range(0, len(lines2)):
    if len(lines2) != len(lines1):
        print("El segundo archivo debe tener menos lineas que el primero")
        break
    lines2[i] = lines2[i].strip() + lines1[i].strip()

textoconcatenado = ""
for line in lines2:
    textoconcatenado += line + "\n"

with open('concatenado.txt', 'w') as file3:
    file3.write(textoconcatenado)