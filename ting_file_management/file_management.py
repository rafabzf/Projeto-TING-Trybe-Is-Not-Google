import sys


def txt_importer(path_file):
    final = path_file.endswith(".txt")
    if not final:
        print("Formato inválido", file=sys.stderr)
        return None
    try:
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
