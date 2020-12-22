geral_list = list()
turmas = list()
temp_data = list()
done = False
s = 0

print('''-=-=-=-=- Gerenciador de Alunos -=-=-=-=-
Programado por KevBoyz >>> Versão   1.4
''')


while True:
    print('''Menu de opções:
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_/ /
[1] Conferir lista de alunos    |
[2] Cadastrar novo aluno        |
[3] Cadastrar nova turma        |
[4] Configurações do programa   |
[5] editar configurações do aluno''')
    inpt = int(input('>>> '))
    print()
    done = False

    if inpt < 0 or inpt == 0 or inpt > 5 or inpt == 5:
        print('Operação inválida')
        print()
    elif inpt == 1:
        if len(geral_list) == 0:
            print('Nenhum aluno cadastrado...')
            print()
        else:
            s = 0
            for c in range(0, len(turmas)):
                print(f'-=-=-=- Alunos cadastrados na turma: {turmas[c]} -=-=-=-')
                for aluno in geral_list:
                    if aluno[2] == turmas[c]:
                        print(f'{s + 1}Nome: {aluno[0]:<20} | Data de nascimento: {aluno[1]}')
                s = 0
                print()
    elif inpt == 2:
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
                for c in range(0, loop):
                    temp_data.append(str(input('Nome do aluno: ')))
                    temp_data.append(str(input('Data de nascimento do aluno: ')))
                    print('Turmas disponiveis: ', end='')
                    for turma in turmas:
                        print(f'{turma}', end='')
                    aluno_turma = (str(input('\nDigite o nome da turma na qual o aluno sera cadastrado: ')))
                    if aluno_turma not in turmas:
                        print('Turma não encontrada')
                        aluno_turma = (str(input('\nDigite o nome da turma na qual o aluno sera cadastrado: ')))
                    print('Aluno cadastrado!')
                    print()
                    temp_data.append(aluno_turma)
                    geral_list.append(temp_data[:])
                    print('Visão prévia:')
                    print(f'Nome: {temp_data[0]:<20} | Data de nascimento: {temp_data[1]}')
                    print()
                    temp_data.clear()

    elif inpt == 3:
        print('=-=-= Cadastramento de turmas =-=-=')
        name = str(input('Digite um nome para sua turma: ')).capitalize().strip()
        turmas.append(name)
        print('''Turma criada com Sucesso!
        ''')

    elif inpt == 4:
        while True:
            print('''=== Configurações do Programa ===
            
[1] Deletar turmas
[2] Deletar alunos
[3] Voltar ao programa
''')
            inpt = int(input('>>> '))

            if inpt == 1:
                print('Turmas disponiveis: ', end='')
                for turma in turmas:
                    print(f'{turma}', end='')
                del_item = str(input('Digite o nome da turma a ser deletada: '))
                if del_item not in turmas:
                    print('Turma não encontrada')
                    del_item = int(input('Digite o nome da turma a ser deletada: '))
                elif del_item in turmas:
                    turmas.remove(del_item)
                    print(turmas)
                    for aluno in geral_list:
                        if aluno[2] == del_item:
                            aluno[2] = 'Aluno sem Turma'
                    print('Concluido com exito')
                    print()
            elif inpt == 2:
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
                break
                print()



    elif inpt == 5:
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
                if done == True:
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
[4] Voltar ao programa''')
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
                                if done == False:
                                    while done == False:
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
                            print('Saindo do configurador...')
                            print()
                            break
