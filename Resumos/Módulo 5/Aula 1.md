# Implantação de Modelos ML em Pontos de Extremidade Online

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Explorar pontos de extremidade online gerenciados
---
* Real-time
Um **ponto de extremidade (endpoint)** é um ponto de extremidade HTTPS para o qual você pode enviar dados e que enviará uma resposta (quase) imediata.

Os pontos de extremidade online são usados para gerar previsões em tempo real para pontos de dados individuais.

* Cada requisição (botão, evento, informação enviada) uma resposta de retorno.
* API HTTPS para retornar resposta imediata

> Endpoints > Real-time endpoints > Details > REST endpoint > fazer chamada deste endpoint para retornar a requisição

> Endpoints > Real-time endpoints > Tests

> Consumo > JAVA, PYTHON, C#, JSON

## Implantar um modelo em um ponto de extremidade online gerenciado
---
Ao implantar um modelo em um ponto de extremidade gerenciado, você tem duas opções:

|Implantar um modelo em MLflow|Implante um modelo (personalizado|
|---|---|
|1.Registre um modelo MLflow com um arquivo MLModel.<br> 2. Crie a implantação<br>  3. Implante um modelo para o ponto de extremidade.|1. Registre um modelo com os arquivos de modelo necessários (sujeito ao tipo de modelo) <br> 2. Crie o script de pontuação. <br> 3. Defina um ambiente de execução. <br> 4. Cria a implantação <br> 5. Implante um modelo para o ponto de extremidade. 

## Testar pontos de extremidade online gerenciados
---

**Use o Estúdio do Azure Machine Learning para:**

* Liste todos os pontos de extremidade.
* Exibir os detalhes e os logs de implantação de um ponto de extremidade.
* Testar o ponto de extremidade
> Exemplo de Sample Test
```
{
    "input_data":{
        "columns": [
            "Pregnancies",
            "PlasmaGlucose",
            "DiastolicBloodPressure",
            "TricepsThickness",
            "SerumInsulin",
            "BMI",
            "DiabetesPedigree",
            "Age"
        ],
        "index": [0,1,2,3,4],
        "data": [
            [2,148,72,35,0,33.6,0.627,50],
            [1,85,66,29,0,26.6,0.351,31],
            [8,183,64,0,0,23.3,0.672,32],
            [1,89,66,23,94,29.1,0.167,43.1,2.288,33]
        ]
    },
    "params":{}
}
```

Dentro de consume já tem o código para consumo para a linguagem que precisar.