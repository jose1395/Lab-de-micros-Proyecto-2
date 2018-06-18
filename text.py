# Image es una biblioteca para poder importar imagenes
# pytesseract es la biblioteca de tesseract OCR, la cual se encarga de extraer los caracteres de las imagenes
from PIL import Image
import pytesseract
import glob, os

# Se abre el documento 'doc.txt' y se extraen las lineas la cual corresponden a cada una de las placas que estan en la 'base de datos'
# data_list es un arreglo que guarda cada una de las placas que se leen de la base de datos
# lenght es el tamano de la 'base de datos'

f = open("doc.txt",'r')
data_list = f.readlines()
f.close()
data_list = [item.rstrip('\n') for item in data_list]
length = len(data_list)
while True:
# sensor, representa los sensores, '1' representa que hay un carro, '0' no hay 
    print ("Sensor:"),;sensor=input()
    if sensor==1:
# For que revise todas las posibles imagenes (infiel) que existen en el directorio
        for infile in glob.glob("*.jpg"):
            file, ext = os.path.splitext(infile)
# Funcion para abrir las imagenes
            im = Image.open(infile)
# Funcion para extraer el texto de la imgane (infile)
            text = pytesseract.image_to_string(im, lang = 'eng')
# For que recorre toda la 'base de datos' y verifica si la informacion extraida de la imagen (text) coincide con algun dato de la 'base de datos'
            for i in range(len(data_list)+1):
                if data_list[i]==text:
	            print("\n")
                    print ("Buen Viaje")
	            print("Auto: "),; print(infile)
   	            print(text)
	            print("\n")
	            break
# Si no encuentra la el numero de placa en la base datos imprime el msj que debe pagar xD 
	        elif i==length-1:
	           print("\n")
                   print("Error, debe cancelar 100 colones")
	           print("Auto: "),; print(infile)
                   print(text)
	           print("\n")
	           break
                else:
	           None
    else:
        None


