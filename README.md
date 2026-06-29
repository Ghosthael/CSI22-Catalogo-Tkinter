# CSI22 — Catálogo de Prestadores de Serviços (Tkinter)

Projeto para criar um catálogo de prestadores de serviços com interface gráfica em Tkinter. Permite cadastro, consulta e remoção de prestadores, persistindo informações em um banco de dados local.
Alunos:
- Ricardo Cardoso
- Leonardo Dantas
- Luiz Satoshi 

Resumo em inglês: A simple Tkinter-based service providers catalog with CRUD operations backed by a local database.

---

## Índice
- [Funcionalidades](#funcionalidades)
- [Capturas de tela](#capturas-de-tela)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Banco de dados](#banco-de-dados)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como contribuir](#como-contribuir)
- [Licença](#licença)
- [Autores](#autores)
- [Roadmap / Melhorias futuras](#roadmap--melhorias-futuras)

---

## Funcionalidades
- Cadastro de prestadores (nome, contato, especialidade, etc.)
- Busca/consulta por prestador
- Edição e exclusão de registros
- Interface gráfica usando Tkinter
- Persistência em banco de dados local (por exemplo SQLite)
- Controle de entradas no banco de dados
- Validação de CPF, CNPJ
- API de CEP que preenche automaticamente

## Requisitos
- Python 3.8+ 
- tkinter
- requests
- sqlite3
