# Introdução ao Azure AI Foundry

## Otimize modelos de linguagem para aplicações generativas de IA
---
AI Foundry: Hub de criação e gerenciamento de aplicativos de IA Generativa

* Explore e implemente modelos do catálogo de modelos
* Otimize o desempenho do modelo por meio da engenharia de prompt
* Otimize por meio de Retrieval Augmented Generation (RAG)
* Otimize através do ajuste fino

## Introdução ao Azure AI Foundry
---
* Workspace da IA Generativa dentro da Azure

Três pilares principais:

### 1. Componentes

* Hubs
* Projetos
* Connections:
    * Azure OpenAI
    * Azure AI Services
        * Language
        * Speech
        * Vision
    * Storage
    * Key Vault

### 2. Interface

* Playgrounds para testar LLM 
* Model catalog: comparações entre datasets
* Outros serviços
* Código
* Fine Tunning
* Prompt flow
* Tracing
* Evaluate
* Datasets
* Index
* Compartilhamento 
* ...

### 3. Tipos de Modelos / Região

**Global Standard**
Recomendado para playgrounds iniciantes.
**Global Batch**
Pontuação Offline
**Standard**
Para clientes com requerimentos específicos para os dados
**Provisioned-managed**
Pontuação em tempo-real, alta volumetria, especificidades de datasets.

## Configure o Azure AI Foundry
---
* Gerencie com **hubs**
* Crie aplicativos em um **projeto**
* Configure **conexões**

> PORTAL AZURE > Azure AI Foundry > Instancia do AI Foundry (Workspace)

* Criar novo Projeto
    * Model + endpoints
    * Vincula a um Azure Blobstorage
    * Compartilhamento
    * Conexões
    * Model Deployments


## Construa e personalize
---
* Selecione um modelo
* Adicione seus dados
* Orquestre fluxos de trabalho


## Implemente um modelo
---

* Selecione o tipo de implantação
* Personalize o limite da taxa de tokens por minuto
* Considere a disponibilidade regional