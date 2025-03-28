filename="ListadoNombres.txt"

ls $filename 2>> Errores.log

if [[ $? -gt 0 ]];then
echo "El archivo $filename no existe en su directorio."
else

read -p "Ingrese un apellido: " apellido

repeticiones=$(grep $apellido $filename | wc -l)

if [[ repeticiones -gt 1 ]];then
echo "Apellido múltiple"

elif [[ repeticiones -eq 0 ]];then
echo "Apellido inexistente"

else
echo "El apellido $apellido aparece $repeticiones vez."

fi

fi
