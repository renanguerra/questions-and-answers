import time

perguntas = open('perguntas.txt','r')
respostas = open('respostas.txt','r')
respostas_linha = respostas.readline()

score = 0
a = 0
estado = True      

def pergunta():
    for linhas in perguntas:
        if linhas == '\n':
            resposta_usuario = input('Qual sua resposta?: ')
            return resposta_usuario
            break
        elif linhas == 'fim':
            print('Final de jogo')
            break
        else:
            print (linhas)
            
def resposta():
    global score
    global a
    global estado
    
    if resposta_final == respostas_linha[a]:
        print('\nResposta Correta\n')
        score = score + 10
        a = a + 1
    else:
        estado = False
        print('Você errou')
        print('Fim de jogo!')
        print('Tente novamente')
        print('Seu score foi de {} pontos'.format(score))
            
                
nome = input('Qual o seu nome?: ')
time.sleep(1)
print ('\nOlá, {}'.format(nome))
time.sleep(1)
print ('\nSeja Bem-Vindo\n')
time.sleep(1)

while estado == True:
    resposta_final = pergunta()
    resposta()
