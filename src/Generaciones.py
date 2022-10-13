from Modulos.mutaciones.Mutacion import mutacion, mutacionAuto, mutacionJerar, mutacionAutoJerar
from Modulos.opBasicas.Decodificacion import DecodificacionAuto
from Modulos.mutaciones.MutacionPC2 import mutacionPC2, mutacionPC2Auto, mutacionPC2Jerar, mutacionPC2AutoJerar
from Modulos.mutaciones.MutacionUniforme import mutacionUnif, mutacionUnifAuto, mutacionUnifJerar, mutacionUnifAutoJerar

'''Opciones con 1'''
def combi1a(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacion(poblacion, longitud, rangoMin, rangoMax)
    print(listaBinarios)
    print(listaBinarios[0])
    print(type(listaBinarios[0]))
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionAuto(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break

def combi1b(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionPC2(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionPC2Auto(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break

def combi1c(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionUnif(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionUnifAuto(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break

'''Opciones con 2'''
def combi2a(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionJerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionAutoJerar(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break

def combi2b(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionPC2Jerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionPC2AutoJerar(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break

def combi2c(poblacion, longitud, rangoMin, rangoMax):
    listaBinarios = mutacionUnifJerar(poblacion, longitud, rangoMin, rangoMax)
    gen = int(input("Ingrese el numero de generaciones: "))
    print()
    x = 1
    while True:
        listaBin = mutacionUnifAutoJerar(
            listaBinarios, poblacion, longitud, rangoMin, rangoMax, x)
        listaBinarios = listaBin
        x += 1
        if (x == gen):
            tablaManual, valoresLongitud = DecodificacionAuto(
                listaBin, poblacion, longitud, rangoMin, rangoMax, x)
            break
