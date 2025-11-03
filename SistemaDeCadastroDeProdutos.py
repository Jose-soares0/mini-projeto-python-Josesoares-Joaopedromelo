produtos_lista = []
codigos = set()
categorias = ('Alimentos', 'Limpeza', 'Bebidas')

while True:
    print('\n1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Buscar produto')
    print('4 - Atualizar produto')
    print('5 - Excluir produto')
    print('0 - Sair')

    try:
        opcao = int(input('Digite o número referente ao que deseja: '))
    except ValueError:
        print('Entrada inválida! Digite apenas números.')
        continue

    if opcao == 1:
        try:
            codigo = int(input('Digite o código do produto: '))
        except ValueError:
            print('Código inválido! Digite apenas números.')
            continue
        
        if codigo in codigos:
            print('Código já existente')
            continue
        
        nome = input('Digite o nome do produto: ')
        try:
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade do produto: '))
        except ValueError:
            print('Preço ou quantidade inválidos! Cadastro cancelado.')
            continue

        print(f'Essas são as categorias existentes: {categorias}')
        categoria = input('Digite a categoria do produto: ').capitalize()

        if categoria not in categorias:
            print('Categoria inválida! Produto não cadastrado.')
            continue

        produtos = {
            'Código': codigo,
            'Nome': nome,
            'Preço': preco,
            'Quantidade': quantidade,
            'Categoria': categoria
        }
    
        codigos.add(codigo)
        produtos_lista.append(produtos)
        print('Produto cadastrado com sucesso!')

    elif opcao == 2:
        if not produtos_lista:
            print('Nenhum produto cadastrado.')
        else:
            print('\nLista de produtos:')
            for p in produtos_lista:
                print(f"Código: {p['Código']} | Nome: {p['Nome']} | "
                      f"Preço: R$ {p['Preço']:.2f} | Quantidade: {p['Quantidade']} | "
                      f"Categoria: {p['Categoria']}")

    elif opcao == 3:
        try:
            codigo = int(input('Digite o código do produto que deseja procurar: '))
        except ValueError:
            print('Código inválido!')
            continue

        encontrado = False
        for p in produtos_lista:
            if p['Código'] == codigo:
                print('\nProduto encontrado:')
                print(f"Código: {p['Código']} | Nome: {p['Nome']} | "
                      f"Preço: R$ {p['Preço']:.2f} | Quantidade: {p['Quantidade']} | "
                      f"Categoria: {p['Categoria']}")
                encontrado = True
                break
        
        if not encontrado:
            print('Produto não encontrado.')

    elif opcao == 4:
        try:
            codigo = int(input('Digite o código do produto que deseja alterar: '))
        except ValueError:
            print('Código inválido!')
            continue

        produto_encontrado = None
        for p in produtos_lista:
            if p['Código'] == codigo:
                produto_encontrado = p
                break
        
        if produto_encontrado:
            print(f"Produto atual: {produto_encontrado['Nome']} | "
                  f"Preço: R$ {produto_encontrado['Preço']:.2f} | "
                  f"Quantidade: {produto_encontrado['Quantidade']}")
            
            info_produto = input('Qual informação deseja alterar (Nome, Preço, Quantidade, Categoria)? ').capitalize()
            
            if info_produto not in produto_encontrado:
                print('Informação inválida!')
                continue

            nova_info = input(f'Digite o novo valor para {info_produto}: ')
            
            if info_produto == 'Preço':
                try:
                    nova_info = float(nova_info)
                except ValueError:
                    print('Preço inválido!')
                    continue
            elif info_produto == 'Quantidade':
                try:
                    nova_info = int(nova_info)
                except ValueError:
                    print('Quantidade inválida!')
                    continue
            elif info_produto == 'Categoria':
                nova_info = nova_info.capitalize()
                if nova_info not in categorias:
                    print('Categoria inválida!')
                    continue

            produto_encontrado[info_produto] = nova_info
            print('Informação alterada com sucesso!')
            print(produto_encontrado)
        else:
            print('Produto não encontrado.')

    elif opcao == 5:
        try:
            codigo = int(input('Digite o código do produto que deseja excluir: '))
        except ValueError:
            print('Código inválido!')
            continue

        produto_excluido = None
        for p in produtos_lista:
            if p['Código'] == codigo:
                produto_excluido = p
                break
        
        if produto_excluido:
            produtos_lista.remove(produto_excluido)
            codigos.remove(codigo)
            print('Produto excluído com sucesso!')
        else:
            print('Produto não encontrado.')

    elif opcao == 0:
        print('Sistema encerrado.')
        break   

    else:
        print('Opção inválida.')