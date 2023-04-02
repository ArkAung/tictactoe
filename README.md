# Tic Tac Toe

A simple Tic Tac Toe game built with Python and Tkinter.

## Table of Contents

- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Building the Application](#building-the-application)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project, you should have Python 3.7 or higher and Poetry installed on your machine.

1. Clone the repository:

```bash
git clone https://github.com/<username>/tictactoe.git
cd tictactoe

2. Install the project dependencies using Poetry:
```bash
poetry install
```

## Running the Application
To run the Tic Tac Toe game, you can use the run Makefile target:

```bash
make run
```

Alternatively, you can run the game directly using Python:

```bash
poetry run python -m tictactoe.tictactoe
```

## Building the Application
To build the Tic Tac Toe game into a standalone binary, you can use the build Makefile target:

```bash
make build
```
This will generate a standalone binary in the dist directory.

## Running Tests
To run the unit tests for the Tic Tac Toe game, you can use the test Makefile target:

```bash
make test
```
Alternatively, you can run the tests directly using Python:

```bash
poetry run python -m unittest discover tests
```

## Contributing
We welcome contributions from the community. To contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository:
```bash
git clone https://github.com/<your-username>/tictactoe.git
cd tictactoe
```
3. Create a new branch for your changes:
```bash
git checkout -b feature/<your-feature-name>
```
4. Make your changes and commit them using Conventional Commits format:
```bash
git add .
git commit -m "<type>(<scope>): <description>"
```
5. Push your branch to your forked repository:
```bash
git push -u origin feature/<your-feature-name>
```
6. Create a pull request (PR) to merge your branch into the main branch.
Please ensure that your commit messages follow the Conventional Commits specification to ensure that the project conforms to semantic versioning.

## License
This project is licensed under the MIT License - see the LICENSE file for details.