from flask import render_template, request
from . import home
from flask_wtf import FlaskForm
from wtforms import SelectField
from ..models import Districts

class Form(FlaskForm):
    district = SelectField('district', choices=[])

@home.route('/', methods=['GET', 'POST'])
def home():
    rows = Districts().districts()
    form = Form()
    form.district.choices = rows

    id = form.district.data

    output = 'Default'

    for row in rows:
        rowId = str(row[0])
        if rowId == id:
            output = row[1]

    if request.method == 'POST':
        return '<h1>You selected: {} </h1>'.format(output)

    return render_template('home/home.html', form=form)
