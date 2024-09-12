from app.posts.dao.posts_dao import get_all_posts
from config import PATH_POSTS, PATH_COMMENTS
from utils import get_all_users


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


