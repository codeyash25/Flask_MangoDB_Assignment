from flask import Flask , jsonify
import json
app = Flask(__name__)

@app.route('/')
def Home():
    return 'Hello!  To access the data, add /api to the URL in your browser.'

@app.route('/api')
def Api():
    data = open('data.json', 'r')
    result =  json.load(data)
    data.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)