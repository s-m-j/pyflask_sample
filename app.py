from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_there():
  return render_template("home.html")


@app.route("/test/")
def hello_world2():
  return "<p>Hello, World 2</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
