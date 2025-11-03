# mini-projeto-python-Josesoares-Joaopedromelo
Trabalho Referente a segunda nota de Python, materia da professora Heloisa.

Projeto 1: Sistema De Cadastro De Produtos

Funcionalidades:

O sistema apresenta um menu interativo com as seguintes opções:

 1.	Cadastrar produto

Permite inserir um novo produto no sistema.

Durante o cadastro, o usuário deve informar:

 •	Código (não pode repetir)
	
 •	Nome
	
 •	Preço
	
 •	Quantidade
	

 •	Categoria (entre as opções: Alimentos, Limpeza, Bebidas)

Caso o código informado já exista, o sistema avisa e solicita um novo código.

 2.	Listar produtos

Exibe todos os produtos cadastrados, mostrando seus detalhes (código, nome, preço, quantidade e categoria).

 3.	Buscar produto

Permite procurar um produto pelo nome e exibe todas as suas informações.

 4.	Atualizar produto

Permite alterar qualquer informação de um produto já existente.

O usuário deve informar o nome do produto e em seguida qual campo deseja modificar (por exemplo, o preço ou a quantidade).

 5.	Excluir produto

Remove um produto do sistema com base em seu nome.

 6.	Sair

Encerra a execução do sistema.

Estrutura de Dados

Cada produto é armazenado em um dicionário com as seguintes informações:

 •	Código
	
 •	Nome
	
 •	Preço
	
 •	Quantidade
	
 •	Categoria

Esses dicionários são armazenados dentro de uma lista (produtos_lista), e os códigos são controlados por um conjunto (codigos) para evitar duplicações.
As categorias disponíveis são fixas e estão definidas em uma tupla: (‘Alimentos’, ‘Limpeza’, ‘Bebidas’).

Exemplos de Uso

Ao iniciar o programa, o menu principal é exibido com as opções numeradas de 0 a 5. O usuário escolhe o número correspondente à ação que deseja realizar.

Exemplo 1 – Cadastrar produto:
O usuário escolhe a opção 1 e informa os dados do novo produto. Por exemplo, ele digita o código 101, o nome “Arroz”, o preço 7.99, a quantidade 10 e a categoria “Alimentos”. O produto é então adicionado à lista do sistema.

Exemplo 2 – Listar produtos:
Ao selecionar a opção 2, o sistema mostra todos os produtos cadastrados até o momento, exibindo as informações de cada um de forma organizada.

Exemplo 3 – Buscar produto:
Com a opção 3, o usuário digita o nome de um produto, como “Arroz”, e o sistema retorna todas as informações cadastradas sobre esse item.

Exemplo 4 – Atualizar produto:
Na opção 4, o usuário informa o nome do produto que deseja alterar e depois indica qual campo quer modificar, como o preço. Em seguida, fornece o novo valor e o sistema atualiza automaticamente.

Exemplo 5 – Excluir produto:
Ao escolher a opção 5, o usuário informa o nome do produto que deseja remover. O sistema exclui o produto e confirma a ação na tela.

Exemplo 6 – Sair:
Escolhendo a opção 0, o sistema é encerrado e volta para o terminal.

Projeto 2:Sistema de Controle de Alunos e Notas

Descrição do Projeto:
O sistema foi criado para auxiliar professores no registro e consulta do desempenho dos alunos.  
Através de um menu interativo, o usuário pode cadastrar alunos, inserir notas, verificar médias e gerar relatórios.

Funcionalidades:

 1 Cadastrar aluno: adiciona um novo aluno ao sistema, com matrícula gerada automaticamente. 
 
 2 Registrar notas: permite lançar três notas para um aluno cadastrado.
 
 3 Listar alunos e médias: exibe todos os alunos com suas respectivas notas e médias calculadas. 
 
 4 Buscar aluno: pesquisa um aluno específico pelo nome e mostra suas informações. 
 
 5 Mostrar aprovados e reprovados: separa os alunos com média maior ou igual a 7 dos que ficaram abaixo. 
 
 6 Relatórios: apresenta relatórios detalhados com alunos cadastrados, médias, estatísticas e aprovação. 
 
 0 Sair: encerra o programa. 


Estruturas utilizadas:

 `while` e `for` para laços de repetição;
 `if`, `elif`, `else` para tomadas de decisão;
 `dicionário` para armazenar alunos e notas;
 `set` para evitar que repitam nomes;
 `tupla` para armazenar as notas de forma que elas não possam ser mudadas;
 `listas temporárias` para registrar notas antes de transformar em tuplas.

 **Exemplo de uso**


          SISTEMA DE CONTROLE DE ALUNOS E NOTAS

1 - Cadastrar aluno

2 - Registrar notas

3 - Listar alunos e médias

4 - Buscar aluno

5 - Mostrar aprovados e reprovados

6 - Relatórios

0 - Sair

Escolha uma opção: 1
Nome do aluno: Ana
Aluno Ana cadastrado com matrícula 1001.
Depois de registrar notas:

Será printado:
Copiar código
1001 - Ana | Notas: (8.0, 9.0, 7.5) | Média: 8.17 | Aprovado
