Algoritmo EdadUsuario
	Escribir 'Escriba su nombre:'
	Leer NombreDelUsuario
	Edad <- -1
	Mientras edad<0 Hacer
		Escribir 'Escriba su edad'
		Leer edad
		Si edad<0 Entonces
			Escribir 'Error. La edad no puede ser negativa.'
		FinSi
	FinMientras
	Escribir 'Su nombre es:' ,NombreDelUsuario, ', y su edad es:' ,edad, 'a�os.'
	edad = edad+10
	Escribir 'Su edad en 10 a�os ser�:' , edad, 'a�os.'
FinAlgoritmo
