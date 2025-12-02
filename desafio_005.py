# Contar quantidade de vogais

texto = """
Python is a high-level programming language designed for readability and simplicity, created by Guido van Rossum in 1990 while working at the Centrum Wiskunde & Informatica (CWI) in Amsterdam, Netherlands.[12] Its implementation began in December 1989 as a successor to the ABC language, with the first public release occurring in February 1991.[13] Python enforces code structure through significant whitespace indentation rather than delimiters like braces, a deliberate choice to reduce syntactic noise and promote consistent formatting.[14] The language is interpreted via an interactive shell, dynamically typed—meaning variable types are determined at runtime—and employs automatic garbage collection for memory management, avoiding manual allocation common in lower-level languages.
"""
vogal_total = {
    'a': 0, 
    'e': 0, 
    'i': 0, 
    'o': 0, 
    'u': 0,
}

for letra in texto.lower():
    if letra in vogal_total:
        vogal_total[letra] += 1

for letra, total in vogal_total.items():
    print(f'Vogal {letra.upper()}: {total}')