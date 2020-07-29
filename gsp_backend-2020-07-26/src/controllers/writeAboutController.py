from src import app
from resources.data.pyDB import db
from flask import request
from src.services.SendEmailNotication import emailNotication


@app.route("/write", methods=['POST'])
def write():
    value = request.form
    new_dict = dict([(key, value) for key, value in value.items()])
    coll = db.Writeus
    coll.insert_one(new_dict)
    emailNotication(new_dict)
    return "ok"
