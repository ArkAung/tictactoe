.PHONY: test build run clean

test:
	poetry run python -m unittest discover tests

build:
	poetry run pyinstaller --onefile --name tictactoe --add-data 'tictactoe.py:tictactoe' --specpath ./tictactoe -c tictactoe/tictactoe.py

run:
	poetry run python -m tictactoe.tictactoe

clean:
	rm -rf build/ dist/ __pycache__/ tictactoe/tictactoe.spec
