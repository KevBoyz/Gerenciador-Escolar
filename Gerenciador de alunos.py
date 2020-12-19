geral_list = list()
turmas = list()
temp_data = list()

while True:
    print('''=== Gerenciador de Alunos ===

[1] conferir lista de alunos
[2] editar configurações do aluno
[3] cadastrar novo aluno
[4] cadastrar nova turma''')
    inpt = int(input('>>> '))
    print()

    if inpt == 1:
        if len(geral_list) == 0:
            print('Adicione algum aluno na lista...')
            print()
        else:
            for c in range(0, len(turmas)):
                print(f'-=-=-=-=- {turmas[c]} -=-=-=-=-')
                for aluno in geral_list:
                    if aluno[2] == turmas[c]:
                        print(f'Nome: {aluno[0]:^15} Data de nascimento: {aluno[1]}')
                print()
    elif inpt == 2:
        print('== Configurações do aluno ==')
        print('Turmas disponíveis: ', end='')
        for turma in turmas:
            print(turma, end=', ')
        find1 = str(input('\nDigite a turma do aluno desejado: '))
        if find1 in turmas:
            print('OK')
            name = str(input('Digite o nome do aluno'))
            for aluno in geral_list:
                if aluno[2] == find1:
                    print(f'Nome: {aluno[0]:^15} Idade: {aluno[1]}')
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
                elif inpt == 2:
                    new_age = str(input('Nova data de nascimento: '))
                    for aluno in geral_list:
                        if aluno[0] == name:
                            aluno[1] = new_age
                elif inpt == 3:
                    name = str(input('Nome do aluno a ser mudado de turma: '))
                    if name not in geral_list:
                        print('Aluno não encontrado...')
                        name = str(input('Nome do aluno a ser mudado de turma: '))
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
                                    print('OK')
                                    aluno[2] = new_turm
                elif inpt == 4:
                    break
        else:
            print('Turma não encontrada')
            find1 = str(input('\nDigite a turma do aluno desejado: '))

    elif inpt == 3:
        if len(turmas) == 0:
            print('Antes de cadastrar alunos, cadastre primeiro uma turma')
        else:
            print(''' === Cadastramento de Alunos ===''')
            loop = int(input('Quantos alunos você quer cadastar? '))
            if loop == 0 or 0 > loop:
                print('Número invalido')
            else:
                print('OK')
                for c in range(0, loop):
                    temp_data.append(str(input('Nome do aluno: ')))
                    temp_data.append(str(input('Data de nascimento do aluno: ')))
                    print('Turmas disponiveis: ', end='')
                    for turma in turmas:
                        print(f'{turma}', end='')
                    aluno_turma = (str(input('\nDigete o nome d turma na qual o aluno sera cadastrado: ')))
                    if aluno_turma not in turmas:
                        print('Turma não encontrada')
                        aluno_turma = (str(input('\nDigete o nome d turma na qual o aluno sera cadastrado: ')))
                    print('Aluno cadastrado!')
                    temp_data.append(aluno_turma)
                    geral_list.append(temp_data[:])
                    temp_data.clear()
    elif inpt == 4:
        print('=== Casdastramento de turmas ===')
        name = str(input('Digite um nome para sua turma: '))
        turmas.append(name)