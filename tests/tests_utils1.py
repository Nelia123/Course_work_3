import pytest
from utils import get_posts_all, get_post_by_pk, get_posts_by_user, get_comments_by_post_id, search_for_posts


def test_get_posts_all():
    posts_all = get_posts_all()
    assert type(posts_all) == list, "возвращается не список"
    assert len(posts_all) > 0, "возвращается пустой список"


def test_get_posts_by_user():
    posts = get_posts_by_user("leo")
    for post in posts:
        assert post["poster_name"] == "leo", "возвращаются неверные посты"
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"


def test_get_comments_by_post_id():
    comments = get_comments_by_post_id(4)
    for comment in comments:
        assert comment["post_id"] == 4, "возвращаются неверные посты"
    assert type(comments) == list, "возвращается не список"
    assert len(comments) > 0, "возвращается пустой список"


def test_search_for_posts():
    posts = search_for_posts("на")
    for post in posts:
        assert "на" in post["content"]
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"


def test_get_post_by_pk():
    post = get_post_by_pk(1)
    assert post["pk"] == 1, "возвращается неправильный пост"
    assert type(post) == dict, "возвращается не список"