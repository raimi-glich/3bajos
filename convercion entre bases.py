def main() :
    valorCapturado = capturarPositivo()

    baseOrigen = 0
    while(baseOrigen < 2 or baseOrigen >10):
        print('indique la base origen:')
        baseOrigen = capturarPositivo()

    baseDestino = 0
    while(baseDestino < 2 or baseDestino > 10):
        print('índique la base del destino')
        baseDestino = capturarPositivo()

    if(baseDestino == 10):
        print(convertirABase10(valorCapturado, baseOrigen))
    elif(baseOrigen == 10):
        print(convertirDesdeBase10(valorCapturado, baseDestino))
    else:
        print('no se puede hacer esta convercion.')

def capturarPositivo():
    resultado = 0

    while(resultado <= 0):
        resultado = int(input('digite un valor positivo'))

        if(resultado <= 0):
            print('solo positivos')
    return resultado
def convertirABase10(valor, baseOrigen):
    potencia = 1
    numeroConvertido = 0

    while(valor>0):
        numeroConvertido += valor%10 * potencia
        potencia *=baseOrigen
        valor //= 10

    return numeroConvertido

def convertirDesdeBase10(valor, baseDestino):
    potencia10=1
    numeroConvertido = 0

    while(valor > 0):
        numeroConvertido += (valor % baseDestino * potencia10)
        valor //= baseDestino
        potencia10 *= 10

    return numeroConvertido


if(__name__=="__main__"):
    main()
    
