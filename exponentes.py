numero=-1
exponente=-1

while(numero <= 0 or exponente <= 0):
    numero = int(input('escribe su numero'))
    exponente = int(input('escriba su exponente'))

    if (numero <=0 or exponente <=0):
        print('error, solo positivos.')

resultado=numero
while(exponente>1):
    exponente-=1
    numero = numero * resultado

print ('El exponente es: {0} '.format(numero))
