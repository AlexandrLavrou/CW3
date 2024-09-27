import json
import os

from typing import List

from pydantic import BaseModel, TypeAdapter

from config import PATH_COMMENTS, PATH_POSTS


def load_essence(path):
    with open(path, "r", encoding="utf-8") as file:
        essence_data = json.load(file)
        return essence_data


def save_essence(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def remove_essence(path, essence_id):
    """
    Delete essence by pk
    :param path: path to file with list of essence
    :param essence_id: personal key for the essence
    :return: updated list of essences
    """
    essences = load_essence(path)
    for index, essence in enumerate(essences):
        if int(essence["pk"]) == int(essence_id):
            del essences[index]
            break
    save_essence(path, essences)

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


def get_all_users(path_posts, path_comments):
    user_data_posts = load_essence(path_posts)

    users_list = []
    for user in user_data_posts:
        if user not in users_list:
            users_list.append(user["poster_name"])
        else:
            continue

    user_comments = load_essence(path_comments)

    for user in user_comments:
        if user not in users_list:
            users_list.append(user["commenter_name"])
        else:
            continue

    return users_list


def convert_post(post):
    content = post["content"]
    content_list = content.split(" ")
    updated_content = []
    for word in content_list:
        if word[0] == "#":
            print(word)
            new_word = f"<a href='/tag/{word[1:]}'>{word}</a>"
            print(new_word)
            word = new_word
        updated_content.append(word)
    post["content"] = " ".join(updated_content)
    return post


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
