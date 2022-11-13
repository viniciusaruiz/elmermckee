import random
import time
from colorama import Fore
import base_questoes
import funcoes
while True:
    premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    y = True
    total = 0
    print(Fore.MAGENTA + "Olá! Você está no Fortune DesSfot e terá a oportunidade de enriquecer!" + Fore.RESET)
    time.sleep(1.5)
    nome = input("Qual seu nome?")
    time.sleep(1.5)
    print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!")
    time.sleep(1.5)
    print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'! ")
    time.sleep(1.5)
    enter = input("Aperte ENTER para continuar...\n")
    print("O jogo ja vai começar! Lá vem a primeira questão!")
    print("Vamos começar com questões do nível" + Fore.YELLOW + " FACIL!" + Fore.RESET)
    time.sleep(1.5)
    enter = input("Aperte ENTER para continuar...")


    print("-"*75)

    contador = 0
    num = 1
    lista_sorteada = []
    pulo = 3
    ajudas = 2
    while y == True:
        transforma = funcoes.transforma_base(base_questoes.perguntas)
        if contador >= 0 and contador < 4:
            sorteada = funcoes.sorteia_questao_inedita(transforma,'facil',lista_sorteada)
        if contador >= 4 and contador < 7:
            sorteada = funcoes.sorteia_questao_inedita(transforma,'medio',lista_sorteada)
        if contador >= 7 and contador < 11:
            sorteada = funcoes.sorteia_questao_inedita(transforma,'dificil',lista_sorteada)
        if num == 4:
                print("\nHEY! Você passou para o nível" + Fore.YELLOW + "MÉDIO!" + Fore.RESET)
        if num == 7:
                print("\nHEY! Você passou para o nível" + Fore.YELLOW + "DIFÍCIL!" + Fore.RESET)
        print(funcoes.questao_para_texto(sorteada,num))

        resposta = input("Qual sua resposta?") 

        resp = resposta.upper()
        while resp not in sorteada['opcoes'] and resp != "AJUDA" and resp != "PARAR" and resp != 'PULAR': 
            print(Fore.RED + "Opção inválida")
            print(Fore.BLUE + "AS opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'!" + Fore.RESET)
            time.sleep(1.5) 
            resp = input("Qual sua resposta?").upper()

        if resp == "PARAR":
            stop = input(Fore.YELLOW + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(premios[contador - 1]) + Fore.RESET)
            parar = stop.upper()
            time.sleep(1.5)
            while parar != "S" and parar != "N":
                print(Fore.RED + "Opção inválida")
                parar = input(Fore.RESET + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(premios[contador- 1]))
            if parar == "S":
                print("Ok! Você parou e seu prêmio é de R${0}.00".format(premios[contador-1]))
                break           
            if parar == "N":
                print(funcoes.questao_para_texto(sorteada,num))
                resposta = input("Qual sua resposta?") 
                resp = resposta.upper()
                
        if resp == 'PULAR':
            time.sleep(1.5)
            while pulo > 0:
                if pulo != 1:
                    print(Fore.CYAN + f"\nOk, pulando! Você ainda tem {pulo - 1} pulos!" + Fore.RESET)
                    enter = input("Aperte ENTER para continuar...\n")
                if contador >= 0 and contador < 4:
                    sorteada = funcoes.sorteia_questao_inedita(transforma,'facil',lista_sorteada)
                if contador >= 4 and contador < 7:
                    sorteada = funcoes.sorteia_questao_inedita(transforma,'medio',lista_sorteada)
                if contador >= 7 and contador < 11:
                    sorteada = funcoes.sorteia_questao_inedita(transforma,'dificil',lista_sorteada)
                print(funcoes.questao_para_texto(sorteada,num))
                resposta = input("Qual sua resposta?") 
                resp = resposta.upper()
                pulo -= 1
                if pulo == 1:
                    print(Fore.CYAN + f"\nOk, pulando! ATENÇÃO: Você não tem mais direito a pulos!" + Fore.RESET)
                    enter = input("Aperte ENTER para continuar...\n")
                while resp == 'PULAR' and pulo == 0:
                    print(Fore.CYAN + f"\nVocê não tem mais direito a pulos!" + Fore.RESET)
                    resposta = input("Qual sua resposta?") 
                    resp = resposta.upper()
                if resp != 'PULAR':
                    break
                
                
        
        if resp == "AJUDA":
            time.sleep(1.5)
            if ajudas > 1:
                print(Fore.CYAN + f"\nOk,lá vem ajuda! Você ainda tem {ajudas - 1} ajudas!" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...\n")
                print(funcoes.gera_ajuda(sorteada))
                enter = input("Aperte ENTER para continuar...\n")
                print(funcoes.questao_para_texto(sorteada,num))
                resposta = input("Qual sua resposta?") 
                resp = resposta.upper()
                while resp == "AJUDA":
                    print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                    enter = input("Aperte ENTER para continuar...")
                    resposta = input("Qual sua resposta?") 
                    resp = resposta.upper()

            if ajudas == 1:
                print(Fore.YELLOW + f"Ok,lá vem ajuda! ATENÇÃO: você não tem mais direito a ajudas!" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...\n")
                print(funcoes.gera_ajuda(sorteada))
                enter = input("Aperte ENTER para continuar...\n")
                print(funcoes.questao_para_texto(sorteada,num))
                resposta = input("Qual sua resposta?") 
                resp = resposta.upper()
                while resp == "AJUDA":
                    print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                    enter = input("Aperte ENTER para continuar...")
                    resposta = input("Qual sua resposta?") 
                    resp = resposta.upper()

            if ajudas == 0:
                print(Fore.RED + f"Não deu! Você não tem mais direito a ajudas!" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...\n")
                print(funcoes.questao_para_texto(sorteada,num))
                resposta = input("Qual sua resposta?") 
                resp = resposta.upper()
                while resp == "AJUDA":
                    print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                    enter = input("Aperte ENTER para continuar...")
                    resposta = input("Qual sua resposta?") 
                    resp = resposta.upper()

            ajudas = ajudas - 1 

        if resp == sorteada['correta']:
            print(Fore.GREEN + "Você acertou! Seu prêmio atual é de R${0}.00 :D".format(premios[contador]) + Fore.RESET)
            time.sleep(1.5) 
            contador += 1
        if resp != sorteada['correta']: 
            print(Fore.RED + "Que pena! Você errou e vai sair sem nada :(" + Fore.RESET)
            time.sleep(1.5)
            break 
        if contador == 9:
            print(Fore.GREEN + "PARABÉNS, você zerou o jogo e ganhou um milhão de reais!" + Fore.RESET)
            break
        num +=1 
        y == True 
        print("-"*75)
    novo = input('Aperte ENTER para jogar novamente!')
    