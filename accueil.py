from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def accueil():
    return render_template('accueil.html')

@app.route('/bands', methods=['GET'])
def bands():
    groupes = db.get_db().execute('SELECT * FROM Groupe').fetchall()
    print(groupes)
    return render_template('groupes-liste.html', groupes=groupes)