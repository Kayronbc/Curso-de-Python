import random

print(random.randrange(1, 100))
#imprime numeros aleatorios entre o intervalo dado, incluindo o primeiro e excluindo o ultimo

print(random.random())
#imprime um numero aleatorio entre 0 e 1

print(random.randint(10, 20))
#imprime numeros aleatorios entre o intervalo dado, incluindo os extremos

frutas = ['maca', 'banana', 'laranja', 'uva', 'pera']
print("Fruta Escolhida: " + random.choice(frutas))
#imprime um elemento aleatorio da lista dada

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print("Numeros embaralhados: ", numeros)
#embaralha a lista dada

sorteados = random.sample(range(1, 60), 6)
print("Numeros sorteados: ", sorteados)
#imprime 5 numeros aleatorios unicos entre o intervalo dado 

print(random.uniform(1.5, 10.5))
#imprime um numero aleatorio de ponto flutuante entre o intervalo dado, incluindo os extremos