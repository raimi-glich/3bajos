Algoritmo h
	dividendo = -1
	divisor = -1
	Mientras dividendo<=0 o divisor<=0 Hacer
		Escribir 'digite su dividendo:'
		Leer dividendo
		Escribir 'dijite su divisor'
		Leer divisor
		Si dividendo<=0 o divisor<=0 Entonces
			Escribir 'Error, solo numeros positivos'
		FinSi
	FinMientras
	Mientras dividendo >= divisor Hacer
		dividendo = dividendo-divisor
	FinMientras
	Escribir 'su dividendo es:' dividendo
FinAlgoritmo
