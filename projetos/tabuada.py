#Exercício: Tabuada

print("=== Tabuada ===")
print("Digite um número para ver sua tabuada:")
num = int(input("Número: "))
if num < 0:
    print("Por favor, insira um número não negativo.")
    exit()

print("Tabuada de", num)
print("------------------")
print(num, "x 1 =", num * 1)
print(num, "x 2 =", num * 2)
print(num, "x 3 =", num * 3)
print(num, "x 4 =", num * 4)
print(num, "x 5 =", num * 5)
print(num, "x 6 =", num * 6)
print(num, "x 7 =", num * 7)
print(num, "x 8 =", num * 8)
print(num, "x 9 =", num * 9)
print(num, "x 10 =", num * 10)
print("------------------")
print("Fim da tabuada.")