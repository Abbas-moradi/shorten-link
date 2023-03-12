from os import system as terminal, name as os_name


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


def banner(name: str):
    clear()
    print()
    print('#' * 40, name.title().center(40), '#' * 40, sep="\n")
