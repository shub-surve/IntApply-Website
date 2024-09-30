from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS = [
    {"id": 1, "title": "Software Engineer","Location":"Mumbai", "description": "Develop software applications"},
    {"id": 2, "title": "Data Scientist","Location":"Pune", "description": "Analyze and interpret data"},
    {"id": 3, "title": "DevOps Engineer","Location":"Hydrabad", "description": "Ensure smooth operation of systems"},
    {"id": 3, "title": "Software Engineer","Location":"Bangalore", "description": "Ensure smooth operation of systems"}
]

@app.route("/")
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
