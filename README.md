# 📦 Cadastro de Produtos e Controle de Estoque

Projeto desenvolvido durante as férias, por iniciativa própria, com o objetivo de praticar lógica de programação em Python e manipulação de arquivos. Simula o cadastro de produtos, controle de estoque e realização de pedidos com histórico salvo em arquivos `.txt` e `.csv`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Manipulação de arquivos (`.txt` e `.csv`)
- Módulo `datetime` com fuso horário brasileiro (`pytz`)
- Estrutura modular (divisão por arquivos: `main.py`, `estoque.py`, `pedido.py`, `utils.py`)

---

## 🐍 Estrutura do Projeto

- `main.py` – Arquivo principal, com o menu e controle da aplicação.  
- `estoque.py` – Responsável por cadastrar, atualizar e salvar produtos.  
- `pedido.py` – Gerencia os pedidos e atualiza o estoque.  
- `utils.py` – Funções auxiliares como limpar tela e obter data/hora formatada.  

---

## 🗂️ Arquivos Gerados pelo Código

- `estoque.csv` – Armazena os produtos cadastrados (nome, preço, quantidade e data).  
- `estoque_formatado.txt` – Versão legível e formatada do estoque.  
- `historico.txt` – Registro dos pedidos realizados, com data e itens comprados.

---

## 🚀 Funcionalidades

- Cadastro de produtos com nome, preço, quantidade e data/hora.  
- Exibição do estoque atualizado e ordenado.  
- Salvamento automático em arquivos.  
- Realização de pedidos com verificação de estoque.  
- Histórico de pedidos salvo e consultável.  
- Menu interativo e navegação simples.

---

## 💡 Observações

- O projeto não utiliza banco de dados externo, apenas arquivos locais.
- Todos os dados persistem mesmo após o encerramento do programa.

---

Projeto simples, mas funcional — feito com foco em organização, prática e aprendizado real de lógica com Python.
