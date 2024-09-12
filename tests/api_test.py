from run import app


def test_api_posts(keys_in_posts):
    response = app.test_client().get("/api/posts", follow_redirects=True)
    first_keys = set(response.json[0].keys())
    assert type(response.json) == list
    assert first_keys == keys_in_posts


def test_api_post(keys_in_posts):
    response = app.test_client().get("/api/posts/1", follow_redirects=True)
    first_keys = set(response.json.keys())
    assert type(response.json) == dict
    assert first_keys == keys_in_posts

def test_get_users_from_posts(path_posts):
    response = app.test_client().get("/users/johnny", follow_redirections=True)
