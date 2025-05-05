# importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

# load dos dados de vendas
print("Loading Data...")
df = pd.read_csv('vendas_sorvetes_clima_itanhaem_2023.csv')

# transformando variavel categorica em binária
df['ocorrencia_chuva'] = df['ocorrencia_chuva'].map({'Sim': 1, 'Não': 0})

# separar features e labels
X, y = df[['temp_media','precipitacao','ocorrencia_chuva']].values, df['Qtd'].values

# split dos dados entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# configurar hyperparâmetro de regularização
reg = 0.01


# treinar modelo de regressão logística
print('Treinando modelo de regressão logística com regularização = ', reg)
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train, y_train)

# calcular acurácia
y_hat = model.predict(X_test)
acc = np.average(y_hat == y_test)
print('Accuracy:', acc)

# calcular AUC
y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test,y_scores[:,1])
print('AUC: ' + str(auc))
