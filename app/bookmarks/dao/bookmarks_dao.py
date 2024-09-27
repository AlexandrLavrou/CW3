from app.posts.dao.posts_dao import get_all_posts
from utils import load_essence, save_essence, remove_essence


def add_bookmark(path_bookmarks, post_id):
    bookmarks = load_essence(path_bookmarks)
    bookmark = {"pk": int(post_id)}
    bookmarks.append(bookmark)

    # if check_bookmarks(path_bookmarks, post_id):

    save_essence(path_bookmarks, bookmarks)


def remove_bookmark(path_bookmarks, post_id):
    remove_essence(path_bookmarks, post_id)


def check_bookmarks(path_bookmarks, post_id):
    bookmarks = load_essence(path_bookmarks)
    for bookmark in bookmarks:
        if int(post_id) == int(bookmark["pk"]):

            return False

    return True


def get_all_bookmarks(path_bookmarks):
    posts_data = get_all_posts()
    bookmarks = load_essence(path_bookmarks)

    posts_with_bookmarks = []
    for bookmark in bookmarks:
        for post in posts_data:
            if int(bookmark["pk"]) == int(post["pk"]):
                posts_with_bookmarks.append(post)
    return posts_with_bookmarks
