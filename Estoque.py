#Faturamento
faturamento = int(input("Qual o faturamento?"))
percentual_bonus = float(input("Qual o percentual?"))
bonus_total = faturamento * percentual_bonus
faturamento_liquido = faturamento - bonus_total
print(f'o bônus total é R$ {bonus_total:.2f} e o faturamento_liquido é {faturamento_liquido:.2f}')

#Controle de Estoque
estoque = int(input('Estoque'))
vendas = int(input('Vendas'))
reposiçao = int(input('Reposição'))
estoque_final = estoque - vendas + reposiçao
print(f'Estoque atual é {estoque_final}')

#Logística
caixa = int(input('Qtd de caixas'))
capacidade_caminhoes = int(input('Capacidade total'))
caminhoes_completos = caixa // capacidade_caminhoes
print(f'Caixas restantes {caminhoes_completos}')
input()
