dividendo=-1
divisor=-1

while (dividendo <= 0 or divisor <= 0):
    dividendo = int(input('dijite el dividendo'))
    divisor = int(input('dijite el divisor'))
    
    if (dividendo <=0 or divisor <=0):
        print('Error, solo positivos.')
        
cociente = 0
while (dividendo >= divisor):
    cociente+=1
    dividendo -= divisor

print ('El cociente es: {0} '.format(cociente))

