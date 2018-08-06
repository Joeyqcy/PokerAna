from flask import render_template
from .theory import theory
from .stats import stats

def home_page():
    return render_template('index.html')