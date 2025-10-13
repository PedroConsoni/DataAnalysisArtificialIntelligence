# DataFrame - Challenge

This repository is part of the Data Analysis and Artificial Intelligence course and contains the solution to a practical challenge involving data manipulation using Python, CSV, and the Pandas library.
---

## Challenge Objective

The challenge aimed to analyze student and course data from a CSV file, applying basic techniques of data filtering, grouping, and aggregation.
The main goal was to understand how to work with tabular structures and statistical operations in Python.
---

## 🛠 Technologies Used

- **Python 3**
- **Pandas**
- **CSV (Comma-Separated Values)**

---

## Challenge Steps

### 1️⃣ Reading the CSV file

The notas.csv file was read using the csv and pandas libraries, ensuring compatibility with special characters (encoding latin-1).

```
with open('notas.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
```

### 2️⃣ Creating a conditional filter

A new filtered DataFrame was created, displaying only students from the Mathematics subject with grades higher than 7.

```
filter = (df['Disciplina'] == 'Matemática') & (df['Nota'] > 7)
df_filtered = df[filter]
print(df_filtered)
```

### 3️⃣ Displaying approved students

Only students with grades greater than or equal to 6 were selected and displayed.

```
approved_students = df[df['Nota'] >= 6]
print(approved_students)
```

### 4️⃣ Calculating the average grades and total absences per subject

Data was grouped by subject using the groupby() method and aggregated using mean and sum.

```
average_sum = df.groupby('Disciplina').agg({'Nota': 'mean', 'Faltas': 'sum'})
print(average_sum)
```

### 5️⃣ Finding the subject with the highest average

Using the grouped data, the subject with the highest overall average was identified.

```
average = df.groupby('Disciplina').agg({'Nota': 'mean'})
highest_average_discipline = average['Nota'].idxmax()
highest_average = average['Nota'].max()

print("The subject with the highest average is:", highest_average_discipline, "and its average was:", highest_average)
```

## Results

- The code displays all analysis steps in an organized way.
- Shows approved students, averages per subject, and the subject with the best overall performance.
- Demonstrates the use of conditional operations, statistical aggregations, and CSV file reading — essential skills in data analysis.
