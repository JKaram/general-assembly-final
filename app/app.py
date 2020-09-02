from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')

with open('model/pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

@app.route('/',  methods=['POST'])
def predict():
    form = request.form
    new = pd.DataFrame({
        'date': [form.get("date")]
    })
    new["date"] = pd.to_datetime(new["date"])
    prediction = pipe.predict(new)[0]
    return render_template('perdict.html', prediction=prediction)