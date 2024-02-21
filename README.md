# ProjetoPIESC-Uninga
Sistema de Cadastro de Alunos

Documentação do Codigo:

Introdução
Esta documentação técnica descreve o funcionamento e a estrutura do sistema de cadastro implementado em Python utilizando a biblioteca Tkinter para interface gráfica e SQLite para armazenamento de dados. O sistema permite adicionar, exibir, editar e excluir cadastros de indivíduos.
Requisitos do Sistema
•	Python 3.x instalado no ambiente.
•	Bibliotecas tkinter e sqlite3 instaladas (ambas fazem parte da biblioteca padrão do Python).

Funcionamento do Sistema:
•	Ao iniciar a aplicação, uma janela é aberta contendo campos para inserção de informações de cadastro.
•	O usuário pode preencher os campos obrigatórios e clicar no botão "Adicionar" para salvar o cadastro no banco de dados.
•	O botão "Mostrar Cadastros" exibe todos os cadastros em uma nova janela, onde o usuário pode selecionar um cadastro para edição ou exclusão.
•	O botão "Pesquisar Cadastro" permite ao usuário pesquisar um cadastro pelo nome.
•	Os cadastros são armazenados em um banco de dados SQLite local (cadastros.db).
Considerações Finais
O sistema de cadastro oferece uma interface simples e intuitiva para gerenciar informações de cadastro de forma eficiente, utilizando uma combinação das bibliotecas Tkinter e SQLite em Python.
