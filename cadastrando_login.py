#Login
login = input('Digite seu e-mail.com')
senha = input('Digite sua senha')
login_correto = "anclarap09@gmail.com"
senha_correto = "ABC123@"
login_valido = login.endswith('gmail.com')
tem_letra = any(char.isalnum() for char in senha)
tem_especial = any(char.isalpha() for char in senha)
senha_valida = tem_letra and tem_especial
#Verificação
if login_valido and senha_valida:
    print('\cadastro aprovado com sucesso')
else:
    print('\cadastro reprovado com sucesso')

input()
