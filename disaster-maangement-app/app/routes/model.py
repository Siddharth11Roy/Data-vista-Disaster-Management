
from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect, url_for
from ..models.disaster_report import db, DisasterReport

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


@model_bp.route('/report-disaster', methods=['GET', 'POST'])
def report_disaster():
    if request.method == 'POST':
        report = DisasterReport(
            name=request.form['name'],
            email=request.form['email'],
            location=request.form['location'],
            disaster_type=request.form['disaster_type'],
            description=request.form.get('description', '')
        )
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('model.thank_you'))
    return render_template('report-disaster.html')

@model_bp.route('/thank-you')
def thank_you():
    return "<h2>Thank you for reporting the disaster. Authorities will respond promptly.</h2>"
