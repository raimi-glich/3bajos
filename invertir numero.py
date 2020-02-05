def main():
    valor = capturarpositivo()
    print(invertir(valor))
    
def capturarpositivo():
    valor = 0
    while(valor<=0):
        valor = int(input('digite su valor:'))
        if(valor <= 0):
            print('solo numeros positivos')
    return valor

def invertir(numero):
    re=0

    while(numero > 0):
        re *=10
        re += numero%10
        numero //=10
    return re

if (__name__=="__main__"):
    main()
