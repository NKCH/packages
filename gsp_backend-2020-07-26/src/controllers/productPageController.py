from src import app
from resources.data.pyDB import db
from bson import json_util
from flask import render_template

@app.route('/products', methods=['GET'])
def products():
    return render_template('index.html')

@app.route('/products/<code>', methods=['GET', 'POST'])
def product(code):
    coll = db.Product
    data = []
    for x in coll.find({"Category": code}):
        data.append(x)
    j_data = json_util.dumps(data)
    return j_data
