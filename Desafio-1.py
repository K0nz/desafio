#Programa-resposta para a primeira questão do desafio de programação

#Input do número de linhas a ser impresso
print("Insira seu número:")
n = int(input())

#Impressão da quantidade de '*' por linha equivalente à linha
x = 1
print("Saída:")
while x <= n:
    print("*"*x)       
    x=x+1
