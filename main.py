from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date





app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
ckeditor = CKEditor(app)
Bootstrap5(app)


###CONNECT TO DB ####
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///posts.db'
db= SQLAlchemy()
db.init_app(app)

login_manager=LoginMager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(user,user_id)






#####Configure Table


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


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


@app.route('/new-post', methods=['GET','POST'])
def add_new_posrt():
    form= CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title= form.title.data,
            subtitle = form.subtitle.data,
            body=form.body.data,
            img_url = form.img_url.data,
            author =form.author.data,
            date=date.today().strftime('%B,%d,%Y')
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-posr.htm')

@app.route('/edit-post/<post_id>', methods=["GET","POST"])
def edit_post(post_id):
    post=db.get_or_404(BlogPost, post_id)
    edit_form= createPostForm(
        title = post.title,
        subtitle =post.subtitle,
        body=post.body,
        img_url = post.img_url,
        author = post.author,
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data,
        post.subtitle = edit_form.subtitle.data,
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post',post_id= post.id))
    return render_template('make_post.html',form=edit_form,is_edit=True)


    return render_template('make-post', form=edit_form,is_edit=True)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_delete=db.get_or_404(BlogPost,post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return render_template(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True, port=5002)









