from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.model import db
from config import config
from app.command import PokerCommand

app = create_app(config)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('poker', PokerCommand)

if __name__ == '__main__':
    manager.run()
