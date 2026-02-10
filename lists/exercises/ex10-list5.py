def cria_gabarito():
    #pode colocar isso dentro de um while com len(L) < 5 para garantir que o usuário só pode sair quando me der as 5 respostas do gabarito
    L = list()
    L = input("Entre com a lista de gabarito (A, C, B...): ").split(",")
    return(L) #gabarito

def pega_dados_individuais ():

    aluno = input("Qual o nome do aluno? ")
    respostas = input("Entre com a lista de respostas dele (A, B, C...): ").split(",")
    return(aluno, respostas)

def verifica_respostas (aluno, respostas, gabarito):

    acertos = 0
    for i in range(len(respostas)):
        if respostas[i] == gabarito[i]:
            acertos += 1
    
    return(acertos)

def declara_nota (aluno, acertos):

    print(f"O aluno {aluno} acertou {acertos} questões e teve {acertos*2} de nota.")
'''
def main(): #SE QUISER QUE ELE DECLARE A NOTA LOGO APÓS VC DIZER QUEM É O ALUNO

    gabarito = cria_gabarito()

    for k in range(15):
        
        aluno, respostas = pega_dados_individuais()
        acertos = verifica_respostas(aluno, respostas, gabarito)
        declara_nota(aluno, acertos)
'''
def main(): #SE QUISER QUE ELE DECLARE A NOTA AO FINAL E EM FORMATO DE LISTA
    gabarito = cria_gabarito()
    n = []
    for k in range(2):

        aluno, respostas = pega_dados_individuais()
        acertos = verifica_respostas(aluno, respostas, gabarito)
        n += [f"O {aluno} acertou {acertos} questões e teve {acertos*2} de nota."]
    print(n)

    
main()