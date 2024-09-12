from flask import Flask

from app.api.views import api_blueprint
from app.logger.logger import logging_it
from app.posts.views import posts_blueprint
from app.users.views import users_blueprint

app = Flask(__name__)

logging_it()

app.config['JSON_AS_ASCII'] = False
app.config['UTF-8'] = True
app.json.ensure_ascii = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run()
