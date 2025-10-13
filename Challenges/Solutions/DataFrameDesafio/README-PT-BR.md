# DataFrame - Desafio

Este repositório faz parte do **curso de Análise de Dados e Inteligência Artificial**, e contém a **solução de um desafio prático** que envolveu manipulação de dados utilizando **Python**, **CSV** e a biblioteca **Pandas**.

---

## Objetivo do Desafio

O desafio tinha como proposta **analisar dados de alunos e disciplinas** a partir de um arquivo CSV, aplicando técnicas básicas de filtragem, agrupamento e agregação de dados.  
O foco foi compreender como trabalhar com **estruturas tabulares** e **operações estatísticas** em Python.

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **CSV (Comma-Separated Values)**

---


- **notas.csv** → Contém os dados de alunos, disciplinas, notas e faltas.  
- **desafio_pandas.py** → Código Python com todas as etapas de leitura, filtragem e análise dos dados.  
- **README.md** → Este arquivo de documentação.

---

## Etapas do Desafio

### 1️⃣ Leitura do arquivo CSV  
O arquivo `notas.csv` foi lido utilizando a biblioteca **csv** e **pandas**, garantindo compatibilidade com caracteres especiais (encoding `latin-1`).

```python
with open('notas.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
```

### 2️⃣ Criação de um filtro condicional

Foi criado um novo DataFrame filtrado, exibindo apenas alunos da disciplina Matemática com nota maior que 7.

```
filter = (df['Disciplina'] == 'Matemática') & (df['Nota'] > 7)
df_filtered = df[filter]
print(df_filtered)
```

### 3️⃣ Exibição dos alunos aprovados

Foram selecionados e exibidos apenas os alunos com nota maior ou igual a 6.

```
approved_students = df[df['Nota'] >= 6]
print(approved_students)
```

### 4️⃣ Cálculo da média de notas e soma de faltas por disciplina

Agrupamento dos dados por disciplina com uso do método groupby() e agregação de valores com mean e sum.

```
average_sum = df.groupby('Disciplina').agg({'Nota': 'mean', 'Faltas': 'sum'})
print(average_sum)
```

### 5️⃣ Descoberta da disciplina com maior média

Utilizando o agrupamento, foi identificado qual disciplina obteve a maior média geral.

```
average = df.groupby('Disciplina').agg({'Nota': 'mean'})
highest_average_discipline = average['Nota'].idxmax()
highest_average = average['Nota'].max()

print("The subject with the highest average is:", highest_average_discipline, "and your average was:", highest_average)
```

## Resultados

- O código exibe todas as etapas de análise de forma organizada.
- Mostra os alunos aprovados, as médias por disciplina e a disciplina com melhor desempenho geral.
- Demonstra o uso de operações condicionais, agregações estatísticas e leitura de arquivos CSV — habilidades essenciais em análise de dados.
