file = open('docker-compose.yml', 'r+')

# Le o arquivo
file_string = file.read()

# Corrige o texto
new_file_string = file_string.replace('\t', '  ')

# Retorna o file handler para o inicio do arquivo
file.seek(0)

# Sobrescreve o arquivo com o novo texto 
file.write(new_file_string)

file.close()
