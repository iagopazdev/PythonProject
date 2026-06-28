arquivo = open("arquivo.txt", "w")

arquivo.write('curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#leitura do arquivo texto

leitura=open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()