import sqlite3

save = sqlite3.connect("Data_Base.db")

geral_list = list()
turmas = list()
notas = ['ap1', 'ap2', 'ab']
aluno_notas = list()
temp_data = list()
med_min = 7.0
done = False
on = False
s = 0
no_turm = 0


print('''-=-=-=-=- Gerenciador de Alunos -=-=-=-=-
Programado por KevBoyz >>> Versão  2.3
''')

while True:
    print('''Menu de opções:
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
[1] Conferir lista de alunos    |
[2] Alunos sem turma            |
[3] Cadastrar novo aluno        |
[4] Cadastrar nova turma        |
[5] Configurações do programa   |
[6] Atribuir notas para alunos  |
[7] Conferir notas de alunos    |
[8] editar configurações do aluno''')
    inpt = int(input('>>> '))
    print()
    done = False

    if inpt < 0 or inpt == 0 or inpt > 8 or inpt == 8:
        print('Operação inválida')
        print()
    elif inpt == 1:
        if len(geral_list) == 0:
            print('Nenhum aluno cadastrado...')
            print()
        elif len(geral_list) > 0 and len(turmas) == 0:
            print('Nenhuma Turma cadastrada...')
            print('Se você tiver excluido alguma turma, cheque os alunos sem turma na opção [2]')
            print()
        else:
            for c in range(0, len(turmas)):
                print(f'''Informações Gerais:

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Alunos Cadastrados: {len(geral_list)}
Alunos com notas atribuiidas: {len(aluno_notas)} -> {(len(geral_list) * len(aluno_notas))/100}% do total
Turmas cadastradas: {len(turmas)}
Alunos sem turma: {no_turm} -> {(len(geral_list) * no_turm)/100}% do total
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
                print(f'-=-=-=- Alunos cadastrados na turma: {turmas[c]} -=-=-=-')
                for aluno in geral_list:
                    if aluno[2] == turmas[c]:
                        print(f'Nome: {aluno[0]:<20} | Data de nascimento: {aluno[1]}')
                print()

    elif inpt == 2:
        print('=== === Alunos sem Turma === ===')
        print('Para cadastrar alunos em turmas va em configurações do aluno')
        print()

        for aluno in geral_list:
            if aluno[2] == 'Aluno sem Turma':
                print(f'Nome: {aluno[0]:<20} | Data de nascimento: {aluno[1]}')

    elif inpt == 3:
        if len(turmas) == 0:
            print('Antes de cadastrar alunos, cadastre primeiro uma turma')
            print()
        else:
            print(''' === Cadastramento de Alunos ===''')
            loop = int(input('Quantos alunos você quer cadastar? '))
            if loop == 0 or 0 > loop:
                print('Número invalido')
            else:
                print(f'Ok! Informe os dados dos {loop} alunos' if loop > 1 else 'Ok! Informe os dados do aluno' )
                print('-=-'*10)
                print()
                for c in range(0, loop):
                    print(f'-=-=-=- Aluno {c+1} -=-=-=-')
                    temp_data.append(str(input(f'Nome do aluno {c+1}: ')))
                    temp_data.append(str(input(f'Data de nascimento de {temp_data[0]}: ')))
                    print('Turmas disponiveis: ', end='')
                    for turma in turmas:
                        print(f'{turma}', end='')
                    aluno_turma = (str(input('\nEm qual turma o aluno será cadastrado: ')))
                    if aluno_turma not in turmas:
                        print('Turma não encontrada')
                        aluno_turma = (str(input('\nEm qual turma o aluno será cadastrado: ')))
                    print()
                    temp_data.append(aluno_turma)
                    geral_list.append(temp_data[:])
                    print('Visão prévia:')
                    print(f'Nome: {temp_data[0]:<20} | Data de nascimento: {temp_data[1]}')
                    print(f'Aluno {c+1} castrado com sucesso')
                    print()
                    temp_data.clear()

    elif inpt == 4:
        print('=-=-= Cadastramento de turmas =-=-=')
        name = str(input('Digite um nome para sua turma: ')).capitalize().strip()
        turmas.append(name)
        print('''Turma criada com Sucesso!
        ''')

    elif inpt == 5:
        while True:
            print('''
=== Configurações do Programa ===
            
[1] Deletar turmas
[2] Deletar alunos
[3] Mofificar nota mínima para aprovção
[4] Limpar dados
[5] Configuração de notas
[6] Voltar ao programa
''')
            inpt = int(input('>>> '))

            if inpt == 1:
                if len(turmas) == 0:
                    print('Nenhuma turma encontrada')
                    print()
                else:
                    print('Turmas disponiveis: ', end='')
                    for turma in turmas:
                        print(f'{turma}', end=' ')
                    del_item = str(input('\nDigite o nome da turma a ser deletada: '))
                    if del_item not in turmas:
                        print('Turma não encontrada')
                        del_item = int(input('Digite o nome da turma a ser deletada: '))
                    elif del_item in turmas:
                        turmas.remove(del_item)
                        for aluno in geral_list:
                            if aluno[2] == del_item:
                                aluno[2] = 'Aluno sem Turma'
                                no_turm += 1

                        print(f'Turma {del_item} excluida')
                        print()
            elif inpt == 2:
                if len(geral_list) == 0:
                    print('Nenhum aluno encontrado')
                else:
                    name = str(input('Digite o nome do aluno a ser deletado: '))
                    if name not in geral_list:
                        print('Aluno não encontrado')
                        name = str(input('Digite o nome do aluno a ser deletado: '))
                    elif name in geral_list:
                        for aluno in geral_list:
                            if aluno[0] == name:
                                geral_list.remove(aluno[2])
                                geral_list.remove(aluno[1])
                                geral_list.remove(aluno[0])
                                print('Concluido com exito')
                                print()
            elif inpt == 3:
                print('A nota minima é a quantidade minima de pontos que o aluno deve ter para ser aprovado')
                print('Por padrão a nota é 7.0 na média')
                print()
                go = str(input('Você deseja alterar esse valor? (S/N) ')).lower()[0]
                if go[0] == 's':
                    med_min = float(input('Digite o valor a ser atribuido: '))
                    if med_min == 0 or 0 > med_min:
                        print('Valor inválido')
                        med_min = float(input('Digite o valor a ser atribuido: '))
                    else:
                        print('Concluido com exito')
                else:
                    print('Operação cancelada')
                    print()



            elif inpt == 4:
                print('Se esta operação for realizada, todos os dados serão excluidos')
                go = str(input('Você tem certeza que quer fazer isso? (S/N) ')).lower()[0]
                if go[0] == 's':
                    print('Concluido com exito')
                    print()
                    geral_list.clear()
                    turmas.clear()
                else:
                    print('Processo Cancelado')

            elif inpt == 5:

                print(' === Configuração para sistema de notas === ')
                print('''
Por padrão o aluno tem 3 notas para a média final (ap1), (ap2), (ab)''')
                go = str(input('Você mudar o nome das notas? (S/N)')).lower()[0]
                if go[0] == 's':
                    for c in range(0, len(notas)):
                        new_name = str(input(f'Novo nome para a {notas[0]}, {c+1}* nota: '))
                        if len(new_name) > 5 or '!/|:;,*@#%$()?=-+.' in new_name:
                            print('Erro! O nome d nota só pode conter no maximo 5 caracteres e não pode conter')
                            print('Os simbolos: !/|:;,*@#%$()?=-+.  Tente um nome mais simples')
                            new_name = str(input(f'Novo nome para a {notas[0]}'))
                        else:
                            if new_name in notas:
                                print('Já existe uma nota com esse nome, tente algo diferente')
                                new_name = str(input(f'Novo nome para a {notas[0]}'))
                            else:
                                print(f'Nome aceito!, a nota {notas[c]} agora se chama {new_name}')
                                notas[c] = new_name


            elif inpt == 6:
                break
                print()


    elif inpt == 6:
        if len(geral_list) == 0:
            print('Nenhum aluno cadastrado...')
        else:
            print(' === Atribuir notas === ')
            done = False
            while True:
                print('''
Método de atribuição
[1] A um aluno específico
[3] Voltar ao programa''')
                inpt = int(input('>>> '))
                if inpt > 3 or 0 > inpt or inpt == 0:
                    print('Numero invalido')
                    print()
                else:
                    if inpt == 1:
                        name = str(input('Digite o nome do aluno '))
                        for aluno in geral_list:
                            if aluno[0] == name:
                                print('Dados do aluno:')
                                print(f'Nome: {aluno[0]:<20} | Data de nascimento: {aluno[1]} | Cadastrado na turma {aluno[2]}')
                                print()
                                for aluno in geral_list:
                                    if aluno[0] == name:
                                        done = True
                                if done:
                                    print('O aluno ainda não tem nenhuma nota atribuida...')
                                    print('Iniciando laço para adição das tres notas')
                                    print()
                                    temp_data.append(aluno[0])
                                    temp_data.append(aluno[2])
                                    for c in range(0, 3):
                                        temp_data.append(float(input(f'Nota para {notas[c]} do aluno: ')))
                                    aluno_notas.append(temp_data[:])
                                    temp_data.clear()
                                    print('Notas registradas')
                                    print()


                    elif inpt == 3:
                        break
                        print()

    elif inpt == 7:
        if len(aluno_notas) == 0:
            print('Você não atribuiu nota a nenhum aluno')
            print()
        else:
            print('= = === Boletim Dos Estudantes === = =')
            print('Está lista contem apenas os alunos que tiveram notas atribuidas')
            print()
            for c in range(0, len(turmas)):
                print(f'-=-=-=-=- Turma: {turmas[c]} -=-=-=-=-')
                print()
                for aluno in aluno_notas:
                    if aluno[1] == turmas[c]:
                        calc = (aluno[2] + aluno[3] + aluno[4])
                        print(f'Nome: {aluno[0]} |Notas-> {notas[0]} = {aluno[2]} | {notas[1]} = {aluno[3]} | {notas[2]} = {aluno[4]}')
                        if calc >= med_min * 3:
                            print(f'Aluno {aluno[0]} foi Aprovado')
                            print()
                        else:
                            print(f'Aluno {aluno[0]} foi Reprovado ')
                            temp_data.append(aluno[0])
                            print()
                print('-=-=-=- Alunos Reprovados -=-=-=-')
                if len(temp_data) == 0:
                    print('Nenhum aluno reprovou')
                else:
                    for c in temp_data:
                        print(c)

    elif inpt == 8:
        if len(geral_list) == 0 or len(turmas) == 0:
            print('Você ainda não possui alunos cadastrados')
            print()
        else:
            print('=== Configurações do aluno ===')
            print()
            name = str(input('Digite o nome do aluno '))
            for aluno in geral_list:
                if aluno[0] == name:
                    done = True
                if done:
                    print('... Aluno encontrado!')
                    print('-=-'*20)
                    for aluno in geral_list:
                        if aluno[0] == name:
                            print('Dados atuais do aluno:')
                            print(f'Nome: {aluno[0]:<20} | Data de nascimento: {aluno[1]}')
                            print('-=-'*20)
                    while True:
                        print('''Selecione o processo desejado;
[1] Trocar nome do aluno
[2] Trocar data de nascimento 
[3] Mudar aluno de turma
[4] Alterar notas do aluno
[5] Voltar ao programa''')
                        inpt = int(input('>>> '))
                        if inpt == 1:
                            new_name = str(input('Digite um novo nome: '))
                            for aluno in geral_list:
                                if aluno[0] == name:
                                    aluno[0] = new_name
                            print('Concluido com exito')
                            print()
                        elif inpt == 2:
                            new_age = str(input('Nova data de nascimento: '))
                            for aluno in geral_list:
                                if aluno[0] == name:
                                    aluno[1] = new_age
                            print('Concluido com exito')
                            print()
                        elif inpt == 3:
                            name = str(input('Nome do aluno a ser mudado de turma: '))
                            for aluno in geral_list:
                                if aluno[0] == name:
                                    done = True
                                if done:
                                    while done:
                                        print('Aluno não encontrado...')
                                        name = str(input('Nome do aluno a ser mudado de turma: '))
                                        for aluno in geral_list:
                                            if aluno[0] == name:
                                                done = True
                                else:
                                    for aluno in geral_list:
                                        if aluno[0] == name:
                                            print('Turmas disponíveis: ', end='')
                                            for turma in turmas:
                                                print(turma, end=', ')
                                            new_turm = str(input('Selecione uma nova turma para o aluno: '))
                                            if new_turm not in turmas:
                                                print('Turma não encontrada...')
                                                new_turm = str(input('Selecione uma nova turma para o aluno: '))
                                            else:
                                                aluno[2] = new_turm
                                    print('Concluido com exito')
                                    print()

                        elif inpt == 4:
                            if len(aluno_notas) == 0:
                                print('Você não atribuiu nota para nehum aluno')
                                print()
                            else:
                                print('-=-'*10)
                                print('=== Alteração de notas ===')
                                while True:
                                    for aluno in aluno_notas:
                                        if aluno[0] == name:
                                            print(f'''Qual nota do aluno você deseja alterar?
[1] {notas[0]}
[2] {notas[1]}
[3] {notas[2]}
[4] Voltar ao programa''')
                                            inpt = int(input('>>> '))

                                            if inpt == 1 or 2 or 3:
                                                print(f'Aluno: {aluno[0]}')
                                                print('Digite uma nova nota para a', end='')
                                            if inpt == 1:
                                                print(f'{notas[0]}', end='')
                                                new_points = float(input('>>> '))
                                                if new_points > 10:
                                                    print('A nota maxima é 10')
                                                    new_points = float(input('>>> '))
                                                else:
                                                    aluno[2] = new_points
                                                print('Nota modificada com sucesso!')
                                            elif inpt == 2:
                                                print(f'{notas[1]}', end='')
                                                new_points = float(input('>>> '))
                                                if new_points > 10:
                                                    print('A nota maxima é 10')
                                                    new_points = float(input('>>> '))
                                                else:
                                                    aluno[3] = new_points
                                                    print('Nota modificada com sucesso!')
                                            elif inpt == 3:
                                                print(f'{notas[2]}', end='')
                                                new_points = float(input('>>> '))
                                                if new_points > 10:
                                                    print('A nota maxima é 10')
                                                    new_points = float(input('>>> '))
                                                else:
                                                    aluno[4] = new_points
                                                    print('Nota modificada com sucesso!')
                                            elif inpt == 4:
                                                print('Saindo do configurador...')
                                                break