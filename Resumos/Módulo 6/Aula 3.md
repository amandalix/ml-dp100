# Otimizando Modelos de Azure AI Foundry com Engenharia de Prompt

## Aplicar engenharia de prompt
---
Para melhorar a saída do modelo como usuário, você pode aplicar engenharia de prompt:
* Forneça instruções claras
* Formate suas instruções
* Use dicas

* Prompts de sistemas para facilitação do atendimento do chatbot.

## Atualizar a mensagem do sistema
---
System message: O prompt do sistema que vai alimentar o contexto para o modelo a ser utilizado pelo usuário final.

Para melhorar o resultado do modelo como desenvolvedor, você pode atualizar a mensagem do sistema:
* Use uma/poucas shots
* Use cadeia de pensamento
* Adicione contexto

## Prompty como um ativo de prompt independente da linguagem
---
Forma organizada de estruturar os prompts de sistema.

* Fácil de começar
* Codifique primeiro
* Intuitivo para desenvolver
* Várias linguagens de programação serão suportadas
* Implantação simplificada
* Observabilidade por meio de rastreamento
* Escolha a estrutura

> Exemplo .yaml
```yaml
name: Basic Prompt
description: A basic prompt that uses the GPT-3 chat API to answer questions
authors:
    - sethjuarez
    - jietong
mode:
    api: chat
    configuration:
        azure_deployment: gpt-35-turbo
sample:
    firstName: Jane
    lastName: Dow
    question: What is the meaning of life?
---
system:
You are an AI assistant....

# Customer
You are helping {{firstName}} {{lastName}}....

user:
{{question}}
```

