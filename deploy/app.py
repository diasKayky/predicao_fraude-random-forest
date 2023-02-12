from flask import request, Flask
import numpy as np
import pandas as pd
import pickle

modelo = pickle.load(open('../modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict():

    if request.method == 'POST':
        data = request.get_json()

        CUSTOMER_ID = data["custumer_id"]
        TERMINAL_ID = data["terminal_id"]
        TX_AMOUNT = data["tx_amount"]
        TX_TIME_SECONDS = data["tx_time_sec"]

        data_ = {'CUSTOMER_ID': CUSTOMER_ID, 'TERMINAL_ID': TERMINAL_ID, 'TX_AMOUNT': TX_AMOUNT, 'TX_TIME_SECONDS': TX_TIME_SECONDS}
        X = pd.DataFrame(data_, index=[0])
        Y = modelo.predict(X)
        Y = np.array(Y).tolist()

        if Y[0] == 0:
            Y[0] = 'Transação legitima'
        else:
            Y[0] = 'Transação fraudulenta'

        return {'Predição': Y[0]}

if __name__ == '__main__':
    app.run(debug=True)