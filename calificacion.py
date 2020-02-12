def main():
    nota = int(input())
    print(CalcularCalificacion(nota))

def CalcularCalificacion(nota):
    if(nota<60):
        return 'F'
    elif(nota<70):
        return 'D'
    elif(nota<80):
        return 'C'
    elif(nota<90):
        return 'B'
    else:
        return 'A'

if(__name__== '__main__'):
    main()
