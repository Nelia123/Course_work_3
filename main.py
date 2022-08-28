from flask import Flask, render_template
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, get_post_by_pk

app = Flask(__name__, template_folder='templates')
@app.route("/")
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)

@app.route("/posts/<postid>")
def post_page(postid):
    posts = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('posts.html', posts=posts, comments=comments)


if __name__ == "__main__":
    app.run()
