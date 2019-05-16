"""Migrations scripts to create the database tables
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api import app, database

migrate = Migrate(app, database)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


@manager.command
def create_db():
    database.create_all()
    database.session.commit()


if __name__ == "__main__":
    manager.run()
    database.create_all()
