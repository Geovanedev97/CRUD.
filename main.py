import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ge34982125',
    database='academia'
)

cursor = conexao.cursor()
tabela = input(''' [1]- alunos 
 [2]- funcionarios
 [3]- modalidade
 [4]- personal
Escolha a tabela: ''')

while tabela == "1":
    print(''' ---> MENU <---
 [1] Criar Aluno
 [2] Verificar Alunos
 [3] Atualizar Aluno
 [4] Excluir Aluno
 [5] Voltar ao menu principal
 [6] Sair''')
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        query = "INSERT INTO alunos (matricula, nome, cpf, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
        valores = (matricula, nome, cpf, endereco, telefone)
        cursor.execute(query, valores)
        conexao.commit()
        print("Aluno criado com sucesso!")
    elif escolha == '2':
        ler = "SELECT * FROM alunos"
        cursor.execute(ler)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)
    elif escolha == '3':
        matricula = input("Matrícula do aluno a ser atualizado: ")
        novo_nome = input("Novo nome: ")
        novo_cpf = input("Novo CPF: ")
        novo_endereco = input("Novo endereço: ")
        novo_telefone = input("Novo telefone: ")
        atualizar = "UPDATE alunos SET nome = %s, cpf = %s, endereco = %s, telefone = %s WHERE matricula = %s"
        valores = (novo_nome, novo_cpf, novo_endereco, novo_telefone, matricula)
        cursor.execute(atualizar, valores)
        conexao.commit()
        print("Aluno atualizado com sucesso!")
    elif escolha == '4':
        matricula = input("Matrícula do aluno a ser deletado: ")
        deletar = "DELETE FROM alunos WHERE matricula = %s"
        valores = (matricula,)
        cursor.execute(deletar, valores)
        conexao.commit()
        print("Aluno deletado com sucesso!")
    elif escolha == '5':
         tabela = input(
 ''' [1]- alunos 
 [2]- funcionarios
 [3]- modalidade
 [4]- personal
 Escolha a tabela: ''')
    elif escolha == '6':
        print("Saindo do programa.")
        break
    else:
        print("Escolha inválida. Tente novamente.")
        break

while tabela == "2":
    print('''---> MENU <---
 [1] Criar funcionários 
 [2] Verificar funcionários
 [3] Atualizar funcionários
 [4] Excluir funcionário
 [5] Voltar ao menu principal
 [6] Sair''')
    escolher = int(input("Escolha uma opção: "))
    if escolher == 1:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        departamento = input("Departamento: ")
        cpf_supervisor = input("CPF_Supervisor: ")
        salario = input("Salário: ")
        query = "INSERT INTO funcionarios (nome, cpf, departamento, cpf_supervisor, salario) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, cpf, departamento, cpf_supervisor, salario)
        cursor.execute(query, valores)
        conexao.commit()
        print("Funcionario criado com sucesso!")
    elif escolher == 2:
        ler = "SELECT * FROM funcionarios"
        cursor.execute(ler)
        funcionarios = cursor.fetchall()
        for funcionario in funcionarios:
            print(funcionario)
    elif escolher == 3:
        id_funcionarios = input("ID do funcionário: ")
        novo_nome = input("Novo nome: ")
        novo_cpf = input("Novo CPF: ")
        novo_departamento = input("Novo departamento: ")
        novo_cpf_su = input("Novo CPF do supervisor: ")
        novo_salario = input("Novo salário: ")
        atualiza = "UPDATE funcionarios SET nome = %s, cpf = %s, departamento = %s, cpf_supervisor = %s, salario = %s WHERE id_funcionarios = %s"
        valor = (novo_nome, novo_cpf, novo_departamento, novo_cpf_su, novo_salario, id_funcionarios)
        cursor.execute(atualiza, valor)
        conexao.commit()
        print("Funcionário atualizado com sucesso!")
    elif escolher == 4:
        id_funcionarios = input("ID do funcionário a ser deletado: ")
        deletar = "DELETE FROM funcionarios WHERE id_funcionarios = %s"
        valores = (id_funcionarios,)
        cursor.execute(deletar, valores)
        conexao.commit()
        print("Funcionário deletado com sucesso!")
    elif escolher == 5:
         tabela = input(
''' [1]- alunos 
 [2]- funcionarios
 [3]- modalidade
 [4]- personal
 Escolha a tabela: ''')
    elif escolher == 6:
        print("Programa encerrado")
    else:
        print("Escolha inválida. Tente novamente.")
        break

while tabela == "3":
    print('''---> MENU <---
 [1] Criar Modalidade
 [2] Verificar Modalidades
 [3] Atualizar Modalidade
 [4] Excluir Modalidade
 [5] Voltar ao menu principal
 [6] Sair
    ''')
    escolhe = int(input("Escolha uma opção: "))
    if escolhe == 1:
        id_modalidade = input("ID da modalidade: ")
        professor = input("professor: ")
        nome = input("Nome da modalidade: ")
        duracao = float(input("Duração: "))
        horario = float(input("Horário: "))
        query = "INSERT INTO modalidade (id_modalidade, professor, nome, duracao, horario) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, id_modalidade, professor, horario, duracao)
        cursor.execute(query, valores)
        conexao.commit()
        print("Modalidade criada com sucesso!")
    elif escolhe == 2:
        ler = "SELECT * FROM modalidade"
        cursor.execute(ler)
        modalidade = cursor.fetchall()
        for modal in modalidade:
            print(modal)
    elif escolhe == 3:
        id_modalidade = input("ID da modalidade: ")
        novo_professor = input("Novo professor: ")
        novo_nome = input("Nova modalidade: ")
        nova_duracao = input("Nova duração: ")
        novo_horario = input("Novo horário: ")
        atualiza = "UPDATE modalidade SET professor = %s, nome = %s, duracao = %s, horario = %s WHERE id_modalidade = %s"
        valor = (novo_professor, novo_nome, nova_duracao, novo_horario, id_modalidade)
        cursor.execute(atualiza, valor)
        conexao.commit()
        print("Funcionário atualizado com sucesso!")
    elif escolhe == 4:
        id_modalidade = input("ID da modalidade a ser deletado: ")
        deletar = "DELETE FROM modalidade WHERE id_modalidade = %s"
        valores = (id_modalidade,)
        cursor.execute(deletar, valores)
        conexao.commit()
        print("Modalidade deletada com sucesso!")
    elif escolhe == 5:
        tabela = input(
''' [1]- alunos 
 [2]- funcionarios
 [3]- modalidade
 [4]- personal
 Escolha a tabela: ''')
    elif escolhe == 6:
        print("Programa encerrado.")
    else:
        print("Escolha inválida. Tente novamente.")
        break


while tabela == "4":
        print('''---> MENU <---
 [1] Criar Personal 
 [2] Verificar Personais
 [3] Atualizar Personal
 [4] Excluir Personal
 [5] Voltar ao menu principal
 [6] Sair''')
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            id_personal = input("ID do personal: ")
            nome_personal = input("Nome: ")
            cpf_personal = input("CPF: ")
            salario_personal = input("Salário: ")
            query = "INSERT INTO personal (id_personal, nome, cpf_personal, salario_personal) VALUES (%s, %s, %s, %s)"
            valores = (nome_personal, cpf_personal, salario_personal, id_personal)
            cursor.execute(query, valores)
            conexao.commit()
            print("Personal criado com sucesso!")
        elif escolha == 2:
            ler = "SELECT * FROM personal"
            cursor.execute(ler)
            personal = cursor.fetchall()
            for perso in personal:
                print(perso)
        elif escolha == 3:
            id_personal = input("ID do personal: ")
            novo_nome = input("Novo nome: ")
            novo_cpf = input("Novo CPF: ")
            novo_salario = input("Novo Salário: ")
            atualiza = "UPDATE personal SET nome = %s, cpf = %s, salario = %s WHERE id_personal = %s"
            valor = (novo_nome, novo_cpf, novo_salario, id_personal)
            cursor.execute(atualiza, valor)
            conexao.commit()
            print("Personal atualizado com sucesso.")
        elif escolha == 4:
            id_personal = input("ID do Personal a ser deletado: ")
            deletar = "DELETE FROM personal WHERE id_personal = %s"
            valores = (id_personal,)
            cursor.execute(deletar, valores)
            conexao.commit()
            print("Personal deletado com sucesso!")
        elif escolha == 5:
            tabela = input(
''' [1]- alunos 
 [2]- funcionarios
 [3]- modalidade
 [4]- personal
 Escolha a tabela: ''')
        elif escolha == 6:
            print("Programa encerrado.")
        else:
            print("Escolha inválida. Tente novamente.")
            break
cursor.close()
conexao.close()
