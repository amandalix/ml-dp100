# Otimizando Modelos de Azure AI Foundry com fine-tuning

## Entenda quando ajustar finamente um modelo
---
O ajuste fino melhorará o modelo quando:
* Você tem um caso de uso específico e claro.
* Você precisa que a saída do modelo esteja em um estilo personalizado específico.
* Você deseja ter um desempenho mais consistente fornecendo mais exemplos de few shots do que podemo caber no seu prompt.

## Prepare seus dados para o ajuste fino em um modelo de conclusão de chat
---

Os dados devem ser formatados como um documento JSON Lines (JSONL). Para ajuste fino em uma tarefa de conclusão de chat, seus dados devem incluir:

Aplica viés contextual para um modelo fine-tuning.

## Ajustar finamente um modelo
---

1. Selecione o modelo base
2. Selecione seus dados de treinamento
3. Opcional: Selecione seus dados de validação
4. Configure opções avançadas:

|Nome|Descrição|
|---|---|
|`batch_size`|Número de exemplos de treinamento usados para treinar uma única passagem para frente e para trás |
|`learning_rate_multiplier`|Taxa de aprendizado original usado para o pré-treinamento multiplicado por este valor|
|`n_epochs`|O número de epochs para treinar o modelo. Uma epoch refere-se a um ciclo completo atravpes do conjunto de dados de treinamento|
|`seed`|A seed controla a produtividade do trabalho|
