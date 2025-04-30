# Otimizando Modelos de Azure AI Foundry com Retrieval Augmented Generation (RAG)

## Fundamentando um Copilot com seus próprios dados
---
Os modelos de linguagem criam respostas coerentes às perguntas, mas em que se baseam essas respostas?

A **fundamentação** fornece contexto específico ao modelo para fornecer respostas precisas e relevantes.

**Não fundamentado:**
* Qual produto eu deeria usar para o X?
> Vai gerar uma resposta gramaticamente correta, mas descontextualizada.

**Fundamentado**
Carrega uma base de dados/Catálogo de produtos
Qual produto eu deveria usar para o X?
> Resposta contextualizada

## Retrieval Augmented Generation (RAG)
---
Uma **RAG** reúne dados relevantes para incluir no prompt para que o modelo de linguagem utilize como contexto de fundamentação.

Um **padrão RAG** é um design arquitetural para RAG, incluindo dados relevantes recuperados no prompt:

1. **Recuperar** dados de fundamentação com base na entrada do usuário.
2. **Aprimorar** o prompt com dados de fundamentação.
3. **Gerar** uma resposta contextualizada.


Os dados são armazenados como embbedings em um **indíce de busca baseado em vetores**.

Embbedings permitem uma melhor recuperação de dados para *similaridades semânticas* nos resultados de busca.

## Adicione seus dados em um fluxo de prompt
---
Par afundamentar as respostas do seu modelo de linguagem, adicione sua própria fonte de dados para recuperar o contexto relevante:

1. Adicione seus **dados** a um projeto Azure AI.
2. Indexe seus dados com o **Azure AI Search**
3. Consulte seus dados indexados em um fluxo de prompt com a ferramenta **Index Lookup**.
4. Referencie o **contexto** recuperado no prompt.
5. Envie o prompt com o contexto para um **LLM**.

A resposta gerada será fundamenta pelo contexto recuperado.