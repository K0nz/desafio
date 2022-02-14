# Programa-resposta para a terceira questão do desafio de programação

# substring da string
def contaAnagramadaSubstring(s):
	
	# Returna o total de anagramas
	# substrings em s
	n = len(s)
	mp = dict()
	
	# loop para o tamanho de substring
	for i in range(n):
		sb = ''
		for j in range(i, n):
			sb = ''.join(sorted(sb + s[j]))
			mp[sb] = mp.get(sb, 0)
			
			# Aumentando a contagem correspondente ao dicionário
			mp[sb] += 1

	anas = 0
	
	# loop por todo dicionário
	# contagem de items e agregados da substring
	for k, v in mp.items():
		anas += (v*(v-1))//2
	return anas

#input da string a ser analisada
anagramas=input()

# Driver
s = anagramas
print(contaAnagramadaSubstring(s))