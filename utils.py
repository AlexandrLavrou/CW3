import json
import os

from typing import List

from pydantic import BaseModel, TypeAdapter

from config import PATH_COMMENTS, PATH_POSTS


def load_essence(path):
    with open(path, "r", encoding="utf-8") as file:
        essence_data = json.load(file)
        return essence_data


#
# print(os.listdir())
# user_posts = load_essence("posts.json")
# print(user_posts)
# print(os.listdir("data"))
# with open("/data/comments.json", "r", encoding="utf-8") as file:
#     essence_data = json.load(file)
# print(essence_data)

# print(load_essence("data/posts.json"))
# print(load_essence("/data/comments.json"))


def get_users_from_posts(path_posts):
    user_data_posts = load_essence(path_posts)
    if not user_data_posts:
        raise ValueError(f"it have to be list")
    user_list = []
    for user in user_data_posts:
        user_list.append(user["poster_name"])
    return user_list


# with open("posts.json", "r", encoding="utf-8") as file:
#     essence_data = json.load(file)
#     print(essence_data)


def get_users_from_comments(path_comments):
    user_comments = load_essence(path_comments)
    if not user_comments:
        raise ValueError(f"it have to be list")
    user_list = []
    for user in user_comments:
        user_list.append(user["commenter_name"])
    return user_list


def get_all_users(path_posts, path_comments):
    users = get_users_from_posts(path_posts).extend(get_users_from_comments(path_comments))
    return users

#
#
#
# class UserDAO(BaseModel):
#     user: str
#
#     def _load_users(self, path):
#         with open(path, "r", encoding="utf-8") as file:
#             users_data = json.load(file)
#             return users_data
#
#     def get_users_comments(self):
#         users_data = self._load_users(PATH_COMMENTS)
#         users_list = []
#         for user in users_data:
#             users_list.append(user["commenter_name"])
#         ta = TypeAdapter(List[UserDAO])
#         essence_users = ta.validate_python(users_list)
#         return essence_users
#
#     def get_users_posts(self):
#         users_data = self._load_users(PATH_POSTS)
#         users_list = []
#         for user in users_data:
#             print(user)
#             users_list.append(user["poster_name"])
#         ta = TypeAdapter(List[UserDAO])
#         essence_users = ta.validate_python(users_list)
#         return essence_users
#
#     def get_all_users(self):
#         all_users = self.get_users_comments().extend(self.get_users_posts())
#         # print(type(all_users))
#         set_users = set(all_users)
#         return set_users


#
#
# print(user_list)
# print(user_posts)
#
# u = UserDAO.get_users_comments
#
# print(type(u))
# up = UserDAO.get_users_posts
#
# print(up)
#
#
# u_all = UserDAO.get_all_users
#
# # print(type(u_all))
#
# # print(u)
# # print(type(up))
# # print(up)
# print(u_all)
#
#
# # for _u in u_all:
# #     print(_u)
