import random
import time
from colorama import Fore
import base_questoes
import funcoes

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
    while resp not in sorteada['opcoes'] and resp != "AJUDA" and resp != "PARAR": 
        print(Fore.RED + "Opção inválida")
        print(Fore.BLUE + "AS opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'!" + Fore.RESET)
        time.sleep(1.5) 
        resp = input("Qual sua resposta?").upper()

    
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
            if resp == "AJUDA":
                print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...")

        if ajudas == 1:
            print(Fore.YELLOW + f"Ok,á vem ajuda! ATENÇÃO: você não tem mais direito a ajudas!" + Fore.RESET)
            enter = input("Aperte ENTER para continuar...\n")
            print(funcoes.gera_ajuda(sorteada))
            enter = input("Aperte ENTER para continuar...\n")
            print(funcoes.questao_para_texto(sorteada,num))
            resposta = input("Qual sua resposta?") 
            resp = resposta.upper()
            if resp == "AJUDA":
                print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...")

        if ajudas == 0:
            print(Fore.RED + f"Não deu! Você não tem mais direito a ajudas!" + Fore.RESET)
            enter = input("Aperte ENTER para continuar...\n")
            print(funcoes.questao_para_texto(sorteada,num))
            resposta = input("Qual sua resposta?") 
            resp = resposta.upper()
            if resp == "AJUDA":
                print(Fore.RED + "Não deu! Você já pediu ajuda nessa questão" + Fore.RESET)
                enter = input("Aperte ENTER para continuar...")

        ajudas = ajudas - 1 

    if resp == sorteada['correta']:
        print(Fore.GREEN + "Você acertou! Seu prêmio atual é de R${0}.00 :D".format(premios[contador]) + Fore.RESET)
        time.sleep(1.5) 
        contador += 1
    if resp != sorteada['correta']: 
        print(Fore.RED + "Que pena! Você errou e vai sair sem nada :(" + Fore.RESET)
        time.sleep(1.5)
        break 

    num +=1 
    y == True 
    print("-"*75)