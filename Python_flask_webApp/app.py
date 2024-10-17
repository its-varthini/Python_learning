from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/welcome")
def welcome():
    return "Welcome to Varthini's Flask App!"
   

if __name__ == "__main__":
    app.run(debug=True)
