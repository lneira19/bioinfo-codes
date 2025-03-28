touch ListadoNombres.txt

read -p "Ingrese un nombre: " nombre
read -p "Ingrese un apellido: " apellido

echo "$nombre $apellido" >> ListadoNombres.txt
