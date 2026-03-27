from flask import Flask, request, jsonify, render_template
from planner import plan_task
from executor import execute_steps

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    task = data.get("task")

    steps = plan_task(task)
    result = execute_steps(steps)

    return jsonify({
        "steps": steps,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
