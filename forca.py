# adivinhacao.py

#Biblioteca de Regex
import re

#Função que contém o jogo.
def jogar():

    mensagem_inicial()

    pattern1 = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$"

    while True:
        linha_vazia()
        palavra_secreta = str(input('Qual é a palavra secreta? ').strip())
    
        linha_vazia()
        palavra_secreta = palavra_secreta.lower()

        if (re.search(pattern1, palavra_secreta)):
            break

        else:
            print('Palavra secreta invalida, por favor, tente novamente!')

    #Variável para guarda a palavra secreta, para depois ser substituido as letras acentuadas e o Cedilha.
    palavra_secreta_corrigida = palavra_secreta

    #Dicionário que guarda, como chave, uma letra acentuada e cedilha; como valor, a letra não acentuada ou o C.
    letras ={
        'á' : 'a',
        'à' : 'a',
        'â' : 'a',
        'ã' : 'a',
        'é' : 'e',
        "è" : 'e',
        "ê" : 'e',
        'í' : 'i',
        'ï' : 'i',
        'ó' : 'o',
        'ô' : 'o',
        'õ' : 'o',
        'ö' : 'o',
        'ú' : 'u',
        'ñ' : 'n',
        "Á" : 'A',
        'À' : 'A',
        "Â" : 'A',
        "Ã" : 'A',
        'É' : 'E',
        'È' : 'E',
        'Í' : 'I',
        'Ï' : 'I',
        'Ó' : 'O',
        'Ô' : 'O',
        'Õ' : 'O',
        'Ö' : 'O',
        'Ú' : 'U',
        'Ñ' : 'N',
        'ç' : 'c',
        'Ç' : 'C',
    }

    chaves = letras.keys()

    tamanho2 = len(palavra_secreta_corrigida)

    palavra_secreta_corrigida =  substituir_letras(chaves,palavra_secreta_corrigida,letras,tamanho2)

    #Lista para demonstrar o processo de complemento da palavra secreta para o jogador adivinhador.
    palavra = ["_" for i in palavra_secreta_corrigida]

    #Lista para guarda letras já respondidas.
    letras_respondidas = []

    #Variavel booleana para fazer o jogo continuar indeterminadamente até o jogador ganhar ou peder.
    caso_continuar_jogo = True

    #Para printar, com _, a palavra secreta.
    linha_vazia()
    print(*palavra)
    linha_vazia()
    
    #Loop para adivinhação.
    while caso_continuar_jogo:
        
        #Loop para entrada de palpite de Letra + Regex de verificação.
        while True:     
            chute = str(input('Qual letra? ').strip())

            #Variável que guarda o palpite em minúsculo.
            chute_minusculo = chute.lower()

            #Variável que guarda o palpite em maiúsculo.
            chute_maiusculo = chute.upper()
            linha_vazia()

            #Pattern de verficação de palpite de letra.
            pattern2 = "^[A-Za-z ]{1}$"

            #Condicional de se o palpite foi Válido ou não.
            '''
            Essa validação confere se a entrada da variável chute foi válida, conforme o pattern2.
            Além disso, verifica se o palpite fora tentado anteriomente. Por isso, existe o condicional dentr
            '''

            if (re.search(pattern2, chute)):
                if (letras_respondidas.count(chute_maiusculo) == 0):
                    letras_respondidas.append(chute_maiusculo)
                    break
                    
                else:
                    print('Palpite invalido, essa letra já foi escolhida. Por favor, tente novamente!')
                    linha_vazia()
            else:
                print('Palpite invalido, por favor, tente novamente!')
                linha_vazia()


                

        #Variável para passar por cada caractere da lista palavra.
        index = 0

        #Para substituir, caso o palpite seja correto, o '_' pela letra.

        palavra = substituir_palpite_correto(index,palavra_secreta_corrigida,chute_minusculo,palavra)
  

        escrever_letras_respondidas(palavra,letras_respondidas)

        #Para os casos que o jogador acertar sem a necessidade de pedir um palpite de palavra secreta.
        #Baseado na ideia que caso não existir mais o _, irá apresentar erro, com isso, entrará no except.
        try:    
            condicao = palavra.index('_')

        except:
            ganhou()
            caso_continuar_jogo = False


        #Var para verificar quantas letras ainda faltam serem descobertas.
        letras_restante = palavra.count('_')

        '''
        Condicional para verificar se ainda há mais que 3 letras para serem descobertas. Com isso, caso falte serem
        descobertas 3 letras ou menos, o jogo pedirá, ao jogador, um palpite de qual seria a palavra secreta.
        '''
        if (0 < letras_restante <= 3):

            #Loop para garantir que o palpite de palavra secreta seja válido.
            while True:
                resposta = str(input('Qual é a palavra secreta? ').strip())
                print("")

                #O pattern é o mesmo que usado para a entrada da variável palavra_secreta.
                if (re.search(pattern1, resposta)):
                    break
                else:
                    print('Palpite invalido, por favor, tente novamente!')


            #para passar a resposta para minusculo
            resposta_corrigida = resposta.lower()

            #Comprimento da resposta_corrigida
            tamanho2 = len(resposta_corrigida)

            resposta_corrigida = substituir_letras(chaves,resposta_corrigida,letras,tamanho2)

            acertou_resposta = resposta_corrigida.lower() == palavra_secreta_corrigida.lower()

            if (acertou_resposta):

                #Para charmar a função ganhou().
                ganhou(palavra_secreta)
                caso_continuar_jogo = False
            else:
                #Para charmar a função perdeu.().
                perdeu(palavra_secreta)
                caso_continuar_jogo = False


#Função que imprime uma linha vazia.
def linha_vazia():
    print('')

def mensagem_inicial():
    print("*******************************")
    print("**Bem vindo ao jogo da Forca!**")
    print("*******************************")

def substituir_letras(chaves,palavra_secreta_corrigida,letras, tamanho):
    for i in chaves:

        #O value é do 0 ao tamanho da var palavra_secreta_corrigida.
        for value in range(0,tamanho):

        #Verificar se alguma letra detém acento.
            if (palavra_secreta_corrigida[value] == i):
                palavra_secreta_corrigida = palavra_secreta_corrigida.replace(palavra_secreta_corrigida[value],letras[i])
    return palavra_secreta_corrigida


    #Função para caso o jogador adivinhador ganhar.
def ganhou(palavra_secreta):
    print("A palavra secreta é:",palavra_secreta.upper(), end='!\n')
    linha_vazia()
    print("Parabéns, você ganhou!")
    print('Fim do Jogo.')

    #Função para caso o jogador adivinhador perder.
def perdeu(palavra_secreta):
    print('Que azar, você perdeu!')
    linha_vazia()
    print("A palavra secreta era",palavra_secreta.upper(),end='!\n')
    print('Fim do Jogo.')

def substituir_palpite_correto(index,palavra_secreta_corrigida,chute_minusculo,palavra):
    for letra in palavra_secreta_corrigida.lower():
        if (chute_minusculo == letra):
            palavra[index] = palavra_secreta_corrigida[index].upper()
        index += 1  

    return palavra
def escrever_letras_respondidas(palavra,letras_respondidas):
    #Para printar as letras que ainda não e quais já foram tentadas.
    print(*palavra)
    print("")
    print('letras Respondidas:',*letras_respondidas)
    print("")

    #Avisar quantas letras faltam serem adivinhadas.
    print('Faltam',palavra.count('_'), 'letras!')
    print("")    


if (__name__ == "__main__"):
    jogar()