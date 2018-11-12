from flask import render_template
from . import home
from ..models import Queries

@home.route('/')
def home():
    districts = []
    ids = []
    rows = Queries().districts()

    for row in rows:
        ids.append(row[0])
        districts.append(row[1])

    return render_template('home/home.html', rows=rows)
