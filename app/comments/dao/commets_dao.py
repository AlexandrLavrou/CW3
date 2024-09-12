from pydantic import BaseModel

from config import PATH_COMMENTS
from utils import load_essence


class CommentsDAO(BaseModel):
    post_id: int
    commenter_name: str
    comment: str
    pk: int


def get_all_comments():
    comments_data = load_essence(PATH_COMMENTS)
    return comments_data

    # ta = TypeAdapter(List[CommentsDAO])
    # essence_comments = ta.validate_python(comments_data)
    # return essence_comments


def get_comments_by_post_id(post_id):
    comments_data = get_all_comments()
    comments_post_id = []
    for comment in comments_data:
        if comment["post_id"] == int(post_id):
            comments_post_id.append(comment)
    return comments_post_id

    # try:
    #     len(comments_post_id) == 0 or post_id is None
    # except ValueError:
    #     print("ValueError")
    # else:





