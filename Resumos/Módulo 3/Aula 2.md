# Acompanhar métricas com o MLflow e Habilitar o autoregistro

O MLflow é uma plataforma de código aberto que foi projetada para gerenciar o ciclo de vida completo do aprendizado de máquina.

Há duas opções para acompanhar os trabalhos de aprendizado de máquina com o MLflow:

* Habilitar o log automático usando **mlflow.autolog()** -> obter os logs de todo o processamento do treinamento, permitindo o trackeamento desde o início até quando está sendo consumido.
* Usar funções de log para acompanhar métricas personalizadas usando o **mlflow.log_***

Inclua o **mlflow** e **azureml-mlflow** no ambiente para garantir que os pacotes pip sejam instalados na computação antes de executar o script.

Dessa forma, permite-se trackear todo o processamento do modelo.

Também pode ser instalado em máquina local.

## Habilitar o autoregistro
---
Ao trabalhar com uma das bibliotecas comuns para aprendizado de máquina, você pode habilitar o **registro em log automático** no MLflow.

O registro em log automático registra **parâmetros, métricas e artefatos** de modelos sem que seja necessário especificar o que precisa ser registrado.

>Python
```py
import mlflow

mlflow.autolog()
```
## Registrar métricas personalizadas com o MLflow
---
Além do autolog, podemos especificar parâmetro, métrica ou artefato específico.

Dependendo do tipo de valor que vocé deseja registrar, use o método relevante do MLflow para armazenar o parâmetro, a métrica ou o artefato com a execução experimental:

* **mlflow.log_param()**: registrar parâmetro de chave-valor único. Use essa função para um parâmetro de entrada que voce deseja registrar.

* **mlflow.log_metric()**: registrar métrica de chave-valor unica. 0 a valor deve ser um numero. Use essa funcão para qualquer saída que vocé queira armazenar com a execução.

* **mlflow.log_artifact()**: registrar um arquivo. Use essa função para qualquer grafico que voce queira registrar, e salve como arquivo de imagem primeiro.

## Exibir as métricas no Estúdio do Azure Machine Learning 
---
* As métricas registradas serão exibidas nas guias Visão geral e Métricas. 
* Os gráficos registrados como artefatos são exibidos em Imagens. 
* Encontre outros artefatos, como arquivos de modelo, em Saídas + logs.

## Recuperar métricas com o Mlflow em um notebook
---
Use o MLflow em um notebook conectado ao workspace do Azure Machine Learning para ter mais controle sobre quais execuções você deseja recuperar para comparar.

Se estou no computador pessoal, conseguimos recuperar os logs.

Listar experimentos:

```py
experiments = 
mlflow.search_experiments(max_results=2)
    for exp in experiments:
        print(exp.name)
```

Recuperar execuções:

```py
mlflow.search_runs(exp.experiment_id)
```
> Slide: [Módulo 4 - Otimizar o Treinamento de Modelo no Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/b373d8c6-7875-4d98-8d43-a6690138687b.pptx)

