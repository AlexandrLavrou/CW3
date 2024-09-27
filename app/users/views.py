import logging

from flask import Blueprint, render_template

from app.posts.dao.posts_dao import get_post_by_user
from config import PATH_POSTS, PATH_COMMENTS
from utils import get_all_users

users_blueprint = Blueprint("users_blueprint", __name__)

logger = logging.getLogger("basic")


@users_blueprint.route("/users/<user_name>")
def user_posts_page(user_name):
    logger.debug(f"{type(get_all_users(PATH_POSTS, PATH_COMMENTS))}")
    logger.debug(f"{get_all_users(PATH_POSTS, PATH_COMMENTS)}")
    try:
        user_posts = get_post_by_user(user_name)
    except ValueError as error:
        return render_template("error.html", error=error)
    return render_template("user-feed.html", user_posts=user_posts)


