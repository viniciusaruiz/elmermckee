import time
from colorama import Fore
import random 
import funcoes 

y = True
total = 0
print("Olá! Você está no Fortune DesSfot e terá a oportunidade de enriquecer!")
time.sleep(1.5)
nome = input("Qual seu nome? ")
time.sleep(1.5)
print("Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!".format(nome))
time.sleep(1.5)
print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'! ")
time.sleep(1.5)
enter = input("Aperte ENTER para continuar...")
print("O jogo ja vai começar! Lá vem a primeira questão!")
print("Vamos começar com questões do nível FACIL!")
time.sleep(1.5)
enter = input("Aperte ENTER para continuar...")


print("-"*150)


perguntas = [{'titulo': 'Qual destas ferramentas é mais apropriada para cavar pregos em uma superfície?',
          'nivel': 'facil',
          'opcoes': {'A': 'Alicate', 'B': 'Martelo', 'C': 'Serrote', 'D': 'Lixadeira'},
          'correta': 'B'},

         {'titulo': 'Na alimentação vegetariana, qual desses alimentos não é consumido?',
          'nivel': 'facil',
          'opcoes': {'A': 'Carne', 'B': 'Abobrinha', 'C': 'Lentilha', 'D': 'Ervilha'},
          'correta': 'A'},

         {'titulo': 'Um ano é composto de quantos trimestres',
          'nivel': 'facil',
          'opcoes': {'A': '2', 'B': '3', 'C': '4', 'D': '6'},
          'correta': 'C'},

         {'titulo': 'Qual é o filhote da ovelha?',
          'nivel': 'facil',
          'opcoes': {'A': 'ovelha filho', 'B': 'cabrito', 'C': 'cordeiro', 'D': 'bode'},
          'correta': 'C'},

         {'titulo': 'Quando é celebrado o dia internacional da mulher?',
          'nivel': 'facil',
          'opcoes': {'A': '8 de março', 'B': '10 de setembro', 'C': '12 de abril', 'D': '20 de julho'},
          'correta': 'A'},

         {'titulo': 'Qual dessas obras não é de Leonardo da Vinci',
          'nivel': 'facil',
          'opcoes': {'A': 'Mona Lisa', 'B': 'Davi', 'C': 'A Última Ceia', 'D': 'Homem Vitruviano'},
          'correta': 'B'},
          
         {'titulo': 'Qual o volume ocupado por um gás na CNTP?',
          'nivel': 'facil',
          'opcoes': {'A': '21', 'B': '32L', 'C': '25L', 'D': '22,4L'},
          'correta': 'D'},

         {'titulo': 'Qual é o verdadeiro nome do Super-Homem?',
          'nivel': 'facil',
          'opcoes': {'A': 'Bruce Wayne', 'B': 'Clark Kent', 'C': 'Barry Allen', 'D': 'Oliver Queen'},
          'correta': 'B'},

         {'titulo': 'Qual é o livro mais vendido no mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Bíblia', 'B': 'Harry Potter', 'C': 'Dom Quixote', 'D': 'O Pequeno Príncipe'},
          'correta': 'A'},
          
         {'titulo': 'Complete o ditado: Galinha que canta...',
          'nivel': 'facil',
          'opcoes': {'A': 'canta sozinha', 'B': 'acorda os outros', 'C': 'da pintinho', 'D': 'bota o ovo'},
          'correta': 'D'},

         {'titulo': 'De quem é o álbum póstumo mais vendido de todos os tempos?',
          'nivel': 'facil',
          'opcoes': {'A': 'Avicci', 'B': 'Elvis Presley', 'C': 'Michael Jackson', 'D': 'Justin Bieber'},
          'correta': 'C'},

         {'titulo': 'Quantas pontas tem a estrela de Davi?',
          'nivel': 'facil',
          'opcoes': {'A': '7', 'B': '6', 'C': '8', 'D': '5'},
          'correta': 'B'},

         {'titulo': 'Se o pai to Padre é filho do meu pai, o que o Padre é meu?',
          'nivel': 'médio',
          'opcoes': {'A': 'Irmão', 'B': 'Tio', 'C': 'Primo', 'D': 'Sobrinho'},
          'correta': 'D'},

         {'titulo': 'No filme Aladdin, qual era o nome de seu macaco de estimação?',
          'nivel': 'médio',
          'opcoes': {'A': 'Mico', 'B': 'Babu', 'C': 'Rafiki', 'D': 'Abu'},
          'correta': 'D'},

         {'titulo': 'Quantas cores há no arco-írias?',
          'nivel': 'médio',
          'opcoes': {'A': '5', 'B': '6', 'C': '7', 'D': '8'},
          'correta': 'C'},

         {'titulo': 'Qual é o nome do estádio do Santos?',
          'nivel': 'médio',
          'opcoes': {'A': 'Vila Belmiro', 'B': 'Bruno Ramalho', 'C': 'Moisés Lucarelli', 'D': 'Brinco de Ouro da Princesa'},
          'correta': 'A'},

         {'titulo': 'Qual é o maior planeta do sistema solar?',
          'nivel': 'médio',
          'opcoes': {'A': 'Saturno', 'B': 'Júpiter', 'C': 'Marte', 'D': 'Plutão'},
          'correta': 'B'},

         {'titulo': 'Quais são as cinco cores dos anéis dos Jogos Olímpicos?',
          'nivel': 'médio',
          'opcoes': {'A': 'Azul, vermelho, amarelo, verde e preto', 'B': 'Azul, vermelho, amarelo, verde e violeta', 'C': 'Índigo, vermelho, roxo, verde e preto', 'D': 'Azul, vermelho, amarelo, laranja e verde'},
          'correta': 'A'},

         {'titulo': 'Qual classificação dada ao medicamento obtido exclusivamete da matéria-prima vegetal',
          'nivel': 'médio',
          'opcoes': {'A': 'Genérico', 'B': 'Fitoterápico', 'C': 'Homeopático', 'D': 'Alopático'},
          'correta': 'B'},

         {'titulo': 'Em qual destas regiões ficava o Quilombo dos Palmares, onde viveu Zumbi?',
          'nivel': 'difícil',
          'opcoes': {'A': 'Serra da Barriga, AL', 'B': 'Vale do Ribeira, SP', 'C': 'Riacho de Santana, BA', 'D': 'Boqueirão da Arara, CE'},
          'correta': 'A'},

         {'titulo': 'Quantos jogadores há em um time de beisebol?',
          'nivel': 'difícil',
          'opcoes': {'A': '10', 'B': '9', 'C': '8', 'D': '7'},
          'correta': 'B'},  

         {'titulo': 'Qual é o aumentativo de navio?',
          'nivel': 'difícil',
          'opcoes': {'A': 'Não existe', 'B': 'Navião', 'C': 'Grande navio', 'D': 'Naviarra'},
          'correta': 'D'}]




#FACIL
while y == True:
    sorteada = random.choice(perguntas)
    print(sorteada)

    resp = input("Qual sua resposta?") 
    #if resp not in sorteada['opções']: 
    #    print(Fore.RED + "Opção inválida")
    #    print(Fore.BLUE + "AS opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula e 'parar'!")
    #    time.sleep(1.5) 
    #    resp = input(Fore.RESET + "Qual sua resposta?")
    if resp == sorteada['correta']:
        total += 1000
        print(Fore.GREEN + "Você acertou! Seu prêmio atual é de R${0}.00 :D".format(total) + Fore.RESET)
    if resp != sorteada['correta']:
        print(Fore.RED + "Que pena! Você errou e vai sair sem nada :(" + Fore.RESET)
        break 
    if resp == "parar":
        parar = input(Fore.RESET + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(total))
        while parar != "S" or parar != "N":
            print(Fore.RED + "Opção inválida")
            parar = input(Fore.RESET + "Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(total))
        if parar == "S":
            print("Ok! Você parou e seu prêmio é de R${0}.00".format(total))
            break             
    y == True 
    print("-"*150)