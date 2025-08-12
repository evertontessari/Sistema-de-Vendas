# Sistema de Estoque e Vendas

Este projeto é um sistema profissional de controle de estoque e vendas com interface gráfica desenvolvida em Python utilizando Tkinter.

## Funcionalidades
- Cadastro de produtos com validação
- Listagem visual do estoque
- Venda de produtos com leitura de código de barras (simulada)
- Relatório de vendas detalhado
- Persistência dos dados

## Requisitos
- Python 3.7 ou superior
- Tkinter (já incluído na maioria das distribuições Python)

## Instalação
1. Clone o repositório:
   ```bash
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd NOME_REPOSITORIO
   ```
3. Execute o sistema:
   ```bash
   python main.py
   ```

## Uso
- Utilize o menu principal para acessar todas as funções do sistema.
- O cadastro, venda, listagem e relatório são realizados por janelas gráficas intuitivas.
- Para simular a leitura de código de barras, digite ou utilize um leitor no campo correspondente.

## Estrutura dos módulos
- `main.py`: Interface principal e navegação
- `estoque.py`: Cadastro e listagem de produtos
- `vendas.py`: Venda e relatório de vendas
- `persistencia.py`: Carregamento e salvamento dos dados

## Licença
Este projeto está sob a licença MIT.
