from flask import Flask, render_template





#############connections########


app = Flask(__name__)




########Routes###############
@app.route('/')
def home():
    return render_template("Navbar.html")



if __name__ == '__main__':
    app.run(debug=True)





