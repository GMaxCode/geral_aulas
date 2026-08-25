# 🐍 Estudos de Python

Repositório criado para armazenar e acompanhar minha evolução nos estudos de **Python**, reunindo aulas, exercícios práticos, testes e pequenos projetos desenvolvidos durante o aprendizado.

O objetivo deste repositório é documentar minha evolução na linguagem, desde os fundamentos da programação até manipulação e análise de dados.

---

## 📚 Conteúdos estudados

Durante os estudos, estão sendo abordados conceitos como:

* Sintaxe básica do Python
* Variáveis e tipos de dados
* Entrada e saída de dados
* Operadores
* Estruturas condicionais
* Estruturas de repetição
* Listas e outras estruturas de dados
* Funções
* Manipulação de arquivos
* Arquivos CSV
* Introdução à análise de dados
* Pandas
* DataFrames
* Filtros e manipulação de dados
* Criação de novas colunas
* Operações vetorizadas
* Agregação de dados

Novos conteúdos serão adicionados conforme o avanço dos estudos.

---

## 📂 Estrutura do repositório

```text
geral_aulas/
│
├── dados_csv/
│   ├── CSV_SHEETS.PY
│   └── vendas.csv
│
└── python/
    └── python/
        ├── aula41.py
        ├── aula42.py
        ├── aula43.py
        ├── ...
        ├── aula51.py
        │
        ├── entrada_sistema.py
        ├── informaçãoes.py
        │
        ├── praticas.py
        ├── praticas1.py
        ├── praticas2.py
        ├── ...
        └── praticas22.py
```

### `python/python`

Contém os códigos desenvolvidos durante as aulas e exercícios utilizados para praticar os conceitos aprendidos.

Os arquivos `aulaXX.py` representam conteúdos desenvolvidos durante as aulas, enquanto os arquivos `praticasXX.py` são utilizados principalmente para exercícios, testes e fixação dos conceitos.

### `dados_csv`

Área destinada aos estudos envolvendo arquivos CSV e manipulação de dados.

Inclui arquivos de dados utilizados nos exercícios e scripts Python para leitura, tratamento e análise dessas informações.

---

## 📊 Estudos com Pandas

O repositório também acompanha minha introdução à biblioteca **Pandas**, utilizada para manipulação e análise de dados em Python.

Alguns conceitos praticados:

```python
import pandas as pd

df = pd.read_csv('dados_csv/vendas.csv')

df['subtotal'] = df['preco'] * df['quantidade']

total_geral = df['subtotal'].sum()

print(df)
print(total_geral)
```

Esse tipo de exercício permite trabalhar conceitos como:

* Leitura de arquivos CSV
* DataFrames
* Seleção de colunas
* Criação de colunas
* Operações entre colunas
* Vetorização
* Filtros
* Agregações
* Análise de dados

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas\&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

## 🚀 Como executar os códigos

### 1. Clone o repositório

```bash
git clone https://github.com/GMaxCode/geral_aulas.git
```

### 2. Entre na pasta

```bash
cd geral_aulas
```

### 3. Execute um arquivo Python

```bash
python caminho/do/arquivo.py
```

Por exemplo:

```bash
python python/python/aula51.py
```

---

## 📦 Dependências

A maior parte dos exercícios utiliza apenas recursos nativos do Python.

Para os exercícios de análise de dados, pode ser necessário instalar o **Pandas**:

```bash
pip install pandas
```

---

## 🎯 Objetivo

Este repositório funciona como um registro prático da minha evolução em programação.

A ideia é avançar progressivamente de:

```text
Fundamentos de Python
        ↓
Lógica de Programação
        ↓
Estruturas de Dados
        ↓
Funções e organização de código
        ↓
Manipulação de arquivos
        ↓
Pandas e DataFrames
        ↓
Análise de Dados
        ↓
Projetos práticos
```

Mais do que armazenar códigos prontos, o objetivo é manter registrado o processo de aprendizado, incluindo exercícios, testes, erros, correções e melhorias realizadas ao longo do caminho.

---

## 📈 Status

🚧 **Em desenvolvimento**

Este repositório é atualizado conforme avanço nos estudos e desenvolvo novos exercícios e projetos.

---

## 👨‍💻 Autor

Desenvolvido por **GMaxCode** durante os estudos de Python e análise de dados.

GitHub: **@GMaxCode**

---

> "A melhor forma de aprender programação é programando."
