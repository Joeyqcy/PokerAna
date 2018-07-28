from flask_script import Manager, Command

PokerCommand = Manager()

from .init_db import init_db
PokerCommand.add_command('init_db', Command(init_db))

from .statistic import statistic_5cards
PokerCommand.add_command('statistic_5cards', Command(statistic_5cards))


from .theory_prob import theory_prob_5cards
PokerCommand.add_command('theory_prob_5cards', Command(theory_prob_5cards))