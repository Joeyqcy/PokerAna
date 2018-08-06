from flask import Blueprint, render_template, request
from app.funcs.statistic import _statistic_5cards, _statistic_7cards, _statistic_games, _statistic_preflop


stats = Blueprint('stats', __name__, template_folder='templates')


@stats.route('/index', methods=['GET'])
def stats_index():
    return render_template('stats/index.html')


@stats.route('/5cards', methods=['GET', 'POST'])
def _5cards():
    if request.method == 'POST':
        hand_count = int(request.form.get('hand_count'))
        result = _statistic_5cards(hand_count)
        return render_template('stats/result_5cards.html', result=result)
    return render_template('stats/5cards.html')


@stats.route('/7cards', methods=['GET', 'POST'])
def _7cards():
    if request.method == 'POST':
        hand_count = int(request.form.get('hand_count'))
        result = _statistic_7cards(hand_count)
        return render_template('stats/result_7cards.html', result=result)
    return render_template('stats/7cards.html')


@stats.route('/games', methods=['GET', 'POST'])
def _games():
    if request.method == 'POST':
        players = int(request.form.get('players'))
        games = int(request.form.get('games'))
        result = _statistic_games(players, games)
        return render_template('stats/result_games.html', result=result)
    return render_template('stats/games.html')


@stats.route('/preflop', methods=['GET', 'POST'])
def _preflop():
    if request.method == 'POST':
        c1 = request.form.get('c1')
        c2 = request.form.get('c2')
        c3 = request.form.get('c3')
        c4 = request.form.get('c4')
        games = 5000
        result = -_statistic_preflop(c1, c2, c3, c4, games)
        return render_template('stats/result_preflop.html', result=result)
    return render_template('stats/preflop.html')