
alunos_notas = {} 
nomes_cadastrados = set() 

print("--- Bem-vindo ao Sistema de Controle de Alunos ---")

while True:
    
    print("""
- Menu Principal -
1. Cadastrar aluno
2. Registrar notas
3. Listar alunos e médias
4. Buscar aluno
5. Mostrar aprovados e reprovados
6. Relatórios
0. Sair""")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo do sistema...")
        break 

    elif opcao == '1':
        nome = input("Digite o nome do aluno: ")
        if nome in nomes_cadastrados:
            print("Erro: Aluno já cadastrado.")
        else:
            nomes_cadastrados.add(nome) 
            alunos_notas[nome] = () 
            print(f"Aluno '{nome}' cadastrado com sucesso.")

    elif opcao == '2':
        nome = input("Digite o nome do aluno para registrar notas: ")
        
        if nome not in nomes_cadastrados:
            print("Erro: Aluno não cadastrado.")
        else:
            notas_temp = [] 
            try:
                for i in range(3): 
                    nota = float(input(f"Digite a {i+1}ª nota (0-10): "))
                    if not (0 <= nota <= 10):
                        print("Nota inválida. Operação cancelada.")
                        break 
                    notas_temp.append(nota)
                else: 
                    alunos_notas[nome] = tuple(notas_temp) 
                    print(f"Notas {tuple(notas_temp)} registradas para '{nome}'.")
            except ValueError:
                print("Erro: Entrada inválida. Digite apenas números.")

    elif opcao == '3':
        print("\n--- Lista de Alunos e Médias ---")
        if not alunos_notas:
            print("Nenhum aluno cadastrado.")
        else:
            for nome, notas in alunos_notas.items():
                if not notas:
                    print(f"Aluno: {nome} - (Notas não registradas)")
                else:
                    soma = 0
                    for nota in notas: 
                        soma += nota
                    media = soma / len(notas)
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f}")

    elif opcao == '4':
        nome_busca = input("Digite o nome do aluno que deseja buscar: ")
        
        if nome_busca in alunos_notas:
            print(f"\n--- Detalhes do Aluno: {nome_busca} ---")
            notas = alunos_notas[nome_busca]
            
            if not notas:
                print("Situação: Notas ainda não registradas.")
            else:
                soma = 0
                for nota in notas:
                    soma += nota
                media = soma / len(notas)
                print(f"Notas: {notas}")
                print(f"Média: {media:.2f}")
                print(f"Situação: {'Aprovado' if media >= 7 else 'Reprovado'}") 
        else:
            print("Aluno não encontrado.")

    elif opcao == '5':
        print("\n--- Situação dos Alunos (Aprovados/Reprovados) ---")
        aprovados = []
        reprovados = []
        
        for nome, notas in alunos_notas.items():
            if notas:
                soma = 0
                for nota in notas:
                    soma += nota
                media = soma / len(notas)
                
                if media >= 7: 
                    aprovados.append(nome)
                else: 
                    reprovados.append(nome)
        
        print("\n** Alunos Aprovados (Média >= 7.0) **")
        if not aprovados: print("(Nenhum)")
        else:
            for nome in aprovados: print(f"- {nome}")
                
        print("\n** Alunos Reprovados (Média < 7.0) **")
        if not reprovados: print("(Nenhum)")
        else:
            for nome in reprovados: print(f"- {nome}")

    elif opcao == '6':
        print("\n--- Menu de Relatórios ---")
        print("1. Alunos cadastrados")       
        print("2. Médias individuais")        
        print("3. Aprovados e Reprovados")  
        
        sub_opcao = input("Escolha um relatório: ")
        
        if sub_opcao == '1': 
            print("\n** Relatório: Alunos Cadastrados **")
            if not nomes_cadastrados:
                print("Nenhum aluno cadastrado.")
            else:
                for nome in nomes_cadastrados: print(f"- {nome}")

        elif sub_opcao == '2': 
            print("\n** Relatório: Médias Individuais **")
            if not alunos_notas:
                print("Nenhum aluno cadastrado.")
            else:
                for nome, notas in alunos_notas.items():
                    if not notas:
                        print(f"Aluno: {nome} - (Notas não registradas)")
                    else:
                        soma = 0
                        for nota in notas: soma += nota
                        media = soma / len(notas)
                        print(f"Aluno: {nome} - Média: {media:.2f}")
        
        elif sub_opcao == '3': 
            print("\n** Relatório: Aprovados e Reprovados **")
            aprovados_rel = []
            reprovados_rel = []
            
            for nome, notas in alunos_notas.items():
                if notas:
                    soma = 0
                    for nota in notas: soma += nota
                    media = soma / len(notas)
                    
                    if media >= 7: aprovados_rel.append(nome)
                    else: reprovados_rel.append(nome)
            
            print("\nAprovados (Média >= 7.0):")
            if not aprovados_rel: print("(Nenhum)")
            else:
                for nome in aprovados_rel: print(f"- {nome}")
                    
            print("\nReprovados (Média < 7.0):")
            if not reprovados_rel: print("(Nenhum)")
            else:
                for nome in reprovados_rel: print(f"- {nome}")
        else:
            print("Opção de relatório inválida.")

    else:
        print("Opção inválida. Por favor, escolha um número de 0 a 6")