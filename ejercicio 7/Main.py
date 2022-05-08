import csv
from Viaje import Viajero

if __name__ == '__main__':
    lista=[]
    archivo = open("Viajantes.csv")
    reader=csv.reader(archivo,delimiter=",")
    total=0
    c=0
    for fila in reader:
        objeto=Viajero(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
        lista.append(objeto)
    numero = int(input('\ningrese numero de pasajero:'))
    opcion = None
    otroviajero=Viajero('Francisco','Manzano','34932432','5','2454')
    for objeto in lista:
        if numero == objeto.getNumero():
            while opcion!='d':
                print('\n')
                print ('a) Comparar millas')
                print ('b) Las millas acumuladas + 100 es:')
                print ('c) Canjear millas')
                print ('d) Salir')
                opcion = input('\nIngrese opcion a realizar:')
 
                if opcion=='a':
                    x=int(input('\nIngrese el valor entero a comparar:'))
                    i=otroviajero.getMillas()==x
                    if True:
                        print('\nEl viajero frecuente tiene la misma cantidad millas acumuladas')
                
                elif opcion=='b':
                    print('\nLas millas acumuladas son:', objeto.getMillas()+otroviajero.getMillas())
                
                elif opcion=='c':
                    x=int(input('\nIngrese el valor que quiere canjear:'))
                    print('\nLas millas canjeadas son:', otroviajero.getMillas()-x)