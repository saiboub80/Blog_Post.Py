from flask import Flask, render_template,redirect, url_for
from flask_bootstrap5 import Bootstrap
from flask_sqlalchmy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField ,Submitfield
from wtforms.validations import DataRequired, URL
from flask_crediton import Ckeditor ,CKeditorField
from datetime import date




app = Flask(__name__)
app.config[SECRET_KEY]= '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


###CONNECT TO DB ####
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///posts.db'
db= SQLAlchemy()
db.init_app(app)


#####Configure Table

class BlogPost(db.Model):
    id= db.column(db.Integer,primary_key=True)
    title=db.column(db.String(250),unique=True, nullable=False)
    subtitle=db.column(db.String(250),nullable=False)
    date = db.column(db.String(250), nullable=False)
    body = db.column(db.Text, nullable=False)
    author=db.column(db.String(250),nullable=False)
    img_url=db.column(db.String(250),nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result= db.session.execute(db.select(BlogPost))
    posts= result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def Show_post(post_id):
    requested_post= db.get_or_404(BlogPost,post_id)
    return render_template('post.html',post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True, port=5002)









