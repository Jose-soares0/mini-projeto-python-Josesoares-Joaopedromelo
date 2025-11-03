# mini-projeto-python-Josesoares-Joaopedromelo
Trabalho Referente a segunda nota de Python, materia da professora Heloisa.
Sistema de Controle de Alunos e Notas:

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

## 💻 **Exemplo de uso**

text
=======================================================
          SISTEMA DE CONTROLE DE ALUNOS E NOTAS
=======================================================
1 - Cadastrar aluno
2 - Registrar notas
3 - Listar alunos e médias
4 - Buscar aluno
5 - Mostrar aprovados e reprovados
6 - Relatórios
0 - Sair
=======================================================
Escolha uma opção: 1
Nome do aluno: Ana
Aluno Ana cadastrado com matrícula 1001.
Depois de registrar notas:

Será printado:
Copiar código
1001 - Ana | Notas: (8.0, 9.0, 7.5) | Média: 8.17 | Aprovado
