# 42 Python Modules

A consolidated collection of Python exercises and projects completed as part of the **42** curriculum (Modules 00–10).

## About This Repository
During the 42 curriculum, each Python module is developed and evaluated in a separate repository on Vogsphere. To keep my GitHub portfolio clean and easy to navigate, I merged all 11 modules into this single repository **while preserving the original Git commit history** of every module.

The curriculum progresses from core Python syntax and object-oriented design to modular architecture, dependency management, data validation, and functional programming—all written under strict `flake8` linting and type-annotation standards.

## Modules Overview

| Module | Folder | Key Topics & Skills |
| :--- | :--- | :--- |
| **Module 00** | `./module_00` | Python syntax, variables, conditionals, loops, functions, basic I/O |
| **Module 01** | `./module_01` | Object-Oriented Programming (OOP), classes, attributes, methods, inheritance |
| **Module 02** | `./module_02` | Error & exception handling (`try`/`except`/`finally`), custom exceptions |
| **Module 03** | `./module_03` | Core data structures (`list`, `tuple`, `set`, `dict`), comprehensions, generators, `sys.argv` |
| **Module 04** | `./module_04` | File I/O, standard streams (`stdin`/`stdout`/`stderr`), context managers (`with`) |
| **Module 05** | `./module_05` | Polymorphism, Abstract Base Classes (`abc`), interfaces, method overriding, data pipelines |
| **Module 06** | `./module_06` | Modular architecture, packages (`__init__.py`), relative/absolute imports, circular dependencies |
| **Module 07** | `./module_07` | Advanced OOP & design patterns (Factory, Strategy, composition, multiple inheritance) |
| **Module 08** | `./module_08` | Virtual environments (`venv`, `poetry`), dependency isolation, environment configuration |
| **Module 09** | `./module_09` | Data validation & schema modeling with Pydantic (`BaseModel`, `Field`, custom validators) |
| **Module 10** | `./module_10` | Functional programming, `lambda`, `map`/`filter`/`reduce`, closures, decorators, `functools` |

## Tech Stack & Standards
* **Language:** Python 3.10+
* **Tools & Libraries:** Pydantic, Poetry / `venv`, `abc`, `functools`
* **Code Style:** Strict adherence to `flake8` standards and static type hints (`typing`)

## Usage

```bash
git clone [https://github.com/eylulzehrakablan/ft-python-modules.git](https://github.com/eylulzehrakablan/ft-python-modules.git)
cd ft-python-modules/module_00
python3 ex0/*
```