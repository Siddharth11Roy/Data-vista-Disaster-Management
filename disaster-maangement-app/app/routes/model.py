
from flask import Blueprint, render_template

model_bp = Blueprint('model', __name__)

@model_bp.route('/cyclone')
def modelC():
    return render_template('modelC.html')

@model_bp.route('/hurricane')
def modelH():
    return render_template('modelH.html')

@model_bp.route('/volcano')
def modelV():
    return render_template('modelV.html')
