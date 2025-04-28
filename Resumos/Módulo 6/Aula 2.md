# Explore e Implante Modelos do Catálogo do Azure AI Foundry

## Selecione um modelo usando uma abordagem estruturada 
---

### Como a IA pode resolver meu caso?
* Defina casos de uso
* Selecione um modelo
* Estabeleça a viabilidade
* Construa um protótipo

### Como seleciono o modelo "certo" para meu caso de uso?
* Selecione um modelo
* Engenharia de Prompt
* Retrieval Augmented Generation (RAG)
* Afinação (Fine Tuning)

### Posso escalar para cargas de trabalho do mundo real?
* Filtragem de conteúdo
* Segurança e privacidade de dados
* Compensações de capacidade e custos
* Monitoramento

* Adicionar tipos diferentes dependendo da demanda
* Nível de complexidade: Mais simples, LLMs mais baratos. Mais complexos, LLMs mais caros e com fine tuning, por exemplo.
* Segurança no input e output da IA

## Crie um protótipo para resolver o caso de uso
---
### LLMs vs SLM (Large Models vs Small Models)
**Large Language Models**
* GPT-4
* Mistral Large
* Llama3 70b
* Llama 405B
* Command R, R+

**Small Language Models**
* Phi3
* Mistral OSS models
* Llama3 8b

### Modalities, tasks and tools
**Multi-modal**
* GPT-4o
* Phi3-vision
**Image generation**
* Dalle3
* Stability AI
**Embedding models**
* Ada
* Cohere

**Function calling & JSON support**

### Regional and domain specific
* Core42 JAIS Arabic language LLM
* Mistral Large is focused on European languages
* Nixtla TimeGEN-1 Timeseries forecasting

### Open and property
**Premium models first on Azure**
* OpenAI, Mistral Large, Cohere Command R+

**100s of Open models from HuggingFace**

**Open models from Meta, Databricks, Snowflakes, NVIDIA**


## Avalie o desempenho do modelo
---

Avalie o desempenho do seu mode em diferentes fases, usando diversas abordagens:
* Referencias do modelo - COmpare métricas disponíveis publicamente entre modelos e conjundo de dados.
* Avaliações manuais - Avalie respostas do seu modelo
* **Métricas tradicionais de aprendizado de máquina** - Meça a proporção do número de palavras compartilhadas entre as respostas geradas e as respostas verdadeiras
* **Métricas assistidas por IA** - Métrica de risco e segurança; Métricas de qualidade de geração.

## Entenda os benchmarks do modelo
---

Os conjuntos de dados estão disponíveis publicamente para calcular benchmarks individuais e comparar modelos.

Alguns benchmarks comumente utilizados são:
* **Precisão**: Compara o texto gerado pelo modelo com a resposta correta de acordo com o conjunto de dados. O resultado será um se o texto gerado corresponder exatamente à resposta e zero caso contrário.

* **Fluência**: Avalia até que ponto o texto geradoa dere às regras gramaticais, estruturas sintáticas e uso apropriado do vocabulário, resultando em repostas linguisticamente corretas e com som natural.

* **Coerência**: mede se a saída do modelo flui suavemente, se élida naturalmente e se se assemelha à linguagem humana.

* **Similaridade GPT**: quantifica a semelhança entre uma frase (ou documento) verdadeira e a frase de previsão gerada por um modelo de IA.


## Otimize a precisão após selecionar um modelo
---

* Otimize o contexto quando o modelo não tiver conhecimento contextual e você quiser maximizar a precisão da resposta

* Otimize o modelo quando quiser melhorar o formato, o estilo ou a fala da resposta, maximizando a consistência do comportamento.


```mermaid
quadrantChart
    title Otimização de Modelo vs Otimização de Contexto
    x-axis Otimização de modelo --> Como o modelo precisa agir
    y-axis Otimização de contexto --> O que o modelo precisa saber
    quadrant-1: Estratégias combinadas
    quadrant-2: RAG
    quadrant-3: Engenharia de prompt
    quadrant-4: Ajuste fino
```

## Otimize o desempenho para se preparar para a escala
---