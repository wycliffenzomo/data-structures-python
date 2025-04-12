# Data Structures Python
Data Structures Python is a pedagogical Python package designed to help learners understand and implement core data structures from scratch using Object-Oriented Programming (OOP) principles. The project introduces foundational structures—such as stacks, queues, linked lists, and binary search trees—and provides interactive Jupyter notebooks to demonstrate their usage. It serves both as a learning resource and a practical toolkit for exploring how these structures behave under the hood.

# Project Layout and Organization
The repository is structured to promote clarity and modularity:
data_structures/: This folder contains all Python modules implementing individual data structures. Each file encapsulates a single structure with class-based definitions and relevant methods.
examples/: Includes Jupyter notebooks that demonstrate how to use each data structure interactively. These examples serve both as usage demonstrations and testing environments.
README.md: A comprehensive guide providing background, setup instructions, and key usage notes.
pyproject.toml and setup.py: Used to define the package’s metadata, build instructions, and dependencies for PyPI distribution.
LICENSE: Specifies the usage rights and licensing terms under the MIT license.

# Learning Objectives
This project is intended to:
. Illustrate how fundamental data structures are built from the ground up.
. Reinforce principles of object-oriented programming through practical implementation.
. Provide hands-on experience with abstract data types (ADTs) and their behaviors.
. Foster experimentation through interactive notebooks that visualize and test structure operations.

# Data Structures Implemented

The package features a collection of essential data structures, each built using class-based design and equipped with relevant methods:

| Data Structure            | Required Methods                              |
|---------------------------|-----------------------------------------------|
| Stack                     | `push()`, `pop()`, `peek()`, `is_empty()`     |
| Queue                     | `enqueue()`, `dequeue()`, `peek()`, `is_empty()` |
| Singly Linked List        | `insert()`, `delete()`, `search()`, `traverse()` |
| Binary Search Tree (BST)  | `insert()`, `search()`, `inorder_traversal()` |


Each implementation is encapsulated in its own class, following a modular and reusable coding style.

# Documentation Website
A comprehensive documentation site accompanies this package. Built using https://www.mkdocs.org/, it includes:
* Explanations of each data structure.
* Code samples and walkthroughs.
* Links to example notebooks.
* Installation and contribution guides.
* Visit the documentation at:

# Package Distribution
The package is published on the Python Package Index (PyPI), allowing it to be easily installed in any environment.

## Package Installation:
Open bash and run this command: 
pip install data-structures-py

## Example Usage:
Using a cPython compiler, run this pseudocode:
from data_structures.stack import Stack
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # Outputs: 20

The examples/ directory contains more detailed use cases for each data structure in notebook form.

# Development and Build Tools
The project follows modern Python packaging conventions using pyproject.toml. It includes all metadata required to build and distribute the package using tools such as build and twine. Developers can:

* Create a virtual environment
* Install dependencies like build and twine
* Build the project with python -m build
* Upload to PyPI using twine upload dist/*

The project also provides a solid foundation for contributing new data structures or extending existing functionality.

# Enhancements and Extras
🧾 Docstrings and Type Hints: Every method is fully documented and typed to ensure readability and maintainability.
📊 Visualization Support: Future updates will introduce visualization of structures using tools such as matplotlib and networkx.
🔬 Tutorial Notebooks: Interactive notebooks offer step-by-step exploration and testing of each class.
🌍 Public Website: All documentation is hosted for easy public access and continuous learning.

# License
This project is licensed under the MIT License, promoting open collaboration and reuse. See the LICENSE file for details.

# Contributions and Community
Contributions are welcome and encouraged. Whether it’s fixing a bug, adding a feature, or improving documentation, the goal is to create a helpful resource for anyone interested in learning about data structures.
For issues, pull requests, or ideas, please visit the https://github.com/wycliffenzomo/data-structures-python