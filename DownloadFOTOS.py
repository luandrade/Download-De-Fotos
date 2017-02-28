import urllib.request
extensao_foto = ''
fotoDesejada = input('Informe O Link Da Foto Desejada:\n')
foto = urllib.request.urlopen(fotoDesejada).read()
if extensao_foto in 'png':
    extensao_foto = '.png'
else:
    extensao_foto = '.jpg'
arquivo = open('foto'+extensao_foto, 'wb')    
arquivo.write(foto)
arquivo.close()
