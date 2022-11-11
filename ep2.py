import time
from colorama import Fore
import random 
import funcoes 
import base_questoes

y = True
total = 0
print("Olá! Você está no Fortune DesSfot e terá a oportunidade de enriquecer!")
time.sleep(1.5)
nome = input("Qual seu nome? ")
time.sleep(1.5)
print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!")
time.sleep(1.5)
print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'! ")
time.sleep(1.5)
enter = input("Aperte ENTER para continuar...")
print("O jogo ja vai começar! Lá vem a primeira questão!")
print("Vamos começar com questões do nível FACIL!")
time.sleep(1.5)
enter = input("Aperte ENTER para continuar...")


print("-"*150)

contador = 0
num = 1
while y == True:
    transforma = funcoes.transforma_base(base_questoes.perguntas)
    if contador >= 0 and contador < 4:
        sorteada = funcoes.sorteia_questao(transforma,'facil')
    if contador >= 4 and contador < 7:
        sorteada = funcoes.sorteia_questao(transforma,'medio')
    if contador >= 7 and contador < 11:
        sorteada = funcoes.sorteia_questao(transforma,'dificil')
    print(funcoes.questao_para_texto(sorteada,num))
    num +=1 

    resposta = input("Qual sua resposta?") 

    resp = resposta.upper()
    if resp not in sorteada['opcoes']: 
        print(Fore.RED + "Opção inválida")
        print(Fore.BLUE + "AS opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'!")
        time.sleep(1.5) 
        resp = input(Fore.RESET + "Qual sua resposta?")
    if resp == sorteada['correta']:
        total += 1000
        print(Fore.GREEN + "Você acertou! Seu prêmio atual é de R${0}.00 :D".format(total) + Fore.RESET)
        time.sleep(1.5) 
        contador += 1
    if resp != sorteada['correta']: 
        print(Fore.RED + "Que pena! Você errou e vai sair sem nada :(" + Fore.RESET)
        time.sleep(1.5)
        break 
    if resp == "parar":
        parar = input(Fore.RESET + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(total))
        time.sleep(1.5)
        while parar != "S" or parar != "N":
            time.sleep(1.5) 
            print(Fore.RED + "Opção inválida")
            parar = input(Fore.RESET + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(total))
        if parar == "S":
            print("Ok! Você parou e seu prêmio é de R${0}.00".format(total))
            break             
    y == True 
    print("-"*100)