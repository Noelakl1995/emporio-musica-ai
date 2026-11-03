# Empório da Música — Assistente Virtual com IA

## 1. Descrição do projeto

Este projeto foi desenvolvido como parte de um desafio técnico para a posição de AI Engineer na Artefact.

O objetivo é implementar um agente conversacional capaz de atender clientes de uma loja fictícia de instrumentos musicais chamada **Empório da Música**.

O agente utiliza o modelo de linguagem Google Gemini e a técnica de **Function Calling** para consultar informações reais disponibilizadas nos arquivos do desafio.

## 2. Funcionalidades

O assistente permite:

- Consultar instrumentos musicais disponíveis.
- Pesquisar produtos por nome, categoria e faixa de preço.
- Verificar preços e quantidades em estoque.
- Consultar o status de pedidos mediante número e e-mail.
- Responder perguntas sobre políticas da loja.
- Manter o contexto durante uma conversa.
- Identificar solicitações fora do escopo do atendimento.

## 3. Tecnologias utilizadas

- **Python:** linguagem principal.
- **Google Gemini API:** modelo de linguagem utilizado no atendimento.
- **Google Gen AI SDK:** integração com o modelo e execução de ferramentas.
- **Pandas:** leitura e consulta dos arquivos CSV.
- **PyMuPDF:** extração de texto do documento PDF.
- **python-dotenv:** gerenciamento de variáveis de ambiente.

## 4. Estrutura do projeto

```text
emporio-musica-ai/
├── data/
│   ├── arquivos CSV do desafio
│   └── documento PDF de políticas
├── src/
│   ├── agent.py
│   ├── tools.py
│   └── policies.py
├── examples/
│   └── conversas.md
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 5. Arquitetura e funcionamento

O agente utiliza Function Calling para conectar o modelo de linguagem às funções Python responsáveis por consultar os dados da loja.

O funcionamento ocorre da seguinte maneira:

1. O cliente envia uma mensagem pelo terminal.
2. O Gemini interpreta a solicitação.
3. Quando necessário, o modelo seleciona uma ferramenta.
4. A ferramenta executa uma consulta aos arquivos CSV ou ao PDF.
5. O resultado da consulta é enviado ao modelo.
6. O agente formula uma resposta em linguagem natural.

As principais ferramentas implementadas são:

| Ferramenta | Responsabilidade |
|---|---|
| `buscar_produtos()` | Consultar produtos por nome e preço |
| `buscar_por_categoria()` | Filtrar produtos por categoria e orçamento |
| `consultar_pedido()` | Consultar informações de pedidos |
| `buscar_politicas()` | Pesquisar informações nas políticas da loja |

A execução das ferramentas é realizada pelo SDK do Gemini.

## 6. Como executar

### Requisitos

- Python instalado.
- Acesso à API do Google Gemini.
- Arquivos de dados disponibilizados para o desafio.

### Instalação

Clone o repositório:

```bash
git clone https://github.com/Noelakl1995/emporio-musica-ai.git
cd emporio-musica-ai
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto:

```dotenv
GEMINI_API_KEY=sua_chave_aqui
```

Execute o assistente:

```bash
python main.py
```

## 7. Exemplos de utilização

### Consulta de produtos

**Cliente:** Quais violões disponíveis custam até R$ 1000?

**Assistente:** Apresenta os violões disponíveis encontrados no catálogo, incluindo nomes e preços.

### Consulta de pedidos

**Cliente:** Qual é o status do pedido número 1?

**Assistente:** Solicita o e-mail associado ao pedido e consulta os registros para apresentar o status.

### Política de devolução

**Cliente:** Quantos dias tenho para devolver um produto comprado pela internet?

**Assistente:** Informa o prazo de sete dias corridos após o recebimento, conforme a política da loja.

### Solicitações fora do escopo

**Cliente:** Você pode resolver uma equação matemática?

**Assistente:** Explica educadamente que é especializado no atendimento da Empório da Música.

## 8. Decisões técnicas

### Function Calling

Foi utilizado Function Calling para permitir que o modelo consulte os dados da loja por meio de funções Python, em vez de depender apenas de informações presentes no treinamento do modelo.

### Dados estruturados

Os arquivos CSV são processados com Pandas, permitindo consultas por nome, categoria, preço e disponibilidade.

### Políticas da loja

O documento PDF é processado com PyMuPDF. A implementação atual utiliza busca textual por termos para localizar informações relevantes.

### Histórico da conversa

O histórico permite que o agente mantenha o contexto entre mensagens, como quando o cliente informa o número do pedido e posteriormente fornece seu e-mail.

## 9. Limitações e melhorias futuras

- A disponibilidade do Gemini depende da API e das cotas da conta.
- A busca textual no PDF pode não encontrar termos semanticamente equivalentes.
- O modelo pode interpretar incorretamente resultados das ferramentas.
- A consulta de pedidos por número e e-mail não constitui autenticação segura para um ambiente de produção.
- O protótipo utiliza uma interface de terminal.

Possíveis melhorias incluem busca semântica no PDF, testes automatizados, autenticação de clientes e uma interface web.

## 10. Contexto

Projeto desenvolvido para fins de avaliação técnica, utilizando dados de uma loja fictícia de instrumentos musicais.