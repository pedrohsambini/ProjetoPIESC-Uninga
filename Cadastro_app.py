import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Definindo uma cor de fundo

        self.db_conn = sqlite3.connect("cadastros.db")
        self.db_cursor = self.db_conn.cursor()

        self.create_table()

        self.create_widgets()

    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS cadastros (
                                    id INTEGER PRIMARY KEY,
                                    nome TEXT,
                                    data_nascimento TEXT,
                                    nome_mae TEXT,
                                    nome_pai TEXT,
                                    endereco TEXT,
                                    telefone_contato_1 TEXT,
                                    telefone_contato_2 TEXT)''')
        self.db_conn.commit()

    def create_widgets(self):
        # Definindo uma fonte comum para os rótulos e entradas
        self.fonte = ("Helvetica", 12)

        self.label_nome = tk.Label(self.root, text="Nome:", font=self.fonte, bg="#f0f0f0")
        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        self.label_data_nascimento = tk.Label(self.root, text="Data de Nascimento:", font=self.fonte, bg="#f0f0f0")
        self.label_data_nascimento.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_data_nascimento = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_data_nascimento.grid(row=1, column=1, padx=10, pady=5)

        self.label_nome_mae = tk.Label(self.root, text="Nome da Mãe:", font=self.fonte, bg="#f0f0f0")
        self.label_nome_mae.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome_mae = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_nome_mae.grid(row=2, column=1, padx=10, pady=5)

        self.label_nome_pai = tk.Label(self.root, text="Nome do Pai:", font=self.fonte, bg="#f0f0f0")
        self.label_nome_pai.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome_pai = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_nome_pai.grid(row=3, column=1, padx=10, pady=5)

        self.label_endereco = tk.Label(self.root, text="Endereço:", font=self.fonte, bg="#f0f0f0")
        self.label_endereco.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_endereco = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_endereco.grid(row=4, column=1, padx=10, pady=5)

        self.label_telefone1 = tk.Label(self.root, text="Telefone para Contato 1:", font=self.fonte, bg="#f0f0f0")
        self.label_telefone1.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_telefone1 = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_telefone1.grid(row=5, column=1, padx=10, pady=5)

        self.label_telefone2 = tk.Label(self.root, text="Telefone para Contato 2:", font=self.fonte, bg="#f0f0f0")
        self.label_telefone2.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_telefone2 = tk.Entry(self.root, width=50, font=self.fonte)
        self.entry_telefone2.grid(row=6, column=1, padx=10, pady=5)

        # Botão Adicionar
        self.button_add = tk.Button(self.root, text="Adicionar", command=self.add_cadastro, font=self.fonte)
        self.button_add.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Botão Mostrar Cadastros
        self.button_mostrar = tk.Button(self.root, text="Mostrar Cadastros", command=self.mostrar_cadastros, font=self.fonte)
        self.button_mostrar.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Botão Pesquisar Cadastro
        self.button_pesquisar = tk.Button(self.root, text="Pesquisar Cadastro", command=self.pesquisar_cadastro, font=self.fonte)
        self.button_pesquisar.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="we")


    def add_cadastro(self):
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        nome_mae = self.entry_nome_mae.get()
        nome_pai = self.entry_nome_pai.get()
        endereco = self.entry_endereco.get()
        telefone1 = self.entry_telefone1.get()
        telefone2 = self.entry_telefone2.get()

        if nome and data_nascimento and nome_mae and nome_pai and endereco and telefone1:
            self.db_cursor.execute("INSERT INTO cadastros (nome, data_nascimento, nome_mae, nome_pai, endereco, telefone_contato_1, telefone_contato_2) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, data_nascimento, nome_mae, nome_pai, endereco, telefone1, telefone2))
            self.db_conn.commit()
            messagebox.showinfo("Sucesso", "Cadastro adicionado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_data_nascimento.delete(0, tk.END)
            self.entry_nome_mae.delete(0, tk.END)
            self.entry_nome_pai.delete(0, tk.END)
            self.entry_endereco.delete(0, tk.END)
            self.entry_telefone1.delete(0, tk.END)
            self.entry_telefone2.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")

    def mostrar_cadastros(self):
        self.mostrar_window = tk.Toplevel(self.root)
        self.mostrar_window.title("Cadastros")

        self.listbox = tk.Listbox(self.mostrar_window, width=100, height=20)
        self.listbox.pack(expand=True, fill="both")

        self.button_editar = tk.Button(self.mostrar_window, text="Editar Cadastro", command=self.editar_cadastro, font=self.fonte)
        self.button_editar.pack()

        self.button_excluir = tk.Button(self.mostrar_window, text="Excluir Cadastro", command=self.excluir_cadastro_selecionado, font=self.fonte)
        self.button_excluir.pack()

        self.db_cursor.execute("SELECT * FROM cadastros")
        self.cadastros = self.db_cursor.fetchall()
        for cadastro in self.cadastros:
            self.listbox.insert(tk.END, cadastro)

    def editar_cadastro(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            cadastro = self.cadastros[index]
            self.edit_window = tk.Toplevel(self.root)
            self.edit_window.title("Editar Cadastro")

            self.label_nome = tk.Label(self.edit_window, text="Nome:")
            self.label_nome.grid(row=0, column=0, padx=10, pady=5)
            self.entry_nome = tk.Entry(self.edit_window)
            self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
            self.entry_nome.insert(0, cadastro[1])

            self.label_data_nascimento = tk.Label(self.edit_window, text="Data de Nascimento:")
            self.label_data_nascimento.grid(row=1, column=0, padx=10, pady=5)
            self.entry_data_nascimento = tk.Entry(self.edit_window)
            self.entry_data_nascimento.grid(row=1, column=1, padx=10, pady=5)
            self.entry_data_nascimento.insert(0, cadastro[2])

            self.label_nome_mae = tk.Label(self.edit_window, text="Nome da Mãe:")
            self.label_nome_mae.grid(row=2, column=0, padx=10, pady=5)
            self.entry_nome_mae = tk.Entry(self.edit_window)
            self.entry_nome_mae.grid(row=2, column=1, padx=10, pady=5)
            self.entry_nome_mae.insert(0, cadastro[3])

            self.label_nome_pai = tk.Label(self.edit_window, text="Nome do Pai:")
            self.label_nome_pai.grid(row=3, column=0, padx=10, pady=5)
            self.entry_nome_pai = tk.Entry(self.edit_window)
            self.entry_nome_pai.grid(row=3, column=1, padx=10, pady=5)
            self.entry_nome_pai.insert(0, cadastro[4])

            self.label_endereco = tk.Label(self.edit_window, text="Endereço:")
            self.label_endereco.grid(row=4, column=0, padx=10, pady=5)
            self.entry_endereco = tk.Entry(self.edit_window)
            self.entry_endereco.grid(row=4, column=1, padx=10, pady=5)
            self.entry_endereco.insert(0, cadastro[5])

            self.label_telefone1 = tk.Label(self.edit_window, text="Telefone para Contato 1:")
            self.label_telefone1.grid(row=5, column=0, padx=10, pady=5)
            self.entry_telefone1 = tk.Entry(self.edit_window)
            self.entry_telefone1.grid(row=5, column=1, padx=10, pady=5)
            self.entry_telefone1.insert(0, cadastro[6])

            self.label_telefone2 = tk.Label(self.edit_window, text="Telefone para Contato 2:")
            self.label_telefone2.grid(row=6, column=0, padx=10, pady=5)
            self.entry_telefone2 = tk.Entry(self.edit_window)
            self.entry_telefone2.grid(row=6, column=1, padx=10, pady=5)
            self.entry_telefone2.insert(0, cadastro[7])

            self.button_atualizar = tk.Button(self.edit_window, text="Atualizar",
                                              command=lambda: self.atualizar_cadastro(cadastro[0]))
            self.button_atualizar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        else:
            messagebox.showerror("Erro", "Nenhum cadastro selecionado para edição.")

    def atualizar_cadastro(self, cadastro_id):
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        nome_mae = self.entry_nome_mae.get()
        nome_pai = self.entry_nome_pai.get()
        endereco = self.entry_endereco.get()
        telefone1 = self.entry_telefone1.get()
        telefone2 = self.entry_telefone2.get()

        if nome and data_nascimento and nome_mae and nome_pai and endereco and telefone1:
            self.db_cursor.execute(
                "UPDATE cadastros SET nome=?, data_nascimento=?, nome_mae=?, nome_pai=?, endereco=?, telefone_contato_1=?, telefone_contato_2=? WHERE id=?",
                (nome, data_nascimento, nome_mae, nome_pai, endereco, telefone1, telefone2, cadastro_id))
            self.db_conn.commit()
            messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
            self.edit_window.destroy()
            self.mostrar_cadastros()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")

    def excluir_cadastro_selecionado(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            cadastro = self.cadastros[index]
            cadastro_id = cadastro[0]
            self.db_cursor.execute("DELETE FROM cadastros WHERE id=?", (cadastro_id,))
            self.db_conn.commit()
            self.listbox.delete(index)
            messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso!")
        else:
            messagebox.showerror("Erro", "Nenhum cadastro selecionado para exclusão.")

    def pesquisar_cadastro(self):
        pesquisa = simpledialog.askstring("Pesquisar Cadastro", "Digite o nome para pesquisar:")
        if pesquisa:
            self.mostrar_window = tk.Toplevel(self.root)
            self.mostrar_window.title("Resultado da Pesquisa")

            self.listbox = tk.Listbox(self.mostrar_window, width=100, height=20)
            self.listbox.pack(expand=True, fill="both")

            self.db_cursor.execute("SELECT * FROM cadastros WHERE nome LIKE ?", ('%' + pesquisa + '%',))
            resultado = self.db_cursor.fetchall()
            for cadastro in resultado:
                self.listbox.insert(tk.END, cadastro)
        else:
            messagebox.showerror("Erro", "Nenhum termo de pesquisa fornecido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
