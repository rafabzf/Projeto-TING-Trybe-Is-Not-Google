from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    duplicate = False

    for i in range(instance.__len__()):
        dict_find = instance.search(i)

        if path_file == dict_find["nome_do_arquivo"]:
            duplicate = True

    if not duplicate:
        file = txt_importer(path_file)

        dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(dict)
        sys.stdout.write(f"{dict}\n")


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        files = instance.dequeue()
        print(f"Arquivo {files['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        sys.stderr.write("Posição inválida")
