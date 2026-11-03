
from src.agent import responder


def main():
    print("=" * 45)
    print("Bem-vindo à Empório da Música!")
    print("Assistente virtual de atendimento")
    print("Digite 'sair' para encerrar.")
    print("=" * 45)

    historico = None

    while True:
        try:
            mensagem = input("\nVocê: ").strip()

            if mensagem.lower() == "sair":
                print("Obrigado pelo contato!")
                break

            if not mensagem:
                continue

            resposta, historico = responder(
                mensagem,
                historico
            )

            print("\nAssistente:", resposta)

        except KeyboardInterrupt:
            print("\nObrigado pelo contato!")
            break

        except EOFError:
            print("\nObrigado pelo contato!")
            break

        except Exception as erro:
            if "503" in str(erro) and "UNAVAILABLE" in str(erro):
                print(
                    "\nAssistente: O serviço de IA está "
                    "temporariamente sobrecarregado. "
                    "Tente novamente daqui a alguns minutos."
                )

            elif "429" in str(erro):
                print(
                    "\nAssistente: O limite de uso da API "
                    "foi atingido. Verifique sua cota."
                )

            else:
                print(
                    "\nErro ao consultar o agente:",
                    erro
                )


if __name__ == "__main__":
    main()
