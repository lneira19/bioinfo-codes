touch "Mover.txt"
chmod 777 "Mover.txt"
ls -lh *.txt
ls -l *.txt | wc -l
mv Mover.txt ./NombreCambiado.txt
echo Lucas Neira >> NombreCambiado.txt
echo Ivo Bajlec >> NombreCambiado.txt
echo Gonzalo Grau >> NombreCambiado.txt
wc -l NombreCambiado.txt
