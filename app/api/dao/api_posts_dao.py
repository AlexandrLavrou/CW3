import json

from flask import jsonify

from app.posts.dao.posts_dao import get_all_posts
from config import PATH_POSTS
from utils import load_essence


def get_all_api_posts():
    posts_data = load_essence(PATH_POSTS)
    return jsonify(posts_data)


        # posts_data.jsonify())


def get_api_post_by_pk(pk: int):
    posts_data = get_all_posts()
    # if type(pk) != int:
    #     raise TypeError(f"pk must be integer it`s {type(pk)}")
    if int(pk) not in range(1, len(posts_data)):
        raise ValueError(f"pk must by in range(1, {len(posts_data)})")

    for _post in posts_data:
        if _post["pk"] == int(pk):
            return jsonify(_post)



        # json.dumps(user_posts))

