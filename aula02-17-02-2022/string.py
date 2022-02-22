"""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução aos tipos de dados (string)
"""

nome = " igor mendes melo "

### Métodos de string com a sintaxe nome.metodo()

print(f"Nome em maiúsculo: {nome.upper()}")

print(f"Nome em minúsculo: {nome.lower()}")

print(f"Primeira letra em maiúsculo: {nome.capitalize()}")

# Utilização de aspas simples e duplas
print(f"Contando quantas vezes a letra 'e' aparece no nome: {nome.count('e')}")

print(f"Removendo espaços em branco no começo e final da string: {nome.strip()}")

print(f"Substituindo meu nome por algo engraçado: {nome.replace('igor', 'xpto')}")

print(f"Separando o nome em partes: {nome.split()}")

### Função len()

# Espaço em branco conta
print(f"A minha string contém {len(nome)} caracteres")
