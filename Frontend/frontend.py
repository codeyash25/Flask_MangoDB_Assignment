
from flask import Flask , request, render_template, redirect
import requests


app = Flask(__name__)

BACKEND_URL = 'http://localhost:9000'

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/submit' , methods=['POST'])
def submit():
    Fdata = dict(request.form)
    response = requests.post(BACKEND_URL + "/submit", json=Fdata)
    data = response.json()

    if data ['status'] == 'success':
      return redirect('/success')
    else: 
      return render_template('index.html', error=data['message'])

@app.route('/success')
def success():
  return "Data submitted successfully"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)