from flask import Blueprint, render_template, request
from app.funcs.theory import _prob_5cards, _prob_7cards, _prob_preflop


theory = Blueprint('theory', __name__, template_folder='templates')


@theory.route('/index', methods=['GET'])
def theory_index():
    return render_template('theory/index.html')


@theory.route('/5cards', methods=['GET', 'POST'])
def _5cards():
    if request.method == 'POST':
        result = _prob_5cards()
        return render_template('theory/result_5cards.html', result=result)
    return render_template('theory/5cards.html')


@theory.route('/7cards', methods=['GET', 'POST'])
def _7cards():
    if request.method == 'POST':
        result = _prob_7cards()
        return render_template('theory/result_7cards.html', result=result)
    return render_template('theory/7cards.html')


@theory.route('/preflop', methods=['GET', 'POST'])
def _preflop():
    if request.method == 'POST':
        c1 = request.form.get('c1')
        c2 = request.form.get('c2')
        c3 = request.form.get('c3')
        c4 = request.form.get('c4')
        result = _prob_preflop(c1, c2, c3, c4)
        return render_template('theory/result_preflop.html', result=result)
    return render_template('theory/preflop.html')