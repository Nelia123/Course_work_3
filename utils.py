import json


def get_posts_all():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    posts_by_name = []
    posts = get_posts_all()
    for post in posts:
        if post["poster_name"].lower() == user_name.lower():
            posts_by_name.append(post)
    if len(posts_by_name) == 0:
        raise ValueError("Пользователь не найден")
    return posts_by_name


def get_comments_by_post_id(post_id):
    posts_by_id = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            if post["post_id"] == post_id:
                posts_by_id.append(post)
        if len([posts_by_id]) == 0:
            raise ValueError("Пост не найден")
    return posts_by_id


def search_for_posts(query):
    posts_by_query = []
    posts = get_posts_all()
    for post in posts:
        if query.lower() in post["content"].lower():
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post


def get_post_by_tag(query):
    posts_by_tag = []
    posts = get_posts_all()
    for post in posts:
        if query in posts:
            posts_by_tag.append(post)
    return posts_by_tag