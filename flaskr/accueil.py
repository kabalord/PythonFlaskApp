import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('accueil', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def accueil():
    return render_template('accueil/accueil.html')

@bp.route('/bands', methods=['GET'])
def bands():
    groupes = db.get_db().execute('SELECT * FROM Groupe').fetchall()
    print(groupes)
    return render_template('groupes-liste.html', groupes=groupes)