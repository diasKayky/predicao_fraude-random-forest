# Importações de libraries importantes
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Carregamento e preprocessamento de dados
df = pd.read_csv("../../data/raw/dataset1.csv", index_col=[0])
feature_selecao = lambda df, features: df[features]
df = feature_selecao(df, ["CUSTOMER_ID", "TERMINAL_ID", "TX_AMOUNT", "TX_TIME_SECONDS", "TX_FRAUD"])

# Definição e split de X e Y
X = df[["CUSTOMER_ID", "TERMINAL_ID", "TX_AMOUNT", "TX_TIME_SECONDS"]]
Y = df["TX_FRAUD"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# Treinamento do modelo
modelo = RandomForestClassifier(n_estimators=400)
modelo.fit(X_train, Y_train)

# Serializa o modelo usando o pickle
pickle.dump(modelo, open('modelo.pkl', 'wb'))
modelo = pickle.load(open('modelo.pkl', 'rb'))

# Prediz o dataset test
y_pred = modelo.predict(X_test)

target_names = ['transação legítima', 'transação fraudulenta']
print(classification_report(Y_test, y_pred, target_names=target_names))
