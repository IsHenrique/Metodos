import intervalos

resultado = intervalos.intervaloconfiancadesvio(500, 100, 5, 95)
print(resultado)
amostra = ['9', '8', '12', '7', '9', '6', '11', '6', '10', '9']

resultado2 = intervalos.intervaloconfiancasemdesvio(amostra, 95)
print(resultado2)

resultado3 = intervalos.populacional(160, 200, 95)
print(resultado3)


