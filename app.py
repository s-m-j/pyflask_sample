from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id': 1,
    'title': "Data Analyst",
    'location': 'Moscow',
    'salary': 'Rub: 180000'
  },
  {
    'id': 2,
    'title': "Junior Data Analyst",
    'location': 'Moscow',
    'salary': 'Rub: 120000'
  },
  {
    'id': 3,
    'title': "Java Developer",
    'location': 'Moscow',
    'salary': 'Rub: 280000'
  },
  {
    'id': 4,
    'title': "Senior Data Analyst",
    'location': 'Moscow',
    'salary': 'Rub: 280000'
  }
]

@app.route("/")
def hello_there():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
