# Executando Pipelines no Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Criar e registrar um componente
---
Os componentes permitem que você crie scripts reutilizáveis que podem ser facilmente compartilhados entre usuários no mesmo workspace do Azure Machine Learning. Você também pode usar componentes para criar um pipeline do Azure Machine Learning. 

**Usar um componente:**

* Para criar um pipeline
* Para compartilhar o código pronto para uso.

Objetivo:
* Encapsular componentes que podem ser utilizados em pipelines e compartilhados com outras pessoas.
* Caixinhas compartilháveis que você pode utilizar em diversas etapas e também em diversos modelos de Machine Learning.
* Compartilhável com outras pessoas (código pronto pra uso)
* Reduz o tempo de desenvolvimento.

### Criar um componente

Um componente consiste em três partes: 

|Metadados|Interface|Comando, código e ambiente|
|---|---|---|
|Inclui o nome do componente, a versão entre outros|Inclui os parâmetros de entrada esperados (como um conjundo de dados ou hiperparâmetro) e a saída esperada (como métricas e artefatos)|Especifica como executar o código|
|metainformações|parâmetros entrada e saída|script e especificidades do código, bibliotecas, ambiente, código|

Para criar um componente, vocÊ precisa de dois arquivos:
* **Script**: contém o fluxo de trabalho que você deseja executar
* **Arquivo YAML**: define os metadados, a interface e o comando, o código e o ambiente do componente.


### Registrar um componente
* Para usar componentes em um pipeline, você precisará do script e do arquivo YAML.
* Para tornar os componentes acessíveis a outros usuários no workspace, você também poderá registrar componentes no workspace do Azure Machine Learning.

Registrar o componente com código:
> Python
```py
prep = ml_client.components.create_or_update(prepare_data_component)
```

## Executar um trabalho de pipeline
---

### Criar um pipeline

No Azure Machine Learning, um pipeline é um fluxo de trabalho de tarefas de machine learning em que cada tarefa é definida como um componente.

* Um pipeline do Azure Machine Learning é definido em um arquivo YAML. O arquivo YAML inclui o nome do trabalho de pipeline, entradas, saídas e configurações.

![Pipeline](https://ibb.co/twnMCg3d)

> **Slide**: [Módulo 4 - Otimizar o Treinamento de Modelo no Azure Machine Learning.pptx](https://web.dio.me/track/microsoft-certification-challenge-dp-100/course/bde0670f-6dcd-4b34-91ae-d3d6acf8f744/learning/f4ac0ff8-4ae8-40a1-9b97-44bb572965ad?autoplay=1&back=%2Ftrack%2Fmicrosoft-certification-challenge-dp-100#:~:text=Slide%3A%C2%A0M%C3%B3dulo%204%20%2D%20Otimizar%20o%20Treinamento%20de%20Modelo%20no%20Azure%20Machine%20Learning.pptx)
