# Exemplos de conversas — Empório da Música

Este documento apresenta cinco cenários de atendimento do assistente virtual desenvolvido para o desafio técnico da Artefact.

Os exemplos demonstram consultas ao catálogo de produtos, acompanhamento de pedidos, políticas da loja e tratamento de solicitações fora do escopo.

## Exemplo 1 — Consulta de produtos por categoria e preço

**Cliente:** Quais violões disponíveis custam até R$ 1000?

**Ferramenta executada:** `buscar_por_categoria()`

**Assistente:**

Olá! Temos diversos modelos de violões disponíveis por até R$ 1000,00. Confira as opções:

- Yamaha C40 Nylon Natural — R$ 599,90
- Yamaha C70 Nylon Natural — R$ 849,00
- Tagima Memphis AC-39 Nylon Natural — R$ 429,90
- Giannini GN-15 Nylon Cedr Natural — R$ 689,00
- Rozini RC-104 Nylon Estudante — R$ 459,90
- Tagima Dallas Tuner Aço Natural — R$ 749,00
- Yamaha F310 Aço Natural — R$ 699,90
- Giannini GF-1R Aço Folk Sunburst — R$ 579,90
- Shelby SN-100 Folk Aço Preto — R$ 549,00
- Tagima Woodstock Dreadnought Natural — R$ 899,00
- Shelby SGD-195E Elétrico Aço Sunburst — R$ 799,00
- Tagima TW-7 7 Cordas Aço Natural — R$ 999,00

**Resultado:** O agente consultou o catálogo CSV e apresentou os 12 violões disponíveis dentro do orçamento informado.

---

## Exemplo 2 — Consulta de pedido

**Cliente:** Qual é o status do pedido número 1?

**Assistente:** Solicita o e-mail associado ao pedido.

**Cliente:** O número do pedido é 1 e o e-mail é pedro.oliveira@jmail.com.

**Ferramenta executada:** `consultar_pedido()`

**Assistente:**

O status do seu pedido número 1 é: **Entregue**.

Aqui estão os detalhes:

- Data do pedido: 15/10/2025
- Previsão de entrega: 25/10/2025

**Resultado:** O agente consultou os arquivos CSV de pedidos e clientes, utilizando o número do pedido e o e-mail informado.

---

## Exemplo 3 — Pedido não encontrado

**Cliente:** Qual é o status do pedido número 1?

**Cliente:** lucas.mendes@jmail.com

**Ferramenta executada:** `consultar_pedido()`

**Assistente:**

Sinto muito, mas não conseguimos localizar o pedido número 1 com o e-mail informado. Por favor, verifique se o número do pedido e o e-mail estão corretos e tente novamente.

**Resultado:** O agente não apresentou os dados do pedido porque as informações fornecidas não correspondiam ao registro consultado.

---

## Exemplo 4 — Política de devolução

**Cliente:** Comprei um instrumento pela internet. Quantos dias tenho para solicitar a devolução?

**Ferramenta executada:** `buscar_politicas()`

**Assistente:**

De acordo com a nossa política de trocas e devoluções para compras online, você tem até **7 (sete) dias corridos após o recebimento do produto** para solicitar a devolução por direito de arrependimento, sem a necessidade de justificativa.

Para que a devolução seja aceita, o produto deve estar em sua embalagem original, sem sinais de uso e com todos os acessórios e manuais.

**Resultado:** O agente consultou o documento PDF de políticas da loja e apresentou as condições de devolução.

---

## Exemplo 5 — Solicitação fora do escopo

**Cliente:** Você pode resolver uma equação de matemática para mim?

**Assistente:**

Como assistente virtual da Empório da Música, meu foco principal é atender às suas necessidades relacionadas aos nossos produtos, serviços e políticas da loja.

Embora eu não tenha como função resolver equações matemáticas, se houver algo em que eu possa ajudar referente aos nossos instrumentos ou pedidos, estou à total disposição!

**Resultado:** O agente reconheceu uma solicitação fora do escopo e respondeu educadamente, mantendo o foco no atendimento da loja.

---

## Considerações

Os exemplos demonstram o uso de Function Calling para consultar informações estruturadas e documentos da loja.

As respostas foram observadas durante os testes do protótipo. A qualidade das respostas pode variar conforme o modelo e a disponibilidade da API.

A consulta de pedidos utiliza dados fictícios e não representa um mecanismo de autenticação adequado para produção.