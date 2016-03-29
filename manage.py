from flask_script import Manager, Shell, Server
from flaskg.app import create_app
from flask_migrate import MigrateCommand, upgrade
from flaskg.extensions import db
from flask import current_app

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=current_app, db=db)


manager.add_command('shll', Shell(make_context=make_shell_context))


@manager.command
def initdb():
    upgrade()


if __name__ == '__main__':
    manager.run()
