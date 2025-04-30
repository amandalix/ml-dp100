# Criação e Análise de Painéis de IA Responsável no Azure Machine Learning

> Bootcamp DP-100 DIO  >>>> [Microsoft Certification Challenge #3 DP-100](https://web.dio.me/track/d5adf7bc-330f-4c81-adc1-cac7e65bb151).

## Entenda a IA responsável
---
A Inteligência Artificial Responsável (IA responsável) é uma abordagem para desenvolver, avaliar e implantar sistemas de IA de maneira segura, confiável e ética.

* **Imparcialidade**: imparcialidade entre gêneros, raças, classes sociais.
* **Confiabilidade e segurança**: avaliar danos às pessoas pelo modelo, em segurança pessoal.
* **Privacidade e segurança**: dados confidenciais, restrição de acesso, etc.
* **Inclusão**: acessibilidade de grupos com diversidade.
* **Transparência**: limites, cenários e confiança na informação do modelo.
* **Responsabilidade**: quem terá responsabilidade sobre a IA.

## Confiabilidade e segurança: entenda seus conjuntos de dados 
---
Use a análise de dados para ajudar você a identificar problemas de excesso e falta de representação e ver como os dados são clusterizados no conjunto de dados.

Use a análise de dados quando precisar:
* Explorar as estatísticas do conjunto de dados selecionando filtros diferentes para dividir seus dados em dimensões diferentes (também conhecidas como cohortes)
* Entender a distribuição do conjunto de dados em diferentes cohortes e grupos de recursos.

Comparação entre coortes em suas taxas de representatividade de erros, grupo de recursos, etc.

**Error Rate**: analisar as cohorts para cada trecho da árvore de decisão, se o erro aumenta ou permanece próximo.

**Heatmap**: pode analisar o error rate de todo o dataset e compara as colunas em um mapa de calor. Com base no conhecimento dos dados, as análises serão diferenciadas.

**Global cohort**: todo o dataset, temporal, acurácia, falso positivo, precisão correta ou incorreta, features determinantes para o modelo ser explicado.

## Confiabilidade e segurança: avaliar erros em seu modelo
---
Identificar cohortes errôneas de dados. Explorar se o seu modelo tem um desempenho inferior para grupos demográficos específicos.
* **Árvore de erros (treemap)**: particiona os dados em subgrpos interpretáveis.
* **Mapa de calor de erros (heatmap)**: fatia os dados com base em uma grade unidimensional ou bidimensional de recursos de entrada.

## Transparência: interprete seu modelo
---
**Importância do recurso agregada**
* Importância do recurso geral para todos os dados do teste.
* Indica a influência relativa de cada recurso no rótulo previsto

**Importância do recurso individual**
* Importância do recurso para uma previsão individual
* Na classificação isso mostra o suporte relativo para cada classe possível por recurso

Verificar se a coluna de entrada possui importância no resultado final.

## Imparcialidade: mitigar a disparidade
---
A visão geral do modelo e a avaliação de imparcialidade avaliam o desempenho do seu modelo e avaliam os problemas de imparcialidade do grupo do seu modelo.

* **Imparcialidade no desempenho do modelo**: diferentes cohorts dos dados têm um desempenho diferente ao comparar métricas de desempenho selecionadas?

* **Imparcialidade na taxa de seleção**: existem cohorts dos dados que mais frequentemente obtêm uma previsão favorável?

## Criar um painel de IA Responsável
---
Para criar um painel de IA responsável (RAI) você precisa criar um **pipeline** utilizando os componentes internos. O pipeline **deve**:

1. Comece com o Construtor de painel do RAI Insights.
2. Inclua um dos **componentes da ferramenta RAI**.
3. Termine com o painel Coletar RAI Insights para coletar todos os insights em um único painel.
4. *Opcionalmente* você também pode adicionar o cartão de pontuação Coletar RAI Insights no final do seu pipeline.
