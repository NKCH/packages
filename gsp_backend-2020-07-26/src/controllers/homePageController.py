from flask import render_template

from src import app
from resources.data.pyDB import db
from bson import json_util


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/content', methods=['GET'])
def content():
    data = []
    coll = db.BannerContent
    bannerContent = []
    for x in coll.find():
        bannerContent.append(x)
    obj = {"bannerContent": bannerContent}

    productContent = []
    coll2 = db.Products
    for y in coll2.find():
        productContent.append(y)
    objProd = {"productDetails": productContent}
    data.append(obj)
    data.append(objProd)
    j_data = json_util.dumps(data)
    return j_data


@app.route('/about-us', methods=['GET'])
def aboutUs():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/contact-us', methods=['GET'])
def contactUs():
    return render_template('index.html')
