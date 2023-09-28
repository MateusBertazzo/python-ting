def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []

    def is_word_in_line(line):
        return word.lower() in line.lower()

    for new in instance.queue:
        info_txt = {
            "palavra": word,
            "arquivo": new["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": line_index + 1} for line_index, line in enumerate(
                    new["linhas_do_arquivo"]) if is_word_in_line(line)]
        }
        if info_txt["ocorrencias"]:
            result.append(info_txt)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
