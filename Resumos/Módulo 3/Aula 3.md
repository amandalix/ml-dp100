# Realização de ajuste de Hiperparâmetros com o Az Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Entender o ajuste de hiperparâmetros.
---
O ajuste de hiperparâmetro é realizado por meio do treinamento de vários modelos, usando o mesmo algortimo e os mesmos dados de treinamento, mas valores de hiperparâmetros diferentes.

Dentro do processamento do algoritmo, o modelo vai iterar pelos hiperparâmetros (pesos) resultando em modelos distintos. Para algum deles o modelo vai ficar melhor.

No AutomatedML, automaticamente ele vai testando os melhores hiperparâmetros.

## Usar um trabalho de varredura para ajuste de hiperparâmeiro 
---

No Azure Machine Learning, você pode ajustar os hiperparâmetros executando um trabalho de varredura.

1. Criar um script de treinamento para ajuste de hiperparâmetro.
2. Configurar e executar um trabalho de varredura - sweep job
3. Monitorar e revusar trabalhos de varredura (filho)

> [Lab/09 - Perform hyperparameter tuning with a sweep job](https://microsoftlearning.github.io/mslearn-azure-ml/Instructions/09-Hyperparameter-tuning.html)


## Definir espaço de pesquisa
---
O conjunto de valores de hiperparâmetro testado durante o ajuste de hiperparâmetro é conhecido como o espaço de pesquisa. A definição do intervalo de possíveis valores que podem ser escolhidos depende do tipo de hiperparâmetro.

1. **Hiperparâmetros discretos**: alguns hiperparâmetros exigem valores discretos — em outras palavras, você deve selecionar o valor em um determinado conjunto finito de possibilidades.

- Números finitos de parâmetros, só itera sobre os números finitos individualmente.

2. **Hiperparâmetros contínuos**: alguns hiperparâmetros são contínuos — em outras palavras, você pode usar qualquer valor ao longo de uma escala, resultando em um número infinito de possibilidades

Definir um espaço de pesquisa: para definir um espaço de pesquisa para ajuste de hiperparâmetro, crie um dicionário com a expressão de parâmetro apropriada para cada hiperparâmetro nomeado

Faz a varredura em cima dos parâmetros indicados e mostra o ranking do melhor filho que teve a melhor performance.

## Configurar um método de amostragem
---
Os valores específicos usados em uma execução de ajuste de hiperparâmetro, ou trabalho de varredura, dependem do tipo de amostragem usada. Há três métodos de amostragem principais disponíveis no Azure Machine Learning:
1. **Amostragem de grade**: tenta todas as combinações possíveis. 
* Utilize todas as combinações e executa sobre tudo
* Evitar um range grande de parâmetros, deve-se usar uma política de bloqueio.
* Cria vários filhos, e mostra os resultados para todos.

2. **Amostragem aleatória**: escolhe valores aleatoriamente no espaço de pesquisa 
    * Sobol: adiciona uma semente à amostragem aleatória para tornar os resultados reproduzíveis

3. **Amostragem bayesiana**: escolhe novos valores com base nos resultados anteriores.
* Se for ruim, ele escolhe um parâmetro que melhore o modelo com base no que foi executado anteriormente.

> Se refere a amostragem dos hiperparâmetros e não a amostragem dos dados.

## Configurar término antecipado
---

Objetivo: não perder tempo de processamento. Criar uma regra para término antecipado, com base em número de avaliações, políticas de encerramento ou verifica o desempenho, se não estiver melhorando com base no modelo anterior ele para a varredura.

* Ao configurar um trabalho de varredura no Azure Machine Learning, você pode definir um número máximo de avaliações.

* Uma abordagem mais sofisticada pode ser parar um trabalho de varredura quando modelos mais recentes não produzem resultados significativamente melhores.

* Para interromper um trabalho de varredura com base no desempenho dos modelos, você pode usar uma política de encerramento antecipado.

### Quando usar uma política de encerramento antecipado

Se você deve ou não usar uma política de encerramento antecipado depende do espaço de pesquisa e do método de amostragem com o qual você está trabalhando.

Uma **política de encerramento antecipado** pode ser especialmente benéfica ao trabalhar com hiperparâmetros contínuos em seu espaço de pesquisa.

>Com o método de amostragem bayesiano, não pode ter uma política de encerramento antecipado.

## Política de encerramento antecipado
---
Há dois parâmetros principais quando você opta por usar uma política de encerramento antecipado:

|*evauation_interval*|*delay_evaluation*|
|---|---|
|especifica em qual intervalo você deseja que a política seja avaliada|especifica quando começar a avaliar a política|


Os novos modelos podem continuar a ter um desempenho um pouco melhor que os modelos anteriores. Para determinar a extensão segundo a qual um modelo deve ter um desempenho melhor que o apresentado em avaliações anteriores, há três opções de encerramento antecipado:
* **Política Bandit**
* **Política de Encerramento Mediana**
* **Política de seleção de truncamento**

### Política Bandit
---
Você pode usar uma política do Bandit para interromper uma avaliação se, até o momento, a métrica de desempenho de destino não superar a melhor avaliação por uma margem especificada.
> Python
```py
from azure.ai.ml.sweep import BanditPolicy


sweep_job.early_termination = 
    BanditPolicy(
        slack_amount = 0.2,
        delay_evaluation = 5,
        evaluation_interval = 1
    )
```

**🔍 Explicação de cada parâmetro**

* **slack_amount = 0.2**: Esse parâmetro define uma **margem de tolerância** em relação ao melhor desempenho atual.

    - Um experimento será interrompido se seu desempenho estiver **pior que 20% (0.2)** em relação ao melhor desempenho observado até o momento.
    - Isso ajuda a **eliminar candidatos fracos mais rapidamente**, economizando recursos.

* **delay_evaluation = 5**: Define o número de **execuções iniciais (ou *trial s*)** antes de começar a aplicar a política de interrupção.

    - Garante que todos os modelos tenham **tempo suficiente para apresentar resultados iniciais significativos**, antes de compará-los e decidir interromper algum.

* **evaluation_interval = 1**: Indica que a política será aplicada a **cada execução (trial)** a partir do momento em que `delay_evaluation` for atingido.
    - Ou seja, **após 5 execuções**, o desempenho de cada nova execução será avaliado e comparado com os melhores até então — a **cada 1 nova execução**.

Essa política é usada para tornar o processo de *hyperparameter tuning* mais eficiente, **economizando tempo e recursos computacionais** ao interromper execuções que provavelmente não levarão a bons resultados.

Itera o modelo até que os resultados não estejam mais dentro dos parâmetros.

### Política de Encerramento Mediana
---


Uma política de encerramento mediana abandona as avaliações em que a métrica de desempenho de destino é pior do que a mediana das médias em execução para todas as avaliações.
> Python
```py
from azure.ai.ml.sweep import MediaStoppingPolicy

sweep_job.early_termination = 
    MedianStoppingPolicy(
        delay_evaluation = 5,
        evaluation_interval = 1
    )
```

**🧠 Explicação dos parâmetros:** `MedianStoppingPolicy`

🔹 `sweep_job.early_termination = MedianStoppingPolicy(delay_evaluation = 5, evaluation_interval = 1)`

Essa linha define uma política de **interrupção antecipada** (early termination) baseada em mediana para experimentos de *hyperparameter tuning*.

🔹 `delay_evaluation = 5`
Define o número de **execuções (trials)** que devem ser completadas antes de começar a aplicar a política.

- Garante que cada experimento tenha **tempo suficiente para gerar dados significativos** antes de ser avaliado para possível interrupção.

🔹 `evaluation_interval = 1`
Indica com que frequência a política será aplicada após o atraso inicial.

- Com valor `1`, a avaliação ocorre **a cada nova execução (trial)**.


**📌 O que faz a `MedianStoppingPolicy`?**

Essa política interrompe execuções **cujo desempenho esteja abaixo da mediana** das execuções anteriores no mesmo ponto de avaliação.

- É baseada em uma **comparação estatística**, e não no melhor desempenho absoluto.
- Isso permite interromper experimentos **com baixo potencial de forma eficiente**, otimizando o uso de recursos computacionais.

Essa política é ideal para manter o foco nos modelos mais promissores e acelerar o processo de busca pelos melhores hiperparâmetros.



### Política de seleção de trucamento
---
Uma política de seleção de truncamento cancela X% das avaliações com pior desempenho em cada intervalo de avaliação com base no valor de `truncation_percentage` especificado para X.
> Python
```py
from azure.ai.ml.sweep import TruncationSelectionPolicy

sweep_job.early_terminatio = 
    TruncationSelectionPolicy(
        evaluation_interval = 1,
        truncation_percentage=20,
        delay_evaluation=4
    )
```
**🚀 Explicação dos parâmetros: `TruncationSelectionPolicy`**

Essa linha configura uma política de **interrupção antecipada** usando o método de **truncação de seleções** para experimentos de *hyperparameter tuning*.


🔹 `evaluation_interval = 1`
Define com que frequência os experimentos serão avaliados.

- Com valor `1`, a avaliação acontece **a cada nova execução (trial)** após o tempo de espera inicial.


🔹 `truncation_percentage = 20`
Determina a porcentagem de execuções a serem interrompidas.

- Nesse caso, os **20% dos experimentos com pior desempenho** serão parados durante cada avaliação.


🔹 `delay_evaluation = 4`
Especifica o número de execuções (trials) que precisam ser completadas **antes de começar a aplicar a política**.

- Garante que haja **dados suficientes para uma avaliação justa** antes de eliminar os piores resultados.


**📌 Como funciona a `TruncationSelectionPolicy`?**

Após esperar `4` execuções, o sistema começa a avaliar o desempenho **a cada nova execução**.

- Durante cada avaliação, **os 20% dos experimentos com pior desempenho** são **interrompidos**.
- Assim, o processo foca rapidamente nos experimentos mais promissores, economizando **tempo e recursos computacionais**.


Essa política é muito útil para acelerar o *hyperparameter tuning*, eliminando candidatos fracos em várias rodadas ao longo do processo!

>Slide: [Módulo 4 - Otimizar o Treinamento de Modelo no Azure Machine Learning.pptx](https://web.dio.me/track/microsoft-certification-challenge-dp-100/course/realizacao-de-ajuste-de-hiperparametros-com-o-azure-machine-learning/learning/12cc8096-6b34-44a4-b29f-aeef9bac001d?autoplay=1&back=%2Ftrack%2Fmicrosoft-certification-challenge-dp-100#:~:text=Slide%3A%C2%A0M%C3%B3dulo%204%20%2D%20Otimizar%20o%20Treinamento%20de%20Modelo%20no%20Azure%20Machine%20Learning.pptx)