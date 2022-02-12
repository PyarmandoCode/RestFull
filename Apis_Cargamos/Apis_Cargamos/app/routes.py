from flask import render_template
from app import app,db
from app.models import Grupos

@app.route('/')
def index():
    template_name="index.html"
    grupos=Grupos.query.all()
    return render_template(template_name,grupos=grupos)