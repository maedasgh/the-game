from time import strftime
from database import *
from flask import Flask, request,session
import def_qurid
import json

db.create_all()
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        natige = User.query.filter_by(karbar = request.form['karbar']).first()
        if natige == None :
                return "sorry enter again!"
@app.route("/logout", methods=['POST'])
def logout():
    if request.method == 'POST':
        session.pop('karbar', None)
        return "GOODBYE"

@app.route("/play", methods=['POST'])
def play():
    if request.method == 'POST':
        NAME = request.form['id']
        player = session['karbar']
        natige = Table.query.filter_by(id=NAME).first()
        bazikonha = json.loads(natige.bazikonha)
        if bazikonha[0] == player:

        if kaar == "movement":
            x2 = request.form['x']
            y2 = request.form['y']
            return def_qurid.move(player, NAME, x2, y2)
        elif kaar == "DIVAR":
            x = request.form['x']
            y = request.form['y']
            jahat = request.form['jahat']
        else:
            return "check your data"
