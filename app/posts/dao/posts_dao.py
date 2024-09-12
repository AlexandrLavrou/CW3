import json
from pprint import pprint
from typing import List

from pydantic import BaseModel, TypeAdapter

from config import PATH_POSTS, PATH_POSTS_LOCAL, PATH_COMMENTS
from utils import load_essence, get_all_users


# def get_all_posts():
#     posts_data = load_essence(PATH_POSTS)
#     ta = TypeAdapter(List[PostsDAO])
#     essence_posts = ta.validate_python(posts_data)
#     return essence_posts


class PostsDAO:
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int


def get_all_posts():
    posts_data = load_essence(PATH_POSTS)
    return posts_data


def get_post_by_pk(pk):
    posts_data = get_all_posts()

    # if type(pk) != int:
    #     raise TypeError(f"pk must be integer, it`s {type(pk)}")
    if int(pk) not in range(1, len(posts_data)):
        raise ValueError(f"pk must by in range(1, {len(posts_data)})")

    for _post in posts_data:
        if _post["pk"] == int(pk):
            return _post


def get_posts_by_content(search_str):
    posts_data = get_all_posts()
    result_posts = []
    for post in posts_data:
        if search_str in post["content"]:
            result_posts.append(post)

    return result_posts

# print(len(get_posts_by_content("Ага")))


def get_post_by_user(user_name):
    posts_data = get_all_posts()
    user_posts = []
    all_users = get_all_users(PATH_POSTS, PATH_COMMENTS)
    if user_name not in all_users:
        raise ValueError(f"User with name:{user_name} is not exist")

    for _post in posts_data:
        if _post["poster_name"] == user_name.lower():
            user_posts.append(_post)
    if not user_posts:
        raise ValueError(f"User with name:{user_name} doesn't have posts, this user has made comments")
    return user_posts
