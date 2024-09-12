import logging

from flask import Blueprint, render_template, request

from app.comments.dao.commets_dao import get_comments_by_post_id
from app.posts.dao.posts_dao import get_all_posts, get_post_by_pk, get_posts_by_content

posts_blueprint = Blueprint("posts_blueprint", __name__)

logger = logging.getLogger("basic")


@posts_blueprint.route("/", methods=["GET"])
def index_page():
    posts = get_all_posts()

    return render_template("index.html", posts=posts)


@posts_blueprint.route("/posts/<pk>")
def post_page(pk):
    try:
        post = get_post_by_pk(pk)
    except ValueError as error:
        logger.debug(f"Pk value out of range: {error}")
        return render_template("error.html", error=error)
    except TypeError as error:
        logger.debug(f"some error, description: {error}" )
        return render_template("error.html", error=error)

    comments = get_comments_by_post_id(pk)
    logger.debug(f"get comments for the post with pk = {pk}")
    len_comments = len(comments)

    return render_template("post.html", post=post, comments=comments, len_comments=len_comments)


@posts_blueprint.route("/search/")
def search_page():
    query = request.args.get("s", "")
    logger.debug(f"get search request {query}")
    found_posts = get_posts_by_content(query)
    len_found_posts = len(found_posts)

    return render_template("search.html", found_posts=found_posts, query=query, len_found_posts=len_found_posts)

