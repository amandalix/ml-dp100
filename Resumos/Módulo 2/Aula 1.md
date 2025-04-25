# Explorando o Machine Learning Automatizado

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Introdução
___
- Explorar o Machine Learning Automatizado: criar experimentos automatizados e a plataforma escolhe os parâmetros.
- Encontrar o melhor modelo de classificação com o Machine Learning Automatizado
- Acompanhar o treinamento de modelos em notebooks com o MLflow

## Explorar o Machine Learning Automatizado
___
> Também chamado de AutoML
- Treine vários modelos em paralelo, variando o pré-processamento e a seleção de algortimos.
- Encontre o "melhor" modelo com base em uma métrica.
- Paraleliza todos os modelos e depois demonstra um ranking com base nos seus dados.
- Itera todos os algortimos e retorna o melhor

|Algortimos||
|---|---|
|LogisticRegression||
|DecisionTree||
|LinearSVM||

## Machine Learning Studio
___
>**Authoring > Automated ML > New Automated ML job**

1. Basic settings
    - Definir o jobname
    - Definir o nome do Experimento
    - Descrição
    - Tags

2. Tipo de tarefa e dados
    - Selecionar tipo de tarefa: Classificação (exemplo)
    - Selecionar os dados
3. Review e treinar
4. Gera um job e fica rodando, para printar as métricas de acurácia do modelo.

## Escolha uma tarefa
___
Os dados de treinamento, opções de definição de recursos, algoritmos e métricas de desempenho dependerão da tarefa escolhida.

|Tipo de tarefa|Descrição|
|---|---|
|Classificação|Prever um valor categórico|
|Regressão|Prever um valor numérico|
|Previsão de série temporal|Prever valores numéricos futuros com base em dados de séries temporais.|
|Pesquisa Visual Computacional|Classifica imagens ou detecta objetos em imagens|
|NLP (Processamento de linguagem natural|Classificação de textos ou reconhecimento de entidade nomeada|

Cada tipo terá parâmetros específicos e modelos específicos para iterar.

> Resulta no melhor modelo e a acurácia desse modelo sugerido


## Explorar o Machine Learning Automatizado
___

> [Learn about AutomatedML](https://learn.microsoft.com/pt-br/azure/machine-learning/tutorial-first-experiment-automated-ml?view=azureml-api-2)

- Coluna y do arquivo de exemplo: Indica se um cliente assinou um depósito a prazo fixo > "Assinou ou não assinou"
- Vários clientes e informações dos clientes
    - idade
    - moradia
    - contato
    - data de assinatura
    - etc...
- Com base nas características, prever se o cliente vai Assinar ou não um depósito a prazo fixo.
- Identificar a função que representa o comportamento de um cliente com base nas suas características.

> Slide: [Identificação do Melhor Modelo de Classificação com Machine Learning Automatizado.pptx](https://hermes.dio.me/files/assets/e118c1d0-1979-4a8d-99cd-b5d0262ff53d.pptx)




