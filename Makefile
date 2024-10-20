# Makefile
basic-typing:
	mypy basic/main.py

intermediate-typing:
	mypy intermediate/main.py

typing:
	mypy basic/main.py
	mypy intermediate/main.py