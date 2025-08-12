import tkinter as tk
from tkinter import messagebox

def cadastrar_produto(estoque, root=None):
    def salvar_produto():
        codigo = entry_codigo.get().strip()
        nome = entry_nome.get().strip()
        quantidade = entry_quantidade.get().strip()
        preco = entry_preco.get().strip()
        if not codigo or not nome or not quantidade.isdigit() or not preco.replace('.', '', 1).isdigit():
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return
        quantidade = int(quantidade)
        preco = float(preco)
        if codigo in estoque:
            messagebox.showerror("Erro", "Código já cadastrado.")
            return
        estoque[codigo] = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        }
        messagebox.showinfo("Cadastro", "Produto cadastrado com sucesso!")
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Cadastro de Produto")
    janela.geometry("350x320")
    janela.configure(bg="#f5f5f5")

    tk.Label(janela, text="Cadastro de Produto", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#2c3e50").pack(pady=10)
    tk.Label(janela, text="Código:", font=("Arial", 11), bg="#f5f5f5").pack()
    entry_codigo = tk.Entry(janela, font=("Arial", 11), width=25)
    entry_codigo.pack(pady=3)
    tk.Label(janela, text="Nome:", font=("Arial", 11), bg="#f5f5f5").pack()
    entry_nome = tk.Entry(janela, font=("Arial", 11), width=25)
    entry_nome.pack(pady=3)
    tk.Label(janela, text="Quantidade:", font=("Arial", 11), bg="#f5f5f5").pack()
    entry_quantidade = tk.Entry(janela, font=("Arial", 11), width=25)
    entry_quantidade.pack(pady=3)
    tk.Label(janela, text="Preço:", font=("Arial", 11), bg="#f5f5f5").pack()
    entry_preco = tk.Entry(janela, font=("Arial", 11), width=25)
    entry_preco.pack(pady=3)
    tk.Button(janela, text="Salvar", font=("Arial", 12), bg="#27ae60", fg="white", command=salvar_produto).pack(pady=15)

def listar_estoque(estoque, root=None):
    janela = tk.Toplevel(root)
    janela.title("Estoque Atual")
    janela.geometry("420x320")
    janela.configure(bg="#f5f5f5")
    tk.Label(janela, text="Estoque Atual", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#2c3e50").pack(pady=10)
    frame = tk.Frame(janela, bg="#f5f5f5")
    frame.pack(fill="both", expand=True)
    texto = tk.Text(frame, font=("Arial", 11), width=48, height=12, bg="#ecf0f1")
    texto.pack(padx=10, pady=5)
    texto.insert("end", f"{'Código':<10}{'Nome':<18}{'Qtd':<6}{'Preço':<10}\n")
    texto.insert("end", "-"*44 + "\n")
    for codigo, prod in estoque.items():
        texto.insert("end", f"{codigo:<10}{prod['nome']:<18}{prod['quantidade']:<6}{prod['preco']:<10.2f}\n")
    texto.config(state="disabled")