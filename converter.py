from Bio.Seq import Seq

bienvenida = "¡Bienvenido!"
input_user_msg = "Ingrese una cadena de 6 nucleótidos: "

print(bienvenida)
input_user = input(input_user_msg)

coding_dna = Seq(input_user)
translated_SeqObj = coding_dna.translate()

print(f"Cadena de ADN ingresada: {input_user}")
print(f"Traducción: {translated_SeqObj}")

file = open("translation.txt","w")
file.write(f"{translated_SeqObj.__str__()}\n")