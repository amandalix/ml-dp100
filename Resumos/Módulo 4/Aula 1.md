# Registro de Modelos do MLflow no Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Registrar um modelo com o MLflow
---
O MLflow permite registrar um modelo como um **artefato** ou como um **modelo**.

* Quando você registra um modelo como um artefato, ele é tratado como um arquivo.
* Ao registrar como modelo você está adicionando informações ao modelo registrado que permite usar o modelo diretamente em pipelines ou implantações.

> Modelo > Saídas + Logs
* conda.yaml
* MLmodel
* model.pkl
* python_env.yaml
* requirements.txt

Quando registra como um modelo ele adiciona um arquivo MLmodel no diretório de saída. O arquivo MLmodel contém metadados do modelo, o que permite a rastreabilidade do modelo.

* Garante alguns parâmetros para rastreabilidade:
    * Qual o input?
    * Qual o output?
    * Quais os tipos de colunas?
    * Qual o nome da coluna?

* Garantir que os parâmetros sejam controlados.


## Entenda o formato de arquivo MLmodel
---

O arquivo MLmodel pode incluir:

* `artifact_path`: durante o trabalho de treinamento o modelo é registrado nesse caminho.
* `flavor`: a biblioteca de machine learning com a qual o modelo foi criado
* `model_uuid`: o identificador exclusivo do modelo registrado
* `run_id`: o identificador exclusivo da execução de trabalho durante a qual o modelo foi criado


Exemplo:
> MLmodel
```MLmodel
artifact_path: model
flavors:
    python_functions:
        env: conda.yaml
        loader_module: mlflow.sklearn
        model_path: model.pkl
        predict_fn: predict
        python_version: 3.7.16
    sklearn:
        code: null
        pickled_model: model.pkl
        serialization_format: cloudpickle
        sklearn_version: 0.24.1
mlflow_version: 1.30.1
model_uuid: 10asJ3653.........
run_id: nome_do_job_5874254
signature:
    inputs: '[{"type": "tensor", "tensor-spec": {"dtype": "float64", "shape": [-1, 8]}}]'
    outputs: '[{"type": "tensor", "tensor-spec": {"dtype": "float64", "shape": [-1]}}]'
utc_time_created: '2025-02-22 18:24:20.942007'
```

O arquivo MLmodel pode incluir:


* **siganture**: especifica o esquema das entradas e saídas do modelo.
* **inputs**: entrada válida para o modelo. Por exemplo, um subconjunto de dados de treinamento.
* **outputs**: saída válida do modelo. Por exemplo, previsões de modelo para o conjunto de dados de entrada.



