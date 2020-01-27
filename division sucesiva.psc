Algoritmo division
	dividendo <- -1
	Mientras dividendo<=0 O divisor<=0 Hacer
		Escribir 'digite el dividendo'
		Leer dividendo
		Escribir 'digite el divisor'
		Leer divisor
		Si dividendo<=0 O divisor<=0 Entonces
			Escribir 'error, solo numeros positivos'
		FinSi
	FinMientras
	cociente <- 0
	Mientras dividendo>=divisor Hacer
		cociente <- cociente+1
		dividendo <- dividendo-divisor
	FinMientras
	Escribir 'su resultado es:',cociente
	Escribir 'y su residuo es:',dividendo
FinAlgoritmo
