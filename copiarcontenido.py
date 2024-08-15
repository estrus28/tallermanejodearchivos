with open('Original.txt') as file: #abro el archivo original
    lines = file.read() #leo las lineas y devuelve un string dentro de lines
    with open('Copia.txt', 'w') as file2: #abro el archivo de copia especificando que voy a escribir
        file2.write(lines) #escribo el string devuelto en lines en el archivo de la copia