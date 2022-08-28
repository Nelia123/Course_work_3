import logging

from flask import Blueprint, render_template, request, jsonify

import utils


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


logger_one = logging.getLogger()
logger_one.setLevel("INFO")
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler = logging.FileHandler(filename="api.log")
file_handler.setFormatter(formatter_one)
console_handler = logging.StreamHandler()
logger_one.addHandler(console_handler)
logger_one.addHandler(file_handler)


@main_blueprint.route("/")
def main_page():
    posts = utils.get_posts_all()
    logger_one.info("Главная страница запрошена")
    return render_template('index.html', posts=posts)


@main_blueprint.route("/posts/<int:post_id>")
def get_post(post_id):
    posts = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    logger_one.info(f"Страница поста {post_id} запрошена")
    return render_template('post.html', posts=posts, comments=comments)


@main_blueprint.route("/search/")
def search_posts():
    query = request.args.get('s', '')
    posts = utils.search_for_posts(query)
    logger_one.info("Поиск постов запрошен")
    return render_template('search.html', query=query, posts=posts)


@main_blueprint.route("/users/<username>")
def search_users(username):
    posts = utils.get_posts_by_user(username)
    logger_one.info(f"Страница пользователя {username} запрошена")
    return render_template('user-feed.html', posts=posts)


@main_blueprint.route("/tag/<tagname>")
def page_tag(tagname):
    posts = utils.get_post_by_tag(tagname)
    render_template('tag.html', posts=posts)


@main_blueprint.route("/api/posts", methods=['GET'])
def json_posts():
    posts = utils.get_posts_all()
    logger_one.info("Запрос /api/posts")
    return jsonify(posts)


@main_blueprint.route("/api/posts/<int:post_id>", methods=['GET'])
def json_post_one(post_id):
    post = utils.get_post_by_pk(post_id)
    logger_one.info(f"Запрос /api/posts {post_id}")
    return jsonify(post)