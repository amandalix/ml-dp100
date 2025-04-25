# Monitoramento do Treinamento de Modelos em Notebooks Jupyter com MLflow

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Buscando o Melhor Modelo de Classificação com ML
___

### Pré-processar dados e configurar a definição de recursos 

- Antes de executar o AutoML, você precisa preparar os dados.
    - A classificação requer dados tabulares
    - Criar um **ativo de dados** no Azure Machine Learning
    - Criar um ativo de dados **MLTable**: aarmazene seus dados em uma pasta junto com um arquivo MLTable

>Python
```python
from azure.ai.ml.constants improt AssetTypes
from azure.ai.ml import Input
my_training_data_input = Input(type=AssetTypes.MLTABLE, path="azureml:input-data-automl")
```

### Entender o dimensionamento e a normalização
___
- Entender o intervalo existente para os valores
    - Valores negativos
    - Moeda
    - Idade
- Normalizar esses valores para que todas as variáveis estejam em um mesmo padrão.

- O AutoML aplica o dimensionamento e a normalização dos dados numéricos automaticamente, ajudando a impedir que qualquer recurso de grande escala domine o treinamento.
- Durante um experimento de AutoML, várias técnicas serão aplicadas

- Configurar a definição de recursos opcional:
    - Imputação de valor ausente para eliminar os nulos do conjunto de dados de treinamento.
    - Codificação categórica para converter recursos categóricos em indicadores numéricos (String, converte para numérico)
    - Remoção de recursos de alta cardinalidade, como IDs de registro.
    - Engenharia de recursos (por exemplo, derivação de partes de data individuais dos recursos de DateTime) -> Semana, Ano, Mês etc.

## Executar um experimento de ML automatizado
___
Quando você quiser treinar um modelo de classificação, o AutoML escolherá entre uma lista de algortimos de classificação:
- Regressão Logística
- GBM (computador de gradient boosting)
- Árvore de Decisão
- Floresta aleatória
- Naive Bayes
- SVM (computador de vetor de suporte) linear
- XGBoost
- etc ...

Restringir faz com que o modelo execute mais rápido.

### Restringir a seleção de algortimo
- Por padrão, o AutoML fará uma seleção aleatória entre o intervalo completo de algortimos para a task especificada.
- Você pode optar por bloquear a seleção de algortimos individuais, o que poderá ser útil se souber que os dados não são adequados a um tipo específico de algortimo.
- Talvez você também queria bloquear determinados algortimos se precisar cumprir uma política que restrija o tipo de algortimos de aprendizado de máquina que pode usar em sua organização.

## Configurar um experimento de AutoML
____
 Ao usar o SDK do Python(V2) para configurar um experimento ou trabalho de AutoML, configure o experimento usando o automl class.

 1. **Especifique a métrica primária:** o "melhor" modelo é baseado no **primary_metric**.
 2. **Defina os limites:** Para minimizar os custos e tempo gasto com treinamento, você pode definir limites para um experimento ou trabalho de AutoML usando *set_limits()*.
 3. **Defina as propriedades do treinamento:** o AutoML experimentará várias combinações de definição de recursos e algoritmos para treinar um modelo de machine learning.

```python
from azure.ai.ml import automl                      # classe da biblioteca azure.ai.ml

classification_job = automl.classification(         # nome do job, usando o modelo de clasificação
    compute="aml-cluster",                          # nome da computação instanciada na azure
    experiment_name="auto-ml-class-dev",            # nome do experimento
    training_data=my_training_data_input,           # dados de treinamento
    target_column_name="Diabetic",                  # objetivo da coluna
    primary_metric="accuracy",                      # acurácia para melhor modelo
    n_cross_validation=5,                           # numero de validações cross
    enable_model_explainability=True                # habilitado para explicar o modelo
)
```

## Definir os limites
___

Há várias opções para definir limites para um experimento de AutoML:
- **timeout_minutes** : número de minutos após o qual o experimento completo é encerrado.
- **trial_timeout_minutes** : número máximo de minutos que uma avaliação pode levar.
- **max_trials** : número máximo de avaliações ou de modelos que serão treinados.
- **enable_early_termination** : se deseja encerrar o experimento se a pontuação não estiver melhorando no curto prazo.

```python
classification_jobe.set_limits(         # classe para setar limites
    timeout_minutes=60,                  
    trial_timeout_minutes=20,            
    max_trials=5,                        
    enable_early_termination=True        
)
```


## Enviar um experimento de AutoML
___

Você pode enviar um experimento de AutoML com o seguinte código:
- O experimento consistirá em trabalhos filhos:
    - A definição de recursos é realizada em um trabalho filho
    - Cada modelo é treinado em um trabalho filho separado.

```python
returned_job = ml_cliet.jobs.create_or_update(classification_job)
```

### Avaliar e comparar modelos

No Estúdio do Azure Machine Learning, você pode selecionar um experimentode AutoML para explorar os detalhes.

> **machinedio > Jobs > my-1st-automl-experiment > bubbly_stomach_8h0k6txrvs > Models + child jobs**

Na página Visão geral da execução do experimento de AutoML, você pode examinar o ativo de dados de entrada e o resumo do melhor modelo. Para explorar todos os modelos que foram treinados selecione a guia "Models + child jobs"

## Recuperar a melhor execução e o modelo
___

- A seleção permite que ele explique o modelo
- Ao examinar os modelos no AutoML, você pode identificar facilmente a melhor execução com base na métrica primária especificada.
- Na guia Modelos de experimento de AutoML, você poderá editar as colunas se quiser mostrar outras métricas na mesma visão geral.
- Para exportar ainda mais um modelo, você pode gerar explicações individuais dos resultados.




