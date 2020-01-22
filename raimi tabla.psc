Algoritmo tablademultiplicar
	num <- -1
	Mientras num<=0 O num>12 Hacer
		Escribir 'Escriba el numero de la tabla que quiera vizualizar'
		Leer num
		Si num<=0 Entonces
			Escribir 'error. la tabla solo es de numeros positivos mayores que 0.'
		FinSi
		Si num>12 Entonces
			Escribir 'error. la tabla solo llega hasta el 12'
		FinSi
	FinMientras
	min = 1
	max = 12
	total = 0
	Mientras min<=max Hacer
		Escribir num, 'x' , min, '=' , num*min
		total = total+num*min
		min = min+1
	FinMientras
	Escribir 'la suma de todos los resultados es:', total
	Escribir 'gracias por usar este programa, tenga buen dia'
FinAlgoritmo
