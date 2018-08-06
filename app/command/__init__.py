from flask_script import Manager, Command

PokerCommand = Manager()

from .init_db import init_db, upgrade_preflop
PokerCommand.add_command('init_db', Command(init_db))
PokerCommand.add_command('upgrade_preflop', Command(upgrade_preflop))

from .statistic import statistic_5cards,statistic_7cards, statistic_games, statistic_preflop
PokerCommand.add_command('statistic_5cards', Command(statistic_5cards))
PokerCommand.add_command('statistic_7cards', Command(statistic_7cards))
PokerCommand.add_command('statistic_games', Command(statistic_games))
PokerCommand.add_command('statistic_preflop', Command(statistic_preflop))

from .theory_prob import prob_5cards, prob_7cards, preflop
PokerCommand.add_command('prob_5cards', Command(prob_5cards))
PokerCommand.add_command('prob_7cards', Command(prob_7cards))
PokerCommand.add_command('preflop', Command(preflop))
