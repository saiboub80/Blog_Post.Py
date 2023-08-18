from flask import Flask, render_template
from flask_bootstrap5 import Bootstrap





#############connections########


app = Flask(__name__)
Bootstrap(app)




########Routes###############
@app.route('/')
def navbar():
    return render_template("navbar.html")


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/register")
def register():
    render_template('register.html')

@app.route("/footer")
def footer():
    return render_template("footer.html")


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/make-post")
def make_post():
    return render_template("make_post.html")




if __name__ == '__main__':
    app.run(debug=True)





