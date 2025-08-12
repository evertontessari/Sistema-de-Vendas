from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def vender_produto(estoque, vendas, root=None):
    def buscar_produto():
        codigo = entry_codigo.get().strip()
        if codigo in estoque:
            produto = estoque[codigo]
            lbl_nome.config(text=f"Nome: {produto['nome']}")
            lbl_preco.config(text=f"Preço: R$ {produto['preco']:.2f}")
            lbl_estoque.config(text=f"Em estoque: {produto['quantidade']}")
        else:
            lbl_nome.config(text="Produto não encontrado.")
            lbl_preco.config(text="")
            lbl_estoque.config(text="")

    def realizar_venda():
        codigo = entry_codigo.get().strip()
        quantidade = entry_quantidade.get().strip()
        if not codigo or not quantidade.isdigit():
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
            return
        quantidade = int(quantidade)
        if codigo not in estoque:
            messagebox.showerror("Erro", f"Produto com código {codigo} não encontrado.")
            return
        if estoque[codigo]['quantidade'] < quantidade:
            messagebox.showerror("Erro", "Quantidade insuficiente em estoque.")
            return
        estoque[codigo]['quantidade'] -= quantidade
        vendas.append({
            'codigo': codigo,
            'nome': estoque[codigo]['nome'],
            'quantidade': quantidade,
            'preco': estoque[codigo]['preco']
        })
        messagebox.showinfo("Venda", "Venda realizada com sucesso!")
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Realizar Venda - Profissional")
    janela.geometry("350x320")
    janela.configure(bg="#f5f5f5")

    tk.Label(janela, text="Leitura de Código de Barras", font=("Arial", 13, "bold"), bg="#f5f5f5", fg="#2c3e50").pack(pady=10)
    entry_codigo = tk.Entry(janela, font=("Arial", 12), width=20)
    entry_codigo.pack(pady=5)
    entry_codigo.focus()
    tk.Button(janela, text="Buscar Produto", font=("Arial", 10), bg="#2980b9", fg="white", command=buscar_produto).pack(pady=4)

    lbl_nome = tk.Label(janela, text="", font=("Arial", 11), bg="#f5f5f5", fg="#34495e")
    lbl_nome.pack(pady=2)
    lbl_preco = tk.Label(janela, text="", font=("Arial", 11), bg="#f5f5f5", fg="#34495e")
    lbl_preco.pack(pady=2)
    lbl_estoque = tk.Label(janela, text="", font=("Arial", 11), bg="#f5f5f5", fg="#34495e")
    lbl_estoque.pack(pady=2)

    tk.Label(janela, text="Quantidade:", font=("Arial", 11), bg="#f5f5f5").pack(pady=8)
    entry_quantidade = tk.Entry(janela, font=("Arial", 12), width=10)
    entry_quantidade.pack(pady=5)

    tk.Button(janela, text="Confirmar Venda", font=("Arial", 12), bg="#27ae60", fg="white", command=realizar_venda).pack(pady=15)

def relatorio_vendas(vendas, root=None):
    janela = tk.Toplevel(root)
    janela.title("Relatório de Vendas")
    janela.geometry("460x340")
    janela.configure(bg="#f5f5f5")
    tk.Label(janela, text="Relatório de Vendas", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#2c3e50").pack(pady=10)
    frame = tk.Frame(janela, bg="#f5f5f5")
    frame.pack(fill="both", expand=True)
    texto = tk.Text(frame, font=("Arial", 11), width=54, height=13, bg="#ecf0f1")
    texto.pack(padx=10, pady=5)
    texto.insert("end", f"{'Código':<10}{'Nome':<18}{'Qtd':<6}{'Preço':<10}{'Total':<10}\n")
    texto.insert("end", "-"*54 + "\n")
    total_geral = 0
    for venda in vendas:
        total = venda['quantidade'] * venda['preco']
        total_geral += total
        texto.insert("end", f"{venda['codigo']:<10}{venda['nome']:<18}{venda['quantidade']:<6}{venda['preco']:<10.2f}{total:<10.2f}\n")
    texto.insert("end", "\nTotal Geral: R$ {:.2f}".format(total_geral))
    texto.config(state="disabled")