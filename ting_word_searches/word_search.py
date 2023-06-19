def exists_word(word, instance):
    files = []
    for file in range(len(instance)):
        info = instance.search(file)
        name = info["nome_do_arquivo"]
        lines = info["linhas_do_arquivo"]
        res = []
        for i, l in enumerate(lines):
            if word.lower() in l.lower():
                res.append({
                    "linha": i + 1
                })
        if res:
            result = {
                "palavra": word,
                "arquivo": name,
                "ocorrencias": res
            }
            files.append(result)
    return files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
