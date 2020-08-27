from flask import Flask

from cmds import populate_db


def create_app():
    app = Flask(__name__)

    from .stuff import stuff
    app.register_blueprint(stuff)

    app.cli.command()(populate_db)

    return app


if __name__ == '__main__':
    application = create_app()
    application.run()
