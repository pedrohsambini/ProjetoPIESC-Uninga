# ProjetoPIESC-Uninga
Sistema de Cadastro de Alunos

Documentação do Codigo:

Introdução
Esta documentação técnica descreve o funcionamento e a estrutura do sistema de cadastro implementado em Python utilizando a biblioteca Tkinter para interface gráfica e SQLite para armazenamento de dados. O sistema permite adicionar, exibir, editar e excluir cadastros de indivíduos.
Requisitos do Sistema
•	Python 3.x instalado no ambiente.
•	Bibliotecas tkinter e sqlite3 instaladas (ambas fazem parte da biblioteca padrão do Python).
Estrutura do Código
O código está estruturado em uma classe principal CadastroApp, que contém os métodos para criar a interface gráfica e manipular os dados dos cadastros. O código é dividido em métodos para diferentes funcionalidades, como criar a tabela do banco de dados, adicionar cadastros, mostrar cadastros, editar cadastros, excluir cadastros e pesquisar cadastros.
Métodos Principais
1.	__init__(self, root): Método de inicialização da classe, responsável por configurar a janela principal da aplicação e iniciar a conexão com o banco de dados SQLite.
2.	create_table(self): Método para criar a tabela cadastros no banco de dados se ela não existir.
3.	create_widgets(self): Método para criar e posicionar os widgets (rótulos, entradas e botões) na interface gráfica.
4.	add_cadastro(self): Método para adicionar um novo cadastro ao banco de dados.
5.	mostrar_cadastros(self): Método para exibir todos os cadastros cadastrados em uma nova janela.
6.	editar_cadastro(self): Método para editar um cadastro selecionado na lista de cadastros.
7.	atualizar_cadastro(self, cadastro_id): Método para atualizar as informações de um cadastro no banco de dados após edição.
8.	excluir_cadastro_selecionado(self): Método para excluir um cadastro selecionado na lista de cadastros.
9.	pesquisar_cadastro(self): Método para pesquisar um cadastro pelo nome.
Funcionamento do Sistema
•	Ao iniciar a aplicação, uma janela é aberta contendo campos para inserção de informações de cadastro.
•	O usuário pode preencher os campos obrigatórios e clicar no botão "Adicionar" para salvar o cadastro no banco de dados.
•	O botão "Mostrar Cadastros" exibe todos os cadastros em uma nova janela, onde o usuário pode selecionar um cadastro para edição ou exclusão.
•	O botão "Pesquisar Cadastro" permite ao usuário pesquisar um cadastro pelo nome.
•	Os cadastros são armazenados em um banco de dados SQLite local (cadastros.db).
Considerações Finais
O sistema de cadastro oferece uma interface simples e intuitiva para gerenciar informações de cadastro de forma eficiente, utilizando uma combinação das bibliotecas Tkinter e SQLite em Python.
