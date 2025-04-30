# Implantação de Modelos ML em Pontos de Extremidade em lote (Batch)

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Entender os pontos de extremidade em lote
---
1. Para obter previsões em lote, você poderá implantar um modelo em um ponto de extremidade.
2. Um **ponto de extremidade** é um ponto de extremidade HTTPS que você pode chamar para disparar um trabalho de pontuação em lote.
3. A vantagem desse ponto de extremidade é que você pode disparar o trabalho de pontuação em lote de outro serviço, como o Azure Synapse Analytics ou o Azure Databricks.
4. Sempre que o ponto de extremidade é invocado, um trabalho de pontuação em lote é enviado para o workspace do Azure Machine Learning.

Para implantar um modelo, primeiro você precisará criar o ponto de extremidade em lote. Para criar um ponto de extremidade em lote, você usará a classe `BatchEndpoint`. Os nomes de ponto de extremidade em lote devem ser exclusivos dentro de uma região do Azure.

> Python
```py
# create a batch endpoint
endpoint = BatchEndpoint(
    name = "endpoint-example",
    description = "A batch endpoint"
)

ml_client.batch_endpoints.begin_create_or_update(endpoint)
```

## Implantar um modelo em um ponto de extremidade em lote
---
Você pode implantar vários modelos em um ponto de extremidade em lote.

Sempre que você chamar o ponto de extremidade em lote, que dispara um trabalho de pontuação em lote, a **implantação padrão** será usada, a menos que especificado o contrário.

> Endpoints > Batch endpoints 


## Executar pontos de extremidade em lote
---

**Usar clusters de computação para implantações em lote**

Para processar os novos dados em lotes paralelos, será necessário provisionar um cluster de cálculo com mais de uma instância máxima.

Para criar um cluster de computação você poderá usar a classe AMLCompute.

>Python
```py
from azure.ai.ml.entities impor AmlCompute

cpu_cluster = AmlCompute(
    name="aml-cluster",
    type="amlcompute",
    size="STANDAR_DS11_V2",
    min_instances=0,
    max_instances=4,
    idle_time_before_scale_down=120,
    tier="Dedicated",
)

cpu_cluster = ml_client.begin_create_or_update(cpu_cluster)
```
instâncias dependem do quanto você precisa paralelizar o processamento


## Implantar seu modelo de MLflow em um ponto de extremidade em lote
---
* Para implantar um modelo do MLflow em um modelo do MLflow em um ponto de extremidade em lote, você usará a classe `BatchDeployment`.
* Quando você implanta um modelo, precisa especificar o comportamento do trabalho de pontuação em lote.
* Ao configurar a implantação do modelo você poderá especificar:
    * `instance_count`
    * `max_concurrency_per_instance`
    * `mini_batch_size`
    * `output_action`
    * `output_file_name`   


## Implantar um modelo personalizado em um ponto de extremidade em lote 
---
Se você quiser implantar um modelo em um ponto de extremidade em lote sem usar o formato de modelo do MLflow, precisará criar o script de pontuação e o ambiente.
1. **Criar o script de pontuação**: o script de pontuação é um arquivo que lê os novos dados, carrega o modelo e executa a pontuação.
2. **Criar um ambiente**: sua implantação requer um ambiente de execução no qual executar o script de pontuação. Qualquer dependência necessária pelo código deve ser incluída no ambiente.
3. **Configurar e criar a implantação**:finalmente, você pode configurar e criar a implantação com a classe `BatchDeploymeny`. 

## Invocar pontos de extremidade em lote
---

* Para preparar os dados para previsões em lote, você poderá registrar uma pasta como um ativo de dados no workspace do Azure Machine Learning.
* Você poderá usar o ativo de dados registrado como entrada ao invocar o ponto de extremidade em lote com o SDK do Python.

> Python
```py
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes

input = Input(
    type=AssetTypes.URI_FOLFER,
    path="azureml:new-data-1"
)

job = ml_client.batch_endpoints.invoke(
    endpoint-name=endpoint.name,
    input=input
)
```

## Resolver um problema de um trabalho de pontuação em lote
---
O trabalho de pontuação em lote é executado como um trabalho de pipeline. Se você quiser solucionar problemas do trabalho de pipeline, poderá examinar seus detalhes e as saídas e logs do próprio trabalho de pipeline.

* Trabalhos filhos: saídas dos logs (Outputs + logs).
    * job_error
    * job_progress
    * job_result
    * readme.txt -> tudo o que foi feito nesses logs.