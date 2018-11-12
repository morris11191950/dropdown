from flask import render_template, jsonify, json
from . import reference
from ..models import Queries

@reference.route('/reference/<int:district_id>', methods=['GET', 'POST'])
def references(district_id):
    rows = Queries().references(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j
