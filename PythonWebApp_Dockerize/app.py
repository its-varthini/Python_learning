from flask import Flask

app = Flask(__name__)

@app.route("/")
def run():
    return "{\"message\":\"Hey there python\"}"

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=int("3000"))
