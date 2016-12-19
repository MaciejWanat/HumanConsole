# Ludzka konsola

Jest to program w Pythonie który na wejściu przyjmuje polecenia w języku naturalnym, przetwarza je oraz wykonuje.
Jest on przeznaczony pod platformę Windows. Program działa zapomocą lexera i parsera PLY.

Funkcjonalność:
- uruchamianie programów
- uruchamianie plików (jeśli podamy ścieżkę)
- otwieranie linków (jeśli podamy link)
- otwieranie wielu programów/plików jedną komendą
- zamykanie programów

Przykładowe wejście:
- czy mógłbyś otworzyć notatnik, proszę?
- prosze otwórz painta i jeśli byś mógł, to również worda
- teraz zamknij painta i worda
- czy mógłyś uruchomić www.google.pl?
- otwórz mi plik C:\temp\a.txt

Obsługiwane programy:
- notatnik
- word
- excel
- access
- wiersz poleceń (cmd)
- sublime text
- putty
- chrome
- firefox
- filezilla
- skype
- steam

Testowany na Office 2010.

Pliki:
- consolePL.py - polska wersja konsoli (pełna funkcjonalność)
- console.py - angielska wersja konsoli (wczesna wersja rozwojowa)
- sub.py - plik z funkcją pomocniczą zamieniającą nazwy programów na nazwy procesów 
- regex.txt - plik zawierający definicje tokenów

# Human Console

It's a program that processes natural language input and executes it.
Works on Windows platfrom. Program works with PLY lexer & parser.

Features:
- turning programs on
- executing files (if path is given)
- opening links (if link is given)
- opening more than one program with one command
- closing programs

Example input:
- open paint
- close paint
- open www.google.pl
- open C:\temp\a.txt

Files:
- consolePL.py - polish version of human console (full functionality)
- console.py - english version of human console (low functionality)
- sub.py - file with function that switches names of programs for names of processes
- regex.txt - file containing token definitions