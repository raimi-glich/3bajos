num=-1
num2=-1

while(num <= 0 or num2 <= 0):
    num = int(input('escribe su numero'))
    num2 = int(input('escriba por quien quiera multiplicar'))

    if (num <=0 or num2 <=0):
        print('error, solo positivos.')

total=num
while(num2>1):
    num2-=1
    num = num + total

print ('El resultado es: {0} '.format(num))
