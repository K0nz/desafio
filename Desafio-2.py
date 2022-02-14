# Função de validação de senha

Senha=input()
def cheq_senha(senha):
	
	Simbesp =['!','@','#','$','%','^','&','*','(',')','-','+']
	val = True
	
	if len(senha) < 6:
		print('Faltam '+str(int(6-len(senha)))+' caracteres.')
		val = False
		
	if not any(char.isdigit() for char in senha):
		print('A senha deve ter ao menos 1 dígito.')
		val = False
		
	if not any(char.isupper() for char in senha):
		print('A senha deve ter ao menos uma letra maiúscula.')
		val = False
		
	if not any(char.islower() for char in senha):
		print('A senha deve ter ao menos uma letra minúscula.')
		val = False
		
	if not any(char in Simbesp for char in senha):
		print('A senha deve ter ao menos um símbolo especial: !@#$%^&*()-+.')
		val = False
	if val:
		return val

# Método Main
def main():
	senha = Senha
	
	if (cheq_senha(senha)):
		print("Senha é válida!")
	else:
		print("Senha inválida!")
		
# Driver		
if __name__ == '__main__':
	main()
