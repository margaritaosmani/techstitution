from flask import Blueprint, render_template, request, redirect, url_for
from app import mongo
from bson import json_util, ObjectId

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET','POST'])
def index():
    db = mongo.db.arkep
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        db.insert(data)
        return redirect(url_for('.listo'))

@mod_main.route('/<string:id>', methods=['GET'])
def get_doc(id):
    db = mongo.db.arkep
    if request.method == 'GET':
        doc = db.find_one({"_id":ObjectId(id)})
        doc_json = json_util.dumps(doc)
        return render_template('doc.html', doc=doc)
    else:
        return "bad request"

@mod_main.route('/listo',methods=['GET'])
def listo():
    db = mongo.db.arkep
    myCursor = db.find();
    if request.method == 'GET':
        return render_template('list.html', myCursor=myCursor)

@mod_main.route('/delete_document<id>')
def delete_document(id):
    db = mongo.db.arkep
    db.remove({"_id":ObjectId(id)})
    return redirect(url_for('.listo'))

@mod_main.route('/arkep', methods=['GET','POST'])
def arkep():
    form = arkep()
    # TODO: render arkep.html
    # TODO: form.validate_on_submit()
