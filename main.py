import tkinter as tk
from tkinter import messagebox
from persistencia import carregar_estoque, salvar_estoque, carregar_vendas, salvar_vendas
from estoque import cadastrar_produto, listar_estoque
from vendas import vender_produto, relatorio_vendas

def main():
    estoque = carregar_estoque()
    vendas = carregar_vendas()

    def cadastrar():
        cadastrar_produto(estoque, root)

    def listar():
        listar_estoque(estoque, root)

    def vender():
        vender_produto(estoque, vendas, root)

    def relatorio():
        relatorio_vendas(vendas, root)

    def salvar_sair():
        salvar_estoque(estoque)
        salvar_vendas(vendas)
        messagebox.showinfo("Saída", "Dados salvos. Saindo...")
        root.destroy()

    root = tk.Tk()
    root.title("Sistema de Estoque e Vendas")
    root.geometry("400x350")
    root.configure(bg="#f5f5f5")

    titulo = tk.Label(root, text="MENU PRINCIPAL", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#2c3e50")
    titulo.pack(pady=20)

    frame_botoes = tk.Frame(root, bg="#f5f5f5")
    frame_botoes.pack(pady=10)

    btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar Produto", width=25, font=("Arial", 12), bg="#2980b9", fg="white", command=cadastrar)
    btn_cadastrar.pack(pady=6)
    btn_listar = tk.Button(frame_botoes, text="Listar Estoque", width=25, font=("Arial", 12), bg="#27ae60", fg="white", command=listar)
    btn_listar.pack(pady=6)
    btn_vender = tk.Button(frame_botoes, text="Realizar Venda", width=25, font=("Arial", 12), bg="#e67e22", fg="white", command=vender)
    btn_vender.pack(pady=6)
    btn_relatorio = tk.Button(frame_botoes, text="Relatório de Vendas", width=25, font=("Arial", 12), bg="#8e44ad", fg="white", command=relatorio)
    btn_relatorio.pack(pady=6)
    btn_sair = tk.Button(frame_botoes, text="Salvar e Sair", width=25, font=("Arial", 12), bg="#c0392b", fg="white", command=salvar_sair)
    btn_sair.pack(pady=12)

    rodape = tk.Label(root, text="© 2024 Sistema de Estoque e Vendas", font=("Arial", 9), bg="#f5f5f5", fg="#7f8c8d")
    rodape.pack(side="bottom", pady=8)

    root.mainloop()

if __name__ == "__main__":
    main()