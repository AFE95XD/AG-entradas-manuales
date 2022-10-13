def binarioDecimal(poblacion, longitud):

    listaStr = []
    listaDecimales = []
    listaBinarios = []
    i = 1
    while i <= int(poblacion):
        numero = input("\nIntroduce el numero binario: ")
        if len(numero) == longitud:
            listaStr.append(numero)

            listaBinarios.append(numero)

            numero_decimal = int(listaStr[i-1], 2)
            listaDecimales.append(numero_decimal)
            print(
                f'El número en decimal de {listaStr[i-1]} es {numero_decimal}')
            i += 1
        else:
            print("Debe ser de longitud", int(longitud), "intentalo de nuevo")
    return listaDecimales, longitud, listaBinarios


def binarioDecimalAuto(listaBin, poblacion, longitud):

    listaStr = []
    listaDecimales = []
    listaBinarios = []
    i = 1
    while i <= int(poblacion):
        if len(listaBin[i-1]) == longitud:
            listaStr.append(listaBin[i-1])

            listaBinarios.append(listaBin[i-1])

            numero_decimal = int(listaStr[i-1], 2)
            listaDecimales.append(numero_decimal)
            print(
                f'El número en decimal de {listaStr[i-1]} es {numero_decimal}')
            i += 1
        else:
            print("Debe ser de longitud", int(longitud), "intentalo de nuevo")
    return listaDecimales, longitud, listaBinarios
