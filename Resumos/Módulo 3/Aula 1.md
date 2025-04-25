# Execução de Scripts no Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Otimizar o treinamento de modelo no Azure Machine Learning
___
1. Executar um script de treinamento como um trabalho de comando no Azure Machine Learning
2. Monitoramento do Treinamento de Modelos com MLflow
3. Realização de Ajuste de Hiperparâmetros com o Azure ML
4. Execução de Pipelines no Azure Machine Learning

## Configurar um ambiente de comando
___

Converter um notebook em um script

* Os notebooks são ideais para exploração e desenvolvimento.
* Os scripts são ideais para testes e automação no ambiente de produção

Para subir em produção (converter em script): 

1. Remover códigos não essenciais
2. Refatora o código em funções
3. Testar o script (no terminal)

* Nome do Experimento
    * Nome de exibição do trabalho
        * Computação: precisa ter as capacidades e instância ativada
            * Ambiente: com todas as bibliotecas instaladas
                * Comando: chamada para executar o código
                    * Código em si.

## Usar parâmetros em um trabalho de comando
___

Para executar um script com entradas diferentes, use os **parâmetros**: 

Exemplo: 
1. Importe a biblioteca **argparse** no script
2. Use o método ArgumentParse() para definir argumentos para parâmetros
3. Especifique os parÂmetros no script, incluindo nome, tipo e valor padrão.
4. Ao executar o script, especifique o valor para os parâmetros definidos que você deseja que o script use para essa execução específica.


A ideia do script é facilitar que o código seja reutilizado em outros conjuntos de dados, outros treinamentos e experimentos.
A parametrização se faz necessária para ajustar o modelo ao seu objeto de estudo.

``` cmd
python train.py --training_data diabetes.csv --reg_rate 0.01"
```

