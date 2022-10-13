# lista = ['101011010', '101010100', '010110101',
#          '001101010', '011011010', '101010001', '011011101']


# def binarioDecimal(listaBin, poblacion, longitud):

#     listaStr = []
#     listaDecimales = []
#     listaBinarios = []
#     i = 1
#     while i <= int(poblacion):
#         if len(listaBin[i-1]) == longitud:
#             listaStr.append(listaBin[i-1])

#             listaBinarios.append(listaBin[i-1])

#             numero_decimal = int(listaStr[i-1], 2)
#             listaDecimales.append(numero_decimal)
#             print(
#                 f'El número en decimal de {listaStr[i-1]} es {numero_decimal}')
#             i += 1
#         else:
#             print("Debe ser de longitud", int(longitud), "intentalo de nuevo")
#     return listaDecimales, longitud, listaBinarios


# listaDecimales, longitud, listaBinarios = binarioDecimal(lista, 7, 9)

# print(listaDecimales)
# print(longitud)
# print(listaBinarios)

# padre1 = "0100101011"
# padre2 = "0010101110"

# pcMax = 6
# pcMin = 2

# if pcMin != 0:
#     hijo1 = padre1[:-pcMax]
#     hijo2 = padre2[:-pcMax]
#     corteP1 = padre1[-pcMax:-(pcMin-1)]
#     corteP2 = padre2[-pcMax:-(pcMin-1)]
#     res1 = padre1[-(pcMin-1):]
#     res2 = padre2[-(pcMin-1):]

#     hijo1 = hijo1 + corteP2 + res1
#     hijo2 = hijo2 + corteP1 + res2
# else:
#     hijo1 = padre1[:-pcMax]
#     hijo2 = padre2[:-pcMax]
#     corteP1 = padre1[-pcMax:]
#     corteP2 = padre2[-pcMax:]

#     hijo1 = hijo1 + corteP2
#     hijo2 = hijo2 + corteP1

# corteP3 = padre2[-pcMax:]
# print(corteP3)

# from Modulos.selecOrdenamiento.Jerarquia import jer
# from Modulos.selecOrdenamiento.Ruleta import tablaOrdenadaManual
# jer()
# tablaOrdenadaManual(poblacion=13, longitud=9, rangoMin=1, rangoMax=9)

# from Modulos.selecOrdenamiento.Torneo import torneo

from Modulos.selecOrdenamiento.Torneo import torneo

torneo(13, 9, 1, 9)

# 010111010  186
# 100101001  297
# 001010101  85
# 000111001  57
# 110010101  405
# 110101010  426
# 000110110  54
# 000110101  53
# 011010101  213
# 101100001  353
# 001010101  85
# 001100010  98
# 001111001  121