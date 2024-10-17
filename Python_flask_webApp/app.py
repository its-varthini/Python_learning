from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/welcome")
def welcome():
    return "Welcome to Varthini's Flask App!"

@app.route("/user")
def user():
    user = {"user":"admin"}
    return jsonify(user)

if __name__ == "__main__":
   //app.run(debug=True)
    app.run(debug=False, host="0.0.0.0", port="5000")
