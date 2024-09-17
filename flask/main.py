from flask import *
import pickle

app = Flask(__name__)

model = pickle.load(open('./model/model.pkl', 'rb'))

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/predecir", methods=['POST'])
def predict():
    cuartos = int(request.form['cuartos'])
    distancia = int(request.form['distancia'])
    
    predict = model.predict([[cuartos, distancia]])    
    
    output = round(predict[0], 2)

    return render_template('index.html', predictText=f'La ksa con 4 cuartos tiene {predict}')

if __name__ == '__main__':
    app.run()