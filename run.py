import logging

from flask import Flask, render_template

from app.api.views import api_blueprint
from app.bookmarks.views import bookmarks_blueprint
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
app.register_blueprint(bookmarks_blueprint)

logger = logging.getLogger("basic")


@app.errorhandler(404)
def page_not_found(e):
    logger.debug(f"user requests a non-existing address")
    return render_template("error.html", error=e), 404


@app.errorhandler(500)
def error_page(error):
    logger.debug(f"something went wrong status code 500")
    return render_template("error.html", error=error), 500


if __name__ == "__main__":
    app.run()



