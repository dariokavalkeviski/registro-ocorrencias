# 🚨 Sistema de Registro de Ocorrências

Aplicação desenvolvida em **Python puro** que simula um sistema de registro de ocorrências policiais via terminal. Permite cadastrar, listar, buscar e encerrar ocorrências, com persistência de dados em arquivo `.csv`.

> Projeto desenvolvido unindo minha experiência de 30 anos como Policial Militar com os estudos em Análise e Desenvolvimento de Sistemas.

---

## 📸 Preview

```
========================================
   SISTEMA DE REGISTRO DE OCORRÊNCIAS
========================================
  1 - Registrar nova ocorrência
  2 - Listar todas as ocorrências
  3 - Buscar ocorrência
  4 - Encerrar ocorrência
  5 - Sair
========================================
  Escolha uma opção:
```

---

## 🚀 Funcionalidades

- 📋 Registrar nova ocorrência com data/hora automática
- 📄 Listar todas as ocorrências cadastradas
- 🔍 Buscar ocorrências por **tipo** ou **local**
- ✅ Encerrar ocorrência (alterar status para Fechada)
- 💾 Salvar e carregar dados automaticamente em arquivo `.csv`

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Linguagem principal |
| csv (built-in) | Leitura e escrita de dados |
| os (built-in) | Verificação de arquivos |
| datetime (built-in) | Data e hora automática |

> Nenhuma biblioteca externa necessária — tudo com Python puro!

---

## 📂 Estrutura do projeto

```
registro-ocorrencias/
├── ocorrencias.py      # Código principal do sistema
├── ocorrencias.csv     # Gerado automaticamente ao registrar
└── README.md           # Documentação do projeto
```

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/dariokavalkeviski/registro-ocorrencias.git
```

2. Acesse a pasta:
```bash
cd registro-ocorrencias
```

3. Execute o programa:
```bash
python ocorrencias.py
```

> Requisito: Python 3.x instalado. Sem necessidade de instalar pacotes externos.

---

## 📚 O que aprendi neste projeto

- Criação e uso de **funções** (`def`) para organizar o código
- Leitura e escrita de **arquivos CSV** com a biblioteca `csv`
- Uso da biblioteca `datetime` para capturar data e hora
- **List comprehension** para filtrar dados em listas
- Estrutura de **menu interativo** com loop `while`
- Boas práticas de organização e comentários no código

---

## 💡 Contexto do projeto

Este projeto nasceu da minha vivência como Policial Militar. Sistemas de registro de ocorrências são ferramentas fundamentais na segurança pública, e recriá-lo em Python foi uma forma de conectar minha experiência profissional com meu aprendizado em programação.

---

## 👨‍💻 Autor

**Dario Kavalkeviski**  
Estudante de ADS — UniCesumar  
Policial Militar em transição para a área de tecnologia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-dario--kavalkeviski-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/dario-kavalkeviski)
[![GitHub](https://img.shields.io/badge/GitHub-dariokavalkeviski-black?style=flat&logo=github)](https://github.com/dariokavalkeviski)
