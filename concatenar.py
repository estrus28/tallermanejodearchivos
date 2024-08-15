with open('Original.txt') as file: #abro el archivo original
    for line in file:
        content = line
        with open('concatenado.txt', 'a') as file2: #abro el archivo de copia especificando que voy a escribir
            file2.write(content) 
    