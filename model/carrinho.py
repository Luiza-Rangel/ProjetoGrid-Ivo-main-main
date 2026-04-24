from database.conexao import conectar

def recuperar_carrinho(usuario: str) -> list:
    conexao, cursor = conectar()
    cursor.execute(""" SELECT carrinhos.cod_carinho, 
        usuarios.usuario, 
        carrinhos.data, 
        carrinhos.finalizado,
        itens.produto,
        itens_carrinho.quantidade,
        itens.preco,
        itens.imagem
    FROM carrinhos
    INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
    INNER JOIN itens ON itens.codigo = itens_carrinho.cod_produto
    WHERE usuarios.usuario = "Godofredo";
                    """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado