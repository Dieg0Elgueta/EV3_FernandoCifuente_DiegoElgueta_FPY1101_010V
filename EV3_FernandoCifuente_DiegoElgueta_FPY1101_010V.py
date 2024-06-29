import csv
import os
import random

emision_contaminanes: 2000
anotaciones_vigentes: 1800
multas: 3500

autos = []

def menu():
    print('===============================')
    print('             MENU              ')
    print('          AUTO SEGURO          ')
    print('===============================')
    print('1.- Grabar                     ')
    print('2.- Buscar                     ')
    print('3.- Imprimir Certificados      ')
    print('4.- Salir                      ')
    print('===============================')

def grabar(autos):

    tipo = input('Ingrese tipo de vehiculo: ').lower()
    patente = str(input('Ingrese SEIS digitos de la PATENTE de vehiculo: ')).lower()
    while len(patente) != 6:
        print('Patente no valida!')
        patente = input('Ingrese SEIS digitos de laPATENTE de vehiculo: ').lower()
    marca = input('Ingrese marca del vehiculo: ').lower()
    while len(marca) < 2 or len(marca) > 15:
        print('Marca no valida!')
        marca = input('Ingrese marca del vehiculo: ').lower()
    precio = int(input('Ingrese PRECIO del vehiculo: '))
    while precio < 5000000:
        print('Precio no correspondiente')
        precio = int(input('Ingrese PRECIO del vehiculo: '))
    multa_monto = int(input('ingrese MONTO de la multa: '))
    multa_fecha = input('Ingrese FECHA de la multa: ')
    registro = input('Ingrese fecha de registro del vehiculo: ')
    dueño = input('Ingrese NOMBRE del dueño del vehiculo: ').lower()

    autos.append({
        'tipo': tipo,
        'patente': patente,
        'marca': marca,
        'precio': precio,
        'multa_monto': multa_monto,
        'multa_fecha': multa_fecha,
        'registro': registro,
        'dueño': dueño
    })
    
    print('Se ha agregado Auto exitosamente!')
    os.system('pause')
    
def buscar(autos):
    patente = input("Ingrese su patente: ")
    for auto in autos:
        if auto['patente'] == patente:
            print(autos)
        else:
            print('Patente no encontrada')  

    os.system('pause')     

def imprimir_certificados(autos):

    contaminantes = random.randint(1500, 3500)
    multas = random.randint(1500, 3500)
    anotaciones = random.randint(1500, 3500)

    patente = input("Ingrese su patente: ")
    autos_a_imprimir = []
    for auto in autos:
        if auto['patente'] == patente:
            autos_a_imprimir.append(autos)
    nombreArchivo = f'Planilla_autos.csv'

    autos.append({
        'contaminantes': contaminantes,
        'multas': multas,
        'anotaciones':anotaciones 
    })

    with open (nombreArchivo, 'r', newline ='') as lista_autos_csv:
        lector_csv = csv.DictReader(lista_autos_csv)

        for fila in lector_csv:
            tipo = fila['tipo']
            patente = fila['patente']
            marca = fila['marca']
            precio = fila['precio']
            multa_monto = fila['multa_monto']
            multa_fecha = fila['multa_fecha']
            registro = fila['registro']
            dueño = fila['dueño']
            contaminantes = fila['contaminantes']
            multas = fila['multas']
            anotaciones = fila['anotaciones']

        if autos:
            autos_a_imprimir.append({
                'tipo' : tipo,
                'patente' : patente,
                'marca' : marca,
                'precio' : precio,
                'multa_monto' : multa_monto,
                'multa_fecha' : multa_fecha,
                'registro' : registro,
                'dueño' : dueño,
                'contaminantes' : contaminantes,
                'multas' : multas,
                'anotaciones': anotaciones})

def principal():
    autos = []
    sw = 1
    while sw == 1:
        menu()
        opc = int(input('Ingrese opcion que desea ingresar: '))
        if opc == 1:
            print('*****************************')
            print('        GRABAR AUTOS         ')
            print('*****************************')
            grabar(autos)
        elif opc == 2:
            print('*****************************')
            print('        BUSCAR AUTOS         ')
            print('*****************************')
            buscar(autos)
        elif opc == 3:
            print('*****************************')
            print('    IMPRIMIR CERTIFICADOS    ')
            print('*****************************')
            imprimir_certificados(autos)
        elif opc == 4:
            print('Usted ha decidido Salir')
            print('Fernando Cifuentes\nDiego Elgueta')
            print('V1.0')
            sw = 0
        else:
            print('Opcion no valida!')

principal()