from flask import Flask , request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv('database_url')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.test

collection = db['flask_Assignment']

@app.route('/submit' , methods=['POST'])
def submit():
    
    fdata = dict(request.json)

    if fdata.get('name') == "":
        return {"status": "error", "message": "Name is required"}
    if fdata.get('occupation') == "":
        return {"status": "error", "message": "Occupation is required"}
    
    collection.insert_one(fdata)
    return {"status": "success", "message": "Data submitted successfully"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)