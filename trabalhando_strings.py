#Algumas coisas que podemos fazer com strings em Python

# Concatenação de strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome Completo: " + nome_completo)

# Repetição de strings
eco = "Olá! " * 3
print("Eco: " + eco)

# Acesso a caracteres individuais
frase = "Python é divertido"
primeira_letra = frase[0]
ultima_letra = frase[-1]
print("Primeira letra: " + primeira_letra)
print("Última letra: " + ultima_letra)

# Fatiamento de strings
parte = frase[9:11] # Pega os caracteres do índice 9 ao 10
print("Parte da frase: " + parte)
primeiros_cinco = frase[:5]
print("Primeiros cinco caracteres: " + primeiros_cinco)
ultimos_cinco = frase[-5:]
print("Últimos cinco caracteres: " + ultimos_cinco)

# Comprimento da string
tamanho = len(frase)
print("Tamanho da frase: " + str(tamanho))

# Métodos de string
frase_maiuscula = frase.upper()
print("Frase em maiúsculas: " + frase_maiuscula)
frase_minuscula = frase.lower()
print("Frase em minúsculas: " + frase_minuscula)
frase_substituida = frase.replace("divertido", "incrível")
print("Frase substituída: " + frase_substituida)
palavras = frase.split(" ") #divide a frase em uma lista de palavras, usando o espaço como separador
print("Palavras na frase: " + str(palavras))
frase_junta = " ".join(palavras) #junta a lista de palavras em uma única string, usando o espaço como separador
print("Frase juntada: " + frase_junta)

# Verificação de substring
existe = "Python" in frase
print("A palavra 'Python' existe na frase? " + str(existe))
nao_existe = "Java" not in frase
print("A palavra 'Java' não existe na frase? " + str(nao_existe))
#podemos usar o if para validar se a palavra existe ou nao na frase
if "diverido" in frase:
    print("a palavra 'divertido' foi encontrada na frase!")
else:
    print("a palavra 'divertido' nao foi encontrada na frase!") 


# Remoção de espaços em branco
frase_com_espacos = "   Aprendendo Python   "
frase_sem_espacos = frase_com_espacos.strip()
print("Frase sem espaços: '" + frase_sem_espacos + "'")
frase_sem_espacos_esquerda = frase_com_espacos.lstrip()
print("Frase sem espaços à esquerda: '" + frase_sem_espacos_esquerda + "'")
frase_sem_espacos_direita = frase_com_espacos.rstrip()
print("Frase sem espaços à direita: '" + frase_sem_espacos_direita + "'")


