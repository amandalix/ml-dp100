# 📊 Regressão Linear com Azure Machine Learning – Projeto para Bootcamp DP-100 DIO >>>> Microsoft Certification Challenge #3 DP-100.

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

### 🔹 Resultados 1 – Command Job (Script Python)

| Métrica                        | Valor     |
|-------------------------------|-----------|
| Coefficient of Determination (R²) | 0.8159415 |
| Mean Absolute Error (MAE)     | 9.758208  |
| Mean Squared Error (MSE)      | 131.4361  |
| Root Mean Squared Error (RMSE)| 11.46456  |

![Gráfico de Resíduos](Resultados%201%20-%20residuos.JPG)

![Resultados em Metrics](Resultados%201.JPG)


#### 🧠 Interpretação:

- **R² = 0.82:** O modelo conseguiu capturar **82% da variância nas vendas**, mostrando ótimo poder explicativo.
- **MAE ≈ 9.76 e RMSE ≈ 11.46:** Os erros médios de previsão são baixos, com pouca dispersão.
- A abordagem visual se mostrou eficiente para experimentação rápida e bons resultados preditivos.


---

### 🔹 Resultados 2 – Designer Pipeline

![Pipeline](Resultados%202%20-%20Pipeline.JPG)

| Métrica                        | Valor     |
|-------------------------------|-----------|
| Coefficient of Determination (R²) | 0.7698971 |
| Mean Absolute Error (MAE)     | 9.765359  |
| Root Mean Squared Error (RMSE)| 12.30938  |
| Relative Squared Error (RSE)  | 0.2301029 |
| Relative Absolute Error (RAE) | 0.4864980 |

![Resultados 2](Resultados%202%20-%20r.JPG)

#### 🧠 Interpretação:

- **R² = 0.77:** Um pouco inferior ao Command Job, ainda assim explica **cerca de 77% da variação** nas vendas.
- **Erros similares ao pipeline** (MAE ≈ 9.76), mas **com RMSE ligeiramente maior**, sugerindo maior influência de outliers.
- **RAE e RSE < 0.5**, indicando que o modelo supera uma previsão ingênua (ex: média).
- O gráfico de resíduos sugere boa distribuição dos erros, sem padrões evidentes — um sinal positivo para regressão linear.



---

## 🧾 Conclusão

- O projeto demonstrou **com sucesso a aplicação do Azure Machine Learning** em diferentes fluxos de trabalho.
- Ambos os métodos produziram **modelos consistentes e com bom desempenho**, reforçando a utilidade das ferramentas da plataforma.
- A **interface do Designer** se destacou pela praticidade, enquanto o **Command Job** ofereceu mais controle e flexibilidade com código.

---

## 📁 Estrutura do Projeto no GitHub

Repositório disponível em: [https://github.com/amandalix/ml-dp100](https://github.com/amandalix/ml-dp100)

A estrutura está organizada da seguinte forma:

```bash
📂 ml-dp100/
├── 📁 Project 1/         # Dataset de vendas e clima
    ├── 📁 database/
    ├── 📁 src/
├── 📁 Resumos/           # Imagens dos resultados e gráficos (resíduos, métricas)
└── README.md              # Este arquivo
```

Durante o curso, fui anotando e consolidando informações que podem ser acessadas em: [Resumos](Resumos)

## ✅ Recomendações

- Explorar outros algoritmos e técnicas no Azure ML (ex: regressão regularizada, árvores, boosting).
- Realizar validação cruzada e tuning de hiperparâmetros com os recursos integrados da plataforma.
- Expandir o dataset com mais variáveis externas para refinar as previsões.

---


Este projeto faz parte do curso **Bootcamp DP-100 DIO >>>> Microsoft Certification Challenge #3 DP-100.**, que valida habilidades em:

- Gerenciamento de recursos no Azure ML
- Preparação de dados para modelagem
- Construção e implantação de modelos preditivos
- Monitoramento e manutenção de soluções de machine learning

