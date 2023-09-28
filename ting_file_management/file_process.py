from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for item in list(instance.queue):
        if item["nome_do_arquivo"] == path_file:
            return
    info_txt = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(info_txt),
        "linhas_do_arquivo": info_txt
    }

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementaçã"""
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    remove_file = instance.dequeue()["nome_do_arquivo"]
    str_case_sucess = f"Arquivo {remove_file} removido com sucesso\n"

    return sys.stdout.write(str_case_sucess)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
