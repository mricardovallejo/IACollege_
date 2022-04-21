from flask import render_template

from app_demandes import app
from app_demandes.forms import ProjetForm
from flask import flash, render_template, request, redirect, url_for, send_from_directory

@app.route('/welcome')
def welcome():
    return "Bienvenue "


@app.route('/')
@app.route('/index')
def index():
    projets = {'titre': 'Placement de plateforme'}
    return render_template('index.html', title='Accueil', mod=projets)

@app.route('/index2')
def index2():
    projets = {'titre': 'Placement de plateforme'}
    return '''
<html>
    <head>
        <title>Accueil – Projet demandes de travail</title>
    </head>
    <body>
        <h1>Projet : ''' + projets['titre'] + '''!</h1>
    </body>
</html>'''


@app.route('/index6')
def upload_form():
	return render_template('upload.html')

