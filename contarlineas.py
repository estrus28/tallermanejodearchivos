path = 'contlineas.txt'
contadorlineas = 0 #creo contador para las lineas

try:
    with open(path) as file: #abro el archivo
        for line in file: #leo las lineas en el archivo
            contadorlineas += 1 #se suma 1 por cada linea que cuenta
except:
    print("El archivo no pudo ser leido") #Uso except por si el archivo no puede ser leido
finally:
    print(contadorlineas) 
