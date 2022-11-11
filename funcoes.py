def transforma_base(lista):
    dificuldade = {'facil': [], 'medio': [], 'dificil':[]}
    i = 0
    if lista == []:
        return {}
    for i in range(0,len(lista)):
        if lista[i]['nivel'] == 'facil':
            dificuldade['facil'].append(lista[i])
        if lista[i]['nivel'] == 'medio':
            dificuldade['medio'].append(lista[i])
        if lista[i]['nivel'] == 'dificil':
            dificuldade['dificil'].append(lista[i])
    if dificuldade['facil'] == []:
        del dificuldade['facil']
    if dificuldade['medio'] == []:
        del dificuldade['medio']
    if dificuldade['dificil'] == []:
        del dificuldade['dificil']
    return dificuldade

def valida_questao(questao):
    retorno = {}
    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao:
        retorno['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao:
        retorno['opcoes'] = 'nao_encontrado'   
    if 'correta' not in questao:
        retorno['correta'] = 'nao_encontrado'
    if len(questao) != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    if 'titulo' in questao:
        if questao['titulo'] == '' or questao['titulo'].strip() == '':
            retorno['titulo']= 'vazio'
    if 'nivel' in questao:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            retorno['nivel'] = 'valor_errado'
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        if len(questao['opcoes']) == 4:
            if 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
                retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                novo = {}
                if questao['opcoes']['A'].strip() == '':
                    novo['A'] = 'vazia'
                if questao['opcoes']['B'].strip() == '':
                    novo['B'] = 'vazia'
                if questao['opcoes']['C'].strip() == '':
                    novo['C'] = 'vazia'
                if questao['opcoes']['D'].strip() == '':
                    novo['D'] = 'vazia'
                if novo != {}:
                    retorno['opcoes'] = novo
    if 'correta' in questao:
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            retorno['correta'] = 'valor_errado'
    return retorno      

def valida_questoes(lista):
    lista_questoes = []
    for questao in lista:
        lista_questoes.append(valida_questao(questao))
    return lista_questoes

import random 
def sorteia_questao(dic,nivel):
    dicionario = dic[nivel]
    x = random.choice(dicionario)
    return x

def sorteia_questao_inedita(dicionario,nivel,lista):
    x = sorteia_questao(dicionario,nivel)
    while x in lista:
        x = sorteia_questao(dicionario,nivel)
    lista.append(x)
    return x


def questao_para_texto(dicionario,n):
    x = f'''----------------------------------------
QUESTAO {n}

{dicionario['titulo']}

RESPOSTAS:
A: {dicionario['opcoes']['A']}
B: {dicionario['opcoes']['B']}
C: {dicionario['opcoes']['C']}
D: {dicionario['opcoes']['D']}'''
    return x

import random
def gera_ajuda(dicionario):
    certa = dicionario['certa']
    lista = [dicionario['opcoes']['A'],dicionario['opcoes']['B'],dicionario['opcoes']['C'],dicionario['opcoes']['D']]
    y = lista.index(dicionario['opcoes'][certa])
    del lista[y]
    x = random.randint(1,2)
    if x == 1:
        z = random.choice(lista)
        return f'DICA:\nOpções certamente erradas: {z}'
    if x == 2:
        z = random.choice(lista)
        y = lista.index(z)
        del lista[y]
        a = random.choice(lista)
        return f'DICA:\nOpções certamente erradas: {z} | {a}'