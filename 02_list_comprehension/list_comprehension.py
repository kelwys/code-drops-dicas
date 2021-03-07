# Lista de strings
nomes = ['Luiz', 'Maria', 'Natália', 'Miguel']

# Criando uma lista a partir de uma lista usando um for comum
novos_nomes = []
for nome in nomes:
   if 'a' in nome:
      novos_nomes.append(nome.replace('a', '@').upper()) 

# OUTPUT: ['M@RI@', 'N@TÁLI@']


# Criando uma lista a partir de uma lista usando uma list comprehension
novos_nomes = [nome.replace('a', '@').upper() for nome in nomes if 'a' in nome]

# OUTPUT: ['M@RI@', 'N@TÁLI@']