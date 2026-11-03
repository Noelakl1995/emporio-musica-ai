
from pathlib import Path
import pymupdf

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def carregar_politicas():
    arquivo = DATA_DIR / "políticas_da_loja.pdf"

    if not arquivo.exists():
        return "Arquivo de políticas não encontrado."

    paginas = []

    with pymupdf.open(arquivo) as pdf:
        for numero, pagina in enumerate(pdf, start=1):
            texto = pagina.get_text("text")

            paginas.append({
                "pagina": numero,
                "texto": texto
            })

    return paginas


def buscar_politicas(termo):
    paginas = carregar_politicas()

    if isinstance(paginas, str):
        return paginas

    resultados = []

    for pagina in paginas:
        if termo.lower() in pagina["texto"].lower():
            resultados.append(pagina)

    return resultados


if __name__ == "__main__":
    resultados = buscar_politicas("devolução")

    for resultado in resultados:
        print("Página:", resultado["pagina"])
        print(resultado["texto"])
        print("-------------------------")
