# Python Learning Practice

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-success)
![Practicals](https://img.shields.io/badge/Practicals-130-orange)

A structured, practical-first Python course for beginners. Learn one concept at
a time, run each example independently, complete the chapter assignments, and
finish with projects and interview-style logic programs.

> **Learning principle:** read the definition, predict the output, run the
> program, change one value, and then solve the assignment without copying.

This folder is a practical, chapter-by-chapter Python course for beginners.
Every chapter contains **10 separate runnable program files** named `Program_01.py` through `Program_10.py`.
Read the comments, run the file, change a value, and run it again.

## Requirements

- Python 3.10 or newer
- A terminal and an editor such as VS Code

Check your Python installation:

```bash
python --version
```

## Get started

Clone the repository and enter the project folder:

```bash
git clone https://github.com/<your-username>/Python-Learning-Practice.git
cd Python-Learning-Practice
```

Run your first practical:

```bash
python Chapter_2/Program_01.py
```

On some systems, use `python3` instead of `python`.

## Learning path

| Chapter | Topic | What you practise |
| --- | --- | --- |
| 1 | Introduction | `print`, comments, and the first variable |
| 2 | Variables and input | Names, types, conversion, and formatted output |
| 3 | Operators | Arithmetic, comparisons, logic, and assignment |
| 4 | Decisions | `if`, `elif`, `else`, and nested decisions |
| 5 | Loops | `for`, `while`, ranges, `break`, and `continue` |
| 6 | Strings | Indexing, slicing, methods, and simple validation |
| 7 | Collections | Lists, tuples, sets, and dictionaries |
| 8 | Functions | Parameters, return values, scope, and docstrings |
| 9 | Errors and files | Exceptions, reading, writing, and JSON |
| 10 | Modules and packages | Imports, the standard library, and reusable code |
| 11 | Object-oriented Python | Classes, objects, methods, and inheritance |
| 12 | Useful advanced tools | Comprehensions, iterators, generators, and decorators |
| 13 | Projects | Beginner, moderate, and advanced project practice |

Each chapter has 10 separate practical files named `Program_01.py` through
`Program_10.py`. Each practical includes a beginner-friendly definition and
learning comments.

## Recommended practice routine

1. Run the file without changing it.
2. Predict the output before running each section.
3. Change one value and observe the result.
4. Add a small feature in the `# Try it` section.
5. Write the practical again without looking.

The examples intentionally use simple syntax first. Later chapters combine
earlier ideas rather than introducing a large framework.

## Repository structure

```text
Chapter_1 ... Chapter_13/
├── Program_01.py ... Program_10.py
└── Assignment_Practice_Questions/
    └── README.md
Chapter_13/Projects/
├── Beginner_Projects/
├── Moderate_Projects/
└── Advanced_Projects/
Logical_Programs_For_Interview/
```

## Progression

1. Complete Chapters 1-4 for the Python foundations.
2. Complete Chapters 5-8 for problem solving and reusable code.
3. Complete Chapters 9-12 for files, modules, classes, and advanced tools.
4. Complete Chapter 13 projects.
5. Practise the logical programs before interviews.

## Contributing

Suggestions and beginner-friendly improvements are welcome. Keep new examples
focused, use standard-library Python where possible, and include comments that
explain the important learning point.

## License

This repository is provided for educational practice. Add a license before
redistributing it as a public project.

## Beginner-friendly definitions

- **Variable:** a name that points to a value, such as a number or text.
- **Data type:** the kind of value, such as `int`, `float`, `str`, or `bool`.
- **Condition:** a True/False test used by a decision.
- **Loop:** code that repeats.
- **Function:** a reusable block of code that can accept input and return output.
- **List:** an ordered collection that can be changed.
- **Dictionary:** a collection of key-value pairs.
- **Exception:** a runtime problem that can be handled with `try` and `except`.
- **Module:** a Python file whose code can be imported and reused.
- **Class:** a blueprint used to create objects with data and behavior.

Each practical starts with a definition in its docstring. Comments explain the
important code steps; they are learning notes, not replacements for practice.

## Chapter 13 project levels

Chapter 13 also contains a `Projects` folder with separate project levels:

- `Chapter_13/Projects/Beginner_Projects` - calculator, quiz, and unit converter
- `Chapter_13/Projects/Moderate_Projects` - contact book, expense tracker, and
  password generator
- `Chapter_13/Projects/Advanced_Projects` - file organizer, quiz application,
  and library management system

Complete the beginner projects first. Move to moderate projects when you can
use functions, collections, files, and exceptions comfortably. Advanced
projects combine several chapters and are intended as final practice.

## Assignments and interview practice

The last folder inside every chapter is `Assignment_Practice_Questions`.
It contains chapter-specific questions to solve without copying the practical
files. Attempt the questions after completing that chapter.

The course root also contains `Logical_Programs_For_Interview`. These are
separate runnable programs that practise common interview patterns such as
palindromes, prime numbers, frequency counting, searching, sorting, and
recursion.
