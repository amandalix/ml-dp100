# Gerenciamento de Destinos de Computação no Azure Machine Learning
> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Trabalhar com recursos de computação no Azure Machine Learning
___
### Destino de Computação apropriado
---

Tipos:

1. Experimentação em Notebook 
    - Instância de computação
    - Spark sem servidor
    - Computação anexada

    >**Manage > Compute > Compute instances > + New > CPU | GPU (teste em fotos) > Select from recommend options**
    >> **Scheduling**

    >> **Security**

    >> **Applications**
    
    >> **Tags**: quem é o responsável
    

    > **Authoring > Notebook > Trocar o *Compute* para a instância criada**

2. Executar um trabalho para treinar modelo
    - Cluster de cálculo
    - Computação sem servidor
    - Clusters do Kubernetes
    - Computação anexada

3. Executar trabalhos de pipeline (lotes)
    - Cluster de cálculo
    - Computação sem servidor
    - Clusters do Kubernetes
    - Computação anexada

4. Implantar modelo em tempo real
    - Contêineres
    - Clusters do Kubernetes


### Configurar a instância de computação
---
#### Instância
Cada instância só vai ser atribuída ao usuário específico. Toda vez que processa algum job, gera custo. Pode atribuir a outra pessoa mas não pode compartilhar ao mesmo tempo.

- Instância de computação: só pode ser atribuída a um usuários.
- Ao criar uma instância de computação, se você tiver as permissões apropriadas, será possível atribuir a outra pessoa.

#### Minimizar o tempo de computação (Reduzir custos)
- Iniciar e interromper manualmente.
- Programar a instância de computação
- Configure quando desligar sua instância de computação devido a inatividade.

Gerenciar tempo, custo e uso da instância.
Dica: utilizar a computação local para testes e depois subir para a nuvem.

> Slide: [Gerenciamento de Destinos de Computação no Azure Machine Learning.pptx](https://hermes.dio.me/files/assets/4a3aa7a5-97a3-4d7f-b292-0a6e5d4edee9.pptx)