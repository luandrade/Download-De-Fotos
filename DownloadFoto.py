#este programa faz o dowload de fotos
import urllib.request
#ele irá ler o arquivo que está em binário
foto = urllib.request.urlopen('http://www.bestriders.com.br/newblog/wp-content/uploads/2016/01/TESTE_KAWASAKI_NINJA_H2R_06.jpg').read()
#e ira transforma-lo em um arquivo, sendo assim virará uma imágem  
file = open('moto1.png', 'wb')
file.write(foto)
file.close()
