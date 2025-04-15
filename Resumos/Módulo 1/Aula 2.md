# Ferramentas de Desenvolvimento com Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Explorando Ferramentas de Interação com o Workspace
---

### Explorar o estúdio

- Inicie o Estúdio a partir da página Visão geral no portal Azure > Launch Studio
- Navegue diretamente para [Azure Machine Learning Studio](https://ml.azure.com)

1. Home
2. Catálogo

#### Authoring

1. Notebooks
2. Automated ML: escolhe o melhor algoritmo para o modelo e iterar sobre os hiperparâmetros para maximizar a performance do algoritmo. O melhor é estudar em cima de cada modelo/algoritmo para entender qual o melhor para cada modelo.
3. Designer: Alguns modelos default e você pode criar fluxo de ML com drag and drop.
4. Prompt Flow: cria fluxo da parte de prompts LLM

#### Assets

1. Data: dados utilizados
2. Jobs: Jobs criados e em execução
3. Components: componentes de código ou outros modelos
4. Pipelines
5. Environment: Quais os componentes que precisa que rode o modelo, sistema operacional, parâmetros do python, biblioteca, descrição do ambiente, ou default.
6. Models: Quando processa o modelo ele aparece em Models.
7. Endpoint: Fazer chamada para o modelo neste endpoint

#### Manage

1. Compute: Instâncias, clusters, kubernetes, attach compute ou serverless
2. Monitoring
3. Data Labeling: Label nas informações
4. Linked Services
5. Connections

## Explorar SDK do Python
---

1. Instalar o SDK do Python (biblioteca)

```
pip install azure-ai-ml
```

2. Conectar-se ao workspace

```
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
```

Necessário workspace, conexão com a azure, acessos ao portal já criados. Para permitir o acesso, manipulação e sincronização com a própria máquina.


## Explorar a CLI (Linha de Comando)
---

A CLI da Azure costuma ser usada por administradores e engenheiros para automatizar tarefas no Azure.

- Criar fluxo de trabalho de DevOps/MLOps
- Criar código repetível


- Automatizar a criação e a configuração de ativos e recursos para torná-la **repetível**.
- Garantir a **consistência** dos recursos que precisam ser replicadas em vários ambientes.
- Incorporar a configuração de ativos de aprendizado de máquina em **fluxos de trabalho das DevOps (operações de desenvolvedor)**, tais como pipelines de **integração contínua** e de  **implantação contínua** (CI/CD).


1. Instalar no Windows

```
az extension add -n ml -y
```

2. Trabalhar com a CLI do Azure

```
az ml compute create --file compute.yml --resource-group my-resource --workspace-name my-workspace
```

## Materiais de Apoio
---

Os materiais complementares e de apoio que oferecemos têm como objetivo fornecer informações para facilitar e enriquecer a sua jornada de aprendizado no curso "**Ferramentas de Desenvolvimento com Azure Machine Learning**". Aqui você encontrará links úteis, como slides, repositórios e páginas oficiais, além de dicas sobre como se destacar na DIO e no mercado de trabalho 😉

### Recursos Adicionais
---
Durante este conteúdo, compreendemos os fundamentos da engenharia de prompts. Para ajudá-lo a aprofundar o conhecimento, disponibilizamos a seguir o material complementar contendo os conteúdos e links apresentados no curso:

Slide: [Ferramentas de Desenvolvimento com Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/92bc2fa6-3861-42df-875f-a49dbde389a2.pptx)

### Dicas e Links Úteis
___

Para se desenvolver ainda mais e se destacar na DIO e no mercado de trabalho, sugerimos os seguintes recursos:

> [Artigos e Fórum da DIO](https://web.dio.me/articles): Compartilhe seus conhecimentos e dúvidas através dos artigos (visíveis globalmente na plataforma da DIO) e nos fóruns específicos para cada experiência educacional, como nossos Bootcamps.

> Rooms: Participe do Rooms, uma ferramenta de bate-papo em tempo real onde você pode interagir com outros participantes dos nossos Bootcamps, compartilhando dúvidas, dicas e snippets de código.

> Exploração na Web: Utilize motores de busca para aprofundar seu conhecimento sobre temas específicos. Páginas como o [StackOverflow](https://stackoverflow.com/) são recursos valiosos para encontrar soluções e expandir seu entendimento.

Com esses materiais complementares, você estará bem equipado para explorar todo o potencial e se destacar em suas iniciativas. Continue aproveitando as oportunidades de aprendizado, e não hesite em buscar mais conhecimento e compartilhar suas descobertas com a comunidade!
