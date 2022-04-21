from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class ProjetForm(FlaskForm):
    id_projet = IntegerField("ID projet", validators=[DataRequired()])
    titre=StringField("Titre projet:", validators=[DataRequired()])
    submit=SubmitField("Sauvegarder")
