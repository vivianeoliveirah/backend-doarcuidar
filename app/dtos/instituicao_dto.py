def instituicao_to_dict(data):
    return {
        "id": data.get("id"),
        "nome": data.get("nome"),
        "cidade": data.get("cidade"),
        "estado": data.get("estado"),
        "descricao": data.get("descricao")
    }