import time

perguntas = open('perguntas.txt','r')
respostas = open('respostas.txt','r')
pontu = open('pontuação.txt','r')
respostas_linha = respostas.readline()

score = 0
a = 0
estado = True      

#-------------------------------FUNÇÕES------------------------------
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
        
def pontuação():
    global score
    global nome
    pontu = open('pontuação.txt','r')

    scorestr = str(score)
    pontos = nome + ' ' + scorestr + '\n'

    cabeçalho = pontu.readline()
    primeiro = pontu.readline()
    segundo = pontu.readline()
    terceiro = pontu.readline()
    quarto = pontu.readline()
    quinto = pontu.readline()
    pontu.close()

    primeiro_separa = primeiro.split()
    primeiro_pontu = int(primeiro_separa[1])

    segundo_separa = segundo.split()
    segundo_pontu = int(segundo_separa[1])

    terceiro_separa = terceiro.split()
    terceiro_pontu = int(terceiro_separa[1])

    quarto_separa = quarto.split()
    quarto_pontu = int(quarto_separa[1])

    quinto_separa = quinto.split()
    quinto_pontu = int(quinto_separa[1])


    if score < quinto_pontu:
        print('nada acontece')
    elif score >= primeiro_pontu:
        pontu = open('pontuação.txt','w')
        pontu.write(cabeçalho)
        pontu.write(pontos)
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()
    elif score >= segundo_pontu and score < primeiro_pontu:
        pontu = open('pontuação.txt','w')
        pontu.write(cabeçalho)
        pontu.write(primeiro)
        pontu.write(pontos)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()
    elif score >= terceiro_pontu and score < segundo_pontu:
        pontu = open('pontuação.txt','w')
        pontu.write(cabeçalho)
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(pontos)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()
    elif score >= quarto_pontu and score < terceiro_pontu:
        pontu = open('pontuação.txt','w')
        pontu.write(cabeçalho)
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(pontos)
        pontu.write(quarto)
        pontu.close()
    elif score >= quinto_pontu and score < quarto_pontu:
        pontu = open('pontuação.txt','w')
        pontu.write(cabeçalho)
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.write(pontos)
        pontu.close()          
#------------------------------MAIN------------------------------------------



nome = input('Digite seu nome: ')
time.sleep(1)
print ('\nOlá, {}'.format(nome))
time.sleep(1)
print ('\nSeja Bem-Vindo\n')
time.sleep(1)

while estado == True:
    resposta_final = pergunta()
    resposta()

pontuação()

for linha in pontu:
    print(linha)
