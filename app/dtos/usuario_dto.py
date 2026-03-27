def usuario_to_dict(data):
    return {
        "id": data.get("id"),
        "nome": data.get("nome"),
        "email": data.get("email")
    }