import logging

from flask import Blueprint, redirect, render_template

from app.bookmarks.dao.bookmarks_dao import add_bookmark, remove_bookmark, check_bookmarks, get_all_bookmarks
from config import PATH_BOOKMARKS

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__)

logger = logging.getLogger("basic")


@bookmarks_blueprint.route("/bookmarks/add/<post_id>")
def add_bookmark_page(post_id: int):
    if check_bookmarks(PATH_BOOKMARKS, post_id):

        logger.debug(f"type(post_id) {post_id}")
        logger.debug(f"TypeError: {TypeError}")

        add_bookmark(PATH_BOOKMARKS, post_id)

    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<post_id>")
def remove_bookmark_page(post_id):

    remove_bookmark(PATH_BOOKMARKS, post_id)

    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks")
def bookmarks_page():
    bookmark_posts = get_all_bookmarks(PATH_BOOKMARKS)

    return render_template("bookmarks.html", bookmark_posts=bookmark_posts)
