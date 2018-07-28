from flask_script import Manager, Command

PokerCommand = Manager()

from .init_db import init_db
PokerCommand.add_command('init_db', Command(init_db))

