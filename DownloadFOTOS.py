import urllib.request
fotoDesejada = input('Informe O Link Da Foto Desejada:\n')
foto = urllib.request.urlopen(fotoDesejada).read()
if '.png' in fotoDesejada:
    extensao_foto = '.png'
else:
    extensao_foto = '.jpg'
arquivo = open('foto'+extensao_foto, 'wb')    
arquivo.write(foto)
arquivo.close()
