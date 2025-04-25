# Configuração e Uso de Ambientes no Azure Machine Learning
> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Noções básicas sobre os ambientes
---

- Os ambientes definem o contexto necessário para executar código em um destino de computação.
    - Define parâmetros de environment: a versão do python, versão da biblioteca, SO, para executar o modelo sem bug, defazagem, etc.
    - Instala no ambiente para executar o modelo
- Um ambiente é usado para criar o contâiner do Docker no qual seu código é executado no destino de computação especificado.
    - Especifica e instala no Docker.
- Use um ambiente com curadoria predefinida ou crie seu prórpio ambiente personalizado
    - Definir ou pegar algum pré-existente.

> **Assets > Environments > nomedoambiente > Parâmetros

1. Overview
    - Nome
    - Atribuição
    - Versão do contâiner
    - OS
    - REGISTRY
    - Asset ID
    - ...
 2. Contexto
    - data_import_run.py
        - path
        - class
        - dataclass
    - finetune_run.py
        - parâmetros de processamento
    - requirements
        - bibliotecas e as versões 
3. Jobs


> Curated Environments

> Custom environments

## Criar ambientes personalizados (Custom environments)
---

- Imagem de Docker: escolha uma imagem existente de um repositório (público).
- Contexto de compilação do Docker: faça referência a um caminho que inclui um Dockerfile e requirements.txt
### Dockerfile
``` python
#FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
FROM python:3.8

#python installs
COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

# set command
CMD ["bash"]
```

- Expecificação Conda: faça referência a uma imagem e adicione um arquivo YAML conda que inclua dependências adicionais.
### Arquivo YAML do Conda
```YAML
name: pydata-example

channels:

    - conda-forge

dependencies:

    - python:3.8

    - pip=21.2.4

    - pip:

        - numpy==1.22

        - scipy==1.7.1

        - pandas==1.3.0

        - scikit-learn==0.24.2
```

> Slide: [Configuração e Uso de Ambientes no Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/e60a1a6c-0ae3-42a2-acd9-70b09a1b9c2b.pptx)