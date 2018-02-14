from time import strftime
from database import *
from flask import Flask, request,session

import json

db.create_all()
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        result = User.query.filter_by(karbar = request.form['karbar']).first()
        if result == None :
                return "sorry enter again!"
        if request.form['Pass'] != result.Pass :
                return "sorry retry"
        session['karbar'] = request.form['karbar']
        return "T"


@app.route("/logout", methods=['POST'])
def logout():
    if request.method == 'POST':
        session.pop('karbar', None)
        return "GOODBYE"

@app.route("/play", methods=['POST'])
def play():
    pass

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        if not request.form['user']:
            return "Please check your data!"
        result = User.query.filter_by(karbar = request.form['karbar']).first()
        if result != None :
            return "lotfan etelaat khod ra check konid"

        user = User(karbar=request.form['karbar'], Pass=request.form['Pass'], score = '0')
        db.session.add(user)
        db.session.commit()
        return "DONE!!"

@app.route("/score", methods=['POST'])
def score():
    if request.method == 'POST':
        result = User.query.filter_by(user=request.form['user']).first()
        if result == None:
            return "this karbar does not exist!"
        return result.score

@app.route("/my_data", methods=['POST'])
def my_data():
    if request.method == 'POST':
        NAME = request.form['id']
        result = Table.query.filter_by(id = NAME).first()
        game_data = {'id': result.id, 'bazikonha': result.bazikonha, 'safhe': result.safhe, 'nobat': result.nobat, 'makan': result.makan, 'DIVAR': result.DIVAR, 'tedad': result.tedad, 'checker': result.checker}
        return json.JSONEncoder().encode(game_data)

app.secret_key = 'qwertyuiopasdfghjkl;zxcvbnm,!@#$%^&*()_1234567890'
