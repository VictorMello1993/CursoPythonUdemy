from bd import nova_conexao

with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Sessão estabelecida com sucesso!')

print('Fim!')
