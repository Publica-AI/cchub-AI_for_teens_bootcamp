# AI for Teens Bootcamp — Python Course Notes

A collection of structured, beginner-friendly Python learning materials designed for teen students. Each notebook follows **Bloom's Taxonomy** — building from basic recall up to creating real programs — and uses relatable local scenarios throughout every example.

---

## Quick Navigation

| # | Topic | View Notebook |
|---|-------|--------------|
| 1 | Fundamental Programming Concepts | [📘 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/fundamental_programming_concepts.ipynb) |
| 2 | Program Logic and Control Flow | [📗 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/program_logic_and_control_flow.ipynb) |
| 3 | Data Structures and Functions | [📙 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/data_structures_and_functions.ipynb) |
| 4 | Understanding File Paths and File System Interactions | [📕 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/file_paths_and_file_system.ipynb) |
| 5 | Working with Data — Using Pandas | [📓 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/working_with_data_pandas.ipynb) |
| 5b | ↳ Practice Workbook — Real Student Data Analysis | [🔬 Open notebook](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/data_analysis_workbook.ipynb) |

---

## How to Use These Notebooks

### Option 1 — Run in the Browser (No Installation Required)

Click any badge below to open that notebook instantly in **Google Colab** — no setup needed, just a Google account:

| Notebook | Open in Colab |
|----------|--------------|
| Topic 1 — Fundamental Programming Concepts | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/fundamental_programming_concepts.ipynb) |
| Topic 2 — Program Logic and Control Flow | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/program_logic_and_control_flow.ipynb) |
| Topic 3 — Data Structures and Functions | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/data_structures_and_functions.ipynb) |
| Topic 4 — File Paths and File System | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/file_paths_and_file_system.ipynb) |
| Topic 5 — Working with Data — Using Pandas | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/working_with_data_pandas.ipynb) |
| Topic 5 Practice — Data Analysis Workbook | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/data_analysis_workbook.ipynb) |

---

### Option 2 — Run Locally (on Your Computer)

**Prerequisites:**
- [Python 3.8+](https://www.python.org/downloads/) installed
- [Jupyter Notebook](https://jupyter.org/) or [VS Code](https://code.visualstudio.com/) with the Jupyter extension

**Steps:**

```bash
# 1. Clone the repository
git clone https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp.git

# 2. Move into the project folder
cd cchub-AI_for_teens_bootcamp

# 3. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# 4. Install Jupyter if you don't have it
pip install notebook

# 5. Launch Jupyter
jupyter notebook
```

> A browser window will open. Navigate into `Intro_to_Python/` or `Data_literacy/` and click any `.ipynb` file to start a notebook.

---

### Option 3 — VS Code

1. Open VS Code and install the **Jupyter extension** (search in Extensions: `ms-toolsai.jupyter`).
2. Clone or download the repository and open the folder in VS Code.
3. Navigate into `Intro_to_Python/` or `Data_literacy/` and click any `.ipynb` file — it opens directly in VS Code.
4. Select a Python kernel from the top-right dropdown and run cells with **Shift + Enter**.

---

## Course Notebooks

The notebooks are designed to be completed **in order** — each topic builds on the previous one.

---

### 📘 Topic 1 — Fundamental Programming Concepts
**File:** [`Intro_to_Python/fundamental_programming_concepts.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/fundamental_programming_concepts.ipynb)

**What you will learn:**
- How to display information using `print()`
- How to receive input from users using `input()`
- How to create and use variables to store data
- The four core data types: `str`, `int`, `float`, `bool`
- How to write comments to explain your code

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Output | `print()`, `sep`, `end`, f-strings |
| 2 | User Input | `input()`, type conversion with `int()` and `float()` |
| 3 | Variables | Assignment, updating values, swapping |
| 4 | Data Types | `str`, `int`, `float`, `bool`, `type()`, casting |
| 5 | Comments | `#`, `"""docstrings"""`, debugging with comments |

**End-of-topic project:** Student ID Card — a program that collects and displays a formatted profile using all five concepts.

---

### 📗 Topic 2 — Program Logic and Control Flow
**File:** [`Intro_to_Python/program_logic_and_control_flow.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/program_logic_and_control_flow.ipynb)

**What you will learn:**
- How to perform calculations using arithmetic operators
- How to compare values and produce `True` / `False` results
- How to combine conditions with logical operators
- How to make decisions with `if`, `elif`, and `else`
- How to repeat tasks using `for` and `while` loops

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Arithmetic Operators | `+  -  *  /  //  %  **` |
| 2 | Comparison Operators | `==  !=  >  <  >=  <=` |
| 3 | Logical Operators | `and`, `or`, `not` |
| 4 | Conditional Statements | `if`, `elif`, `else` |
| 5 | For Loops | `for x in sequence`, `range()`, `enumerate()` |
| 6 | While Loops | `while condition`, input validation, counters |

**End-of-topic project:** School Report Card Generator — loops through student scores, assigns grades, and prints a formatted report.

---

### 📙 Topic 3 — Data Structures and Functions
**File:** [`Intro_to_Python/data_structures_and_functions.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/data_structures_and_functions.ipynb)

**What you will learn:**
- Why data structures exist and when to use each type
- How to store fixed data in **tuples**
- How to build and modify **lists**
- How to organise data with named keys using **dictionaries**
- How to write reusable blocks of code with **functions**
- How to pass data into functions using **parameters**
- How to send results back using **return values**
- How to combine functions and data structures to solve real problems

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Intro to Data Structures | Overview of list, tuple, dictionary |
| 2 | Tuples | `()`, indexing, unpacking, immutability |
| 3 | Lists | `[]`, `.append()`, `.remove()`, `.sort()`, `len()` |
| 4 | Dictionaries | `{}`, key–value pairs, `.items()`, `.keys()`, `.values()` |
| 5 | Intro to Functions | `def`, calling functions, avoiding repetition |
| 6 | Function Parameters | Arguments, multiple parameters, default values |
| 7 | Return Values | `return`, using returned values, returning multiple values |
| 8 | Functions + Data Structures | Passing lists/dicts to functions, returning filtered results |

**End-of-topic project:** Student Results Management System — stores students and scores in dictionaries, uses functions to calculate averages, assign grades, and find the top student.

---

### 📕 Topic 4 — Understanding File Paths and File System Interactions
**File:** [`Intro_to_Python/file_paths_and_file_system.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Intro_to_Python/file_paths_and_file_system.ipynb)

**What you will learn:**
- How a computer's file system is organised (files, folders, paths)
- What a file path is and how to build one safely in Python
- The difference between absolute paths and relative paths
- How to create and manage directories using Python
- How to open, read, and write text files
- Best practices to avoid data loss and errors when working with files

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Intro to File Systems | `os.getcwd()`, `os.listdir()`, `os.path.exists()` |
| 2 | Understanding File Paths | `os.path.join()`, `basename()`, `dirname()`, `splitext()` |
| 3 | Absolute vs Relative Paths | `os.path.abspath()`, `.` and `..` notation |
| 4 | Working with Directories | `os.mkdir()`, `os.makedirs()`, `os.rename()`, `os.remove()` |
| 5 | Opening Files | `open()`, file modes `r  w  a`, the `with` statement |
| 6 | Reading Files | `.read()`, `.readline()`, `.readlines()`, looping over lines |
| 7 | Writing Files | `.write()`, `.writelines()`, `w` vs `a` mode |
| 8 | Best Practices | `with` statement, `try/except`, safe file functions |

**End-of-topic project:** Personal Notes Manager — saves and retrieves notes per author using functions, file append mode, and directory management.

> **Note:** Topic 4 notebooks create a `sample_files/` folder in the same directory as the notebook. This is expected — the folder holds practice files generated during the exercises.

---

### 📓 Topic 5 — Working with Data — Using Pandas
**File:** [`Data_literacy/working_with_data_pandas.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/working_with_data_pandas.ipynb)

**What you will learn:**
- What pandas is and why it is the go-to tool for working with data in Python
- How to create and use **Series** and **DataFrames**
- How to load data from a CSV file and save results back to disk
- How to explore a dataset: shape, column names, data types, and summary statistics
- How to find and fix missing values and duplicate rows
- How to select specific rows and columns using labels and conditions
- How to add new columns, apply functions, and transform data
- How to summarise data using aggregation and `groupby`
- How to sort, rank, and reshape a dataset
- How to combine two DataFrames using `concat` and `merge`
- How to create basic charts directly from a DataFrame

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Intro to Pandas & Data Structures | `pd.Series`, `pd.DataFrame`, column access |
| 2 | Loading and Saving Data | `pd.read_csv()`, `to_csv()`, `data/` folder |
| 3 | Exploring a Dataset | `.shape`, `.dtypes`, `.info()`, `.describe()`, `.head()` |
| 4 | Data Cleaning | `.isnull()`, `.fillna()`, `.dropna()`, `.drop_duplicates()` |
| 5 | Accessing and Selecting Data | `.loc[]`, `.iloc[]`, boolean filtering |
| 6 | Data Manipulation | New columns, `.apply()`, `pd.cut()` for grade bands |
| 7 | Summarisation and Aggregation | `.mean()`, `.sum()`, `.value_counts()`, `groupby()` |
| 8 | Sorting and Reshaping | `.sort_values()`, `.rank()`, `.reset_index()` |
| 9 | Combining Datasets | `pd.concat()`, `pd.merge()`, inner vs left join |
| 10 | Data Visualisation | `.plot()`, bar, line, histogram, scatter charts |

**End-of-topic project:** Bootcamp Performance Dashboard — loads the student dataset, cleans it, adds grade and performance columns, aggregates by school and city, and produces summary charts.

> **Note:** Topic 5 saves a simulated `students.csv` into `Data_literacy/data/` when you run the notebook. This is expected — it is the shared dataset used across all sections of the notebook.

---

### 🔬 Topic 5 — Practice Workbook: Real Student Data Analysis
> This workbook is a hands-on companion to `working_with_data_pandas.ipynb`. Complete Topic 5 first, then work through this to apply everything on a real dataset.

**File:** [`Data_literacy/data_analysis_workbook.ipynb`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/data_analysis_workbook.ipynb)
**Dataset:** [`Data_literacy/data/Student_performance_data.csv`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/data/Student_performance_data.csv) — 2,392 real student records
**Data dictionary:** [`Data_literacy/data/student_data_dictionary.md`](https://github.com/Publica-AI/cchub-AI_for_teens_bootcamp/blob/main/Data_literacy/data/student_data_dictionary.md) — column definitions and value encodings

**What you will learn:**
- How to load and explore a real-world dataset using pandas
- How to spot missing data and read summary statistics
- How to count and compare groups using `.value_counts()` and `.groupby()`
- How to create bar charts, line charts, and histograms using matplotlib
- How to add titles, axis labels, grid lines, and reference lines to charts
- How to ask data-driven questions and find answers with code

**Sections at a glance:**

| # | Section | Key Concepts |
|---|---------|-------------|
| 1 | Load the Data | `pd.read_csv()` |
| 2 | First Peek | `.head()` |
| 3 | Dataset Size | `.shape` |
| 4 | Column Names | `.columns` |
| 5 | Missing Data | `.isnull().sum()` |
| 6 | Summary Statistics | `.describe()` |
| 7 | Grade Distribution + Bar Chart | `.value_counts()`, `matplotlib` intro |
| 8 | Study Time vs Grades | `.groupby().mean()`, bar chart |
| 9 | Absences vs Grades | groupby, bar chart |
| 10 | Tutoring Effect | groupby, `plt.ylim()`, `width` |
| 11 | Sports, Music & Volunteering | filtering, loops |
| 12 | Parental Support Trend | line chart, `plt.grid()` |
| 13 | GPA Distribution | histogram, `plt.axvline()` |

**Student challenges:** 4 independent tasks — from guided templates to a fully open-ended "design your own question" exercise.

> **Note:** This workbook loads `Student_performance_data.csv` from the `Data_literacy/data/` subfolder. No extra downloads needed — the file is already in the repository.

---

## Repository Structure

```
cchub-AI_for_teens_bootcamp/
│
├── README.md                               ← You are here
├── LICENSE
│
├── Intro_to_Python/                        ← Topics 1–4
│   ├── fundamental_programming_concepts.ipynb   ← Topic 1
│   ├── program_logic_and_control_flow.ipynb     ← Topic 2
│   ├── data_structures_and_functions.ipynb      ← Topic 3
│   └── file_paths_and_file_system.ipynb         ← Topic 4
│
└── Data_literacy/                          ← Topic 5
    ├── working_with_data_pandas.ipynb           ← Topic 5 main notebook
    ├── data_analysis_workbook.ipynb             ← Topic 5 practice workbook
    └── data/                                    ← Data folder
        ├── Student_performance_data.csv         ← Real dataset (2,392 students) used in workbook
        ├── student_data_dictionary.md           ← Column definitions and value encodings
        └── students.csv                         ← Simulated dataset created when Topic 5 runs
```

> **Note:** `students.csv` does not exist until you run the Topic 5 notebook — it is generated automatically by the code. `Student_performance_data.csv` and `student_data_dictionary.md` are already in the repository.

---

## Each Notebook Follows This Structure

Every section inside a notebook is built the same way, following Bloom's Taxonomy:

```
📖 Concept Explanation
    └── Clear definition with a real-life analogy
    └── Syntax summary or reference table

💻 Code Examples (2–3 per section)
    └── Well-commented, runnable code
    └── Relatable scenarios in each example

🏫 Class Activity
    └── A guided task to complete together as a class

✏️ Practice
    └── A short independent exercise to test understanding

🎯 End-of-Topic Project
    └── One larger program that combines all sections
```

---

## Prerequisites

No prior programming experience is required for Topic 1. Each topic builds on the previous, so it is recommended to complete them in order.

**Software needed:**
- Python 3.8 or higher
- Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension

---

## Quick Reference — Running a Cell

| Action | Keyboard Shortcut |
|--------|-------------------|
| Run the current cell | `Shift + Enter` |
| Run and insert a new cell below | `Alt + Enter` |
| Run all cells from top | `Cell → Run All` (menu) |
| Stop a running cell | `Interrupt Kernel` button (■) |
| Add a cell below | `B` (in command mode) |
| Delete a cell | `D D` (press D twice, in command mode) |

> **Command mode vs Edit mode:** Click a cell to select it (command mode — blue border). Press `Enter` to start typing inside it (edit mode — green border). Press `Escape` to return to command mode.

---

## License

See [LICENSE](LICENSE) for details.
