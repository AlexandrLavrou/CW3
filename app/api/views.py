import logging
from flask import Blueprint, render_template

from app.api.dao.api_posts_dao import get_all_api_posts, get_api_post_by_pk
from app.posts.dao.posts_dao import get_all_posts

api_blueprint = Blueprint("api_blueprint", __name__)

logger = logging.getLogger("basic")


@api_blueprint.route("/api/posts", methods=["GET"])
def api_index_page():
    try:
        posts_data = get_all_api_posts()
        logger.debug("attempt to load json file with posts")
    except FileNotFoundError as error:

        logger.debug(f" file with posts not found")
        return render_template("error.html", error=error)
    return posts_data


@api_blueprint.route("/api/posts/<post_id>", methods=["GET"])
def api_post_page(post_id):
    posts_data = get_all_posts()
    try:
        post = get_api_post_by_pk(post_id)
        logger.debug(f"attempt to load json post by post id: {post_id}")

    except ValueError as error:
        logger.debug(f"pk must by in range(1, {len(posts_data)})")
        return render_template("error.html", error=error)

    except FileNotFoundError as file_error:
        logger.debug(f" post with post_id: {post_id} not found")
        return render_template("error.html", error=file_error)

    return post

