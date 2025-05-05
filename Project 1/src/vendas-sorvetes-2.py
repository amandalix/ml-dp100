import mlflow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dados
df = pd.read_csv('vendas_sorvetes_clima_itanhaem_2023.csv')
df['ocorrencia_chuva'] = df['ocorrencia_chuva'].map({'Sim': 1, 'Não': 0})
X, y = df[['temp_media', 'precipitacao', 'ocorrencia_chuva']].values, df['Qtd'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Modelo
model = LinearRegression().fit(X_train, y_train)
y_hat = model.predict(X_test)

# Métricas
mae = mean_absolute_error(y_test, y_hat)
mse = mean_squared_error(y_test, y_hat)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_hat)

mlflow.log_metric("MAE", mae)
mlflow.log_metric("MSE", mse)
mlflow.log_metric("RMSE", rmse)
mlflow.log_metric("R2", r2)

# Gráfico
residuos = y_test - y_hat
plt.scatter(y_hat, residuos)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predições')
plt.ylabel('Resíduos')
plt.title('Gráfico de Resíduos')

os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/residuos.png")
mlflow.log_artifact("outputs/residuos.png", artifact_path="figuras")

