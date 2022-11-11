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

