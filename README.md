# 📊 Regressão Linear com Azure Machine Learning – Projeto para Certificação DP-100

Este projeto foi desenvolvido como parte do **Bootcamp da DIO (Digital Innovation One)** voltado para a **certificação DP-100 da Microsoft**. O foco principal é demonstrar na prática o uso da plataforma **Azure Machine Learning** na criação, execução e análise de um experimento de **regressão linear**.

---

## 🎯 Objetivo do Projeto

O objetivo central é explorar os recursos do **Azure Machine Learning** para treinar e avaliar um modelo de regressão linear em dois formatos distintos:

- Via **Command Job**, utilizando scripts Python.
- Via **Designer Pipeline**, utilizando a interface visual da plataforma.

Para isso, foi utilizado um dataset fictício com dados sobre **vendas de sorvetes** e **condições climáticas**.

### 🔍 Variáveis utilizadas:

- 🌧️ Ocorrência de chuva (Sim/Não)  
- 🌡️ Temperatura média (°C)  
- 🌧️ Precipitação (mm)  
- 🍦 Vendas de sorvete (variável alvo)

---

## ⚙️ Abordagens no Azure ML

- **Command Job:** Treinamento e avaliação de um modelo de regressão linear via código em um ambiente computacional gerenciado pelo Azure.
- **Designer Pipeline:** Criação de pipeline visual com módulos pré-configurados de pré-processamento e regressão linear, sem necessidade de escrever código.

---

## 📈 Resultados e Interpretação

### 🔹 Command Job

| Métrica                        | Valor     |
|-------------------------------|-----------|
| Root Mean Squared Error (RMSE)| 12.30938  |
| Mean Absolute Error (MAE)     | 9.765359  |
| R² (Coef. Determinação)       | 0.7698971 |
| Relative Squared Error (RSE)  | 0.2301029 |
| Relative Absolute Error (RAE) | 0.4864980 |

#### 🧠 Interpretação:

- **R² = 0.77:** O modelo explica cerca de **77% da variação** nas vendas de sorvetes.
- **RMSE e MAE** indicam erros médios em torno de 9 a 12 unidades, com leve presença de outliers.
- **RAE e RSE** abaixo de 0.5 mostram que o modelo tem desempenho significativamente melhor que previsões aleatórias.
- O **gráfico de resíduos** mostra distribuição aleatória, sem padrão evidente, o que é positivo para regressão linear.

![Gráfico de Resíduos](./Resultados%201%20-%20residuos.JPG)

---

### 🔹 Designer Pipeline

| Métrica                        | Valor     |
|-------------------------------|-----------|
| Root Mean Squared Error (RMSE)| 11.46456  |
| Mean Absolute Error (MAE)     | 9.758208  |
| Mean Squared Error (MSE)      | 131.4361  |
| R² (Coef. Determinação)       | 0.8159415 |

#### 🧠 Interpretação:

- **R² = 0.82:** Leve melhora em relação ao Command Job, com maior poder explicativo.
- **Erros (RMSE/MAE)** ligeiramente menores indicam melhor performance.
- A abordagem visual se mostrou eficiente para fins de experimentação e prototipagem rápida.

---

## 🧾 Conclusão

- O projeto demonstrou **com sucesso a aplicação do Azure Machine Learning** em diferentes fluxos de trabalho.
- Ambos os métodos produziram **modelos consistentes e com bom desempenho**, reforçando a utilidade das ferramentas da plataforma.
- A **interface do Designer** se destacou pela praticidade, enquanto o **Command Job** ofereceu mais controle e flexibilidade com código.

---

## ✅ Recomendações

- Explorar outros algoritmos e técnicas no Azure ML (ex: regressão regularizada, árvores, boosting).
- Realizar validação cruzada e tuning de hiperparâmetros com os recursos integrados da plataforma.
- Expandir o dataset com mais variáveis externas para refinar as previsões.

---

## 📚 Sobre a Certificação

Este projeto faz parte do preparo para a **certificação DP-100: Designing and Implementing a Data Science Solution on Azure**, que valida habilidades em:

- Gerenciamento de recursos no Azure ML
- Preparação de dados para modelagem
- Construção e implantação de modelos preditivos
- Monitoramento e manutenção de soluções de machine learning

