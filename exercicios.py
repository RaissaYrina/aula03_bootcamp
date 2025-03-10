#Exercicios da aula

# EXERCÍCIOS DE IF
#Exercício 1: Verificação de Qualidade de Dados
#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos 
# para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos 
# ou "Dados inválidos" caso contrário.
'''
quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print('Valores válidos')
else:
    print('Valores invalidos')
'''

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha 
# idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e 
# imprima "Dados de usuário válidos" ou o erro específico encontrado.


# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial 
# (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

#EXERCICIOS DE FOR

#Contagem de Palavras em Textos
#Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
'''
texto = 'hoje é nossa terceira aula do bootcamp, o bootcamp de python'

novo_texto = texto.replace(',','') #substituindo , por vazio
#quebrar o texto
palavras = novo_texto.split()

print(palavras)

contagem_de_palavras = {} # dicionario vazio 

#eu quero percorrer todas as palavras dentro de palavra e checa se ela ja esta no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else: 
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)'
'''

# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.