import pytest


@pytest.fixture
def keys_in_posts():
    return {"poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk"}

# def test_client():
#     app = run.app
#     return app.test_client()
