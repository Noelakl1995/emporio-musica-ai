
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def carregar_produtos():
    arquivo = DATA_DIR / "desafio_tecnico_ai_eng - products.csv"
    return pd.read_csv(arquivo)


def buscar_produtos(nome="", preco_maximo=None):
    produtos = carregar_produtos()

    # Apenas produtos ativos e com estoque
    produtos = produtos[
        (produtos["status"] == "active")
        & (produtos["stock_quantity"] > 0)
    ]

    # Filtrar pelo nome do instrumento
    if nome:
        produtos = produtos[
            produtos["name"].str.contains(
                nome, case=False, na=False, regex=False
            )
        ]

    # Filtrar pelo preço máximo
    if preco_maximo is not None:
        produtos = produtos[
            produtos["price_brl"] <= preco_maximo
        ]

    return produtos[
        ["product_id", "name", "price_brl", "stock_quantity"]
    ].to_dict(orient="records")


def buscar_por_categoria(categoria, preco_maximo=None):
    # 1. Carregar os produtos
    produtos = carregar_produtos()

    # 2. Carregar as categorias
    arquivo = DATA_DIR / "desafio_tecnico_ai_eng - categories.csv"
    categorias = pd.read_csv(arquivo)

    # 3. Relacionar produtos e categorias
    dados = pd.merge(
        produtos,
        categorias,
        on="category_id",
        how="inner",
        suffixes=("_produto", "_categoria")
    )

    # 4. Filtrar pela categoria
    dados = dados[
        dados["name_categoria"].str.contains(
            categoria,
            case=False,
            na=False,
            regex=False
        )
    ]

    # 5. Selecionar produtos ativos e com estoque
    dados = dados[
        (dados["status"] == "active") &
        (dados["stock_quantity"] > 0)
    ]

    # 6. Filtrar pelo preço máximo
    if preco_maximo is not None:
        dados = dados[
            dados["price_brl"] <= preco_maximo
        ]

    # 7. Retornar as informações
    return dados[
        [
            "product_id",
            "name_produto",
            "price_brl",
            "stock_quantity",
            "name_categoria"
        ]
    ].to_dict(orient="records")


def buscar_por_categoria(categoria, preco_maximo=None):
    # 1. Carregar os produtos
    produtos = carregar_produtos()

    # 2. Carregar as categorias
    arquivo = DATA_DIR / "desafio_tecnico_ai_eng - categories.csv"
    categorias = pd.read_csv(arquivo)

    # 3. Relacionar produtos e categorias
    dados = pd.merge(
        produtos,
        categorias,
        on="category_id",
        how="inner",
        suffixes=("_produto", "_categoria")
    )

    # 4. Filtrar pela categoria
    dados = dados[
        dados["name_categoria"].str.contains(
            categoria,
            case=False,
            na=False,
            regex=False
        )
    ]

    # 5. Selecionar produtos ativos e com estoque
    dados = dados[
        (dados["status"] == "active") &
        (dados["stock_quantity"] > 0)
    ]

    # 6. Filtrar pelo preço máximo
    if preco_maximo is not None:
        dados = dados[
            dados["price_brl"] <= preco_maximo
        ]

    # 7. Retornar as informações
    return dados[
        [
            "product_id",
            "name_produto",
            "price_brl",
            "stock_quantity",
            "name_categoria"
        ]
    ].to_dict(orient="records")


def consultar_pedido(numero_pedido, email_cliente):
    # 1. Carregar os pedidos
    arquivo_pedidos = DATA_DIR / "desafio_tecnico_ai_eng - orders.csv"
    pedidos = pd.read_csv(arquivo_pedidos)

    # 2. Carregar os clientes
    arquivo_clientes = DATA_DIR / "desafio_tecnico_ai_eng - customers.csv"
    clientes = pd.read_csv(arquivo_clientes)

    # 3. Relacionar pedidos com clientes
    dados = pd.merge(
        pedidos,
        clientes,
        on="customer_id",
        how="inner"
    )

    # 4. Procurar o pedido e conferir o e-mail
    resultado = dados[
        (dados["order_id"] == int(numero_pedido)) &
        (
            dados["email"].str.strip().str.lower()
            == email_cliente.strip().lower()
        )
    ]

    # 5. Verificar se encontrou
    if resultado.empty:
        return {
            "mensagem": "Pedido não encontrado ou dados não conferem."
        }

    # 6. Retornar apenas os dados necessários
    pedido = resultado.iloc[0]

    return {
        "numero_pedido": int(pedido["order_id"]),
        "status": pedido["status"],
        "data_pedido": str(pedido["order_date"]),
        "previsao_entrega": (
            str(pedido["estimated_delivery"])
            if pd.notna(pedido["estimated_delivery"])
            else None
        )
    }



if __name__ == "__main__":
    print("=== CONSULTA DE PEDIDO ===")

    numero = input("Digite o número do pedido: ")
    email = input("Digite o e-mail do cliente: ")

    resultado = consultar_pedido(numero, email)

    print("\n=== RESULTADO ===")

    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")
