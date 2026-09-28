from flask import Flask, jsonify, request

app = Flask(__name__)
todo_data = []


@app.route("/")
def index():
    return jsonify({"message": "Todo API", "endpoint": "/api/todo"})


@app.route("/api/todo")
def list_todo():
    return jsonify(todo_data)


@app.route("/api/todo", methods=["POST"])
def add_todo():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"message": "Invalid JSON data", "data": None}), 400

    task = payload.get("task")
    if task is None:
        return jsonify({"message": "Task is required", "data": None}), 400

    todo_data.append({"id": len(todo_data) + 1, "task": task})
    return jsonify({"message": "Todo added", "data": todo_data[-1]})


@app.route("/api/todo/<int:todo_id>")
def get_todo(todo_id):
    todo = next((item for item in todo_data if item["id"] == todo_id), None)
    if todo is None:
        return jsonify({"message": "Todo not found", "data": None}), 404
    return jsonify({"message": "Todo found", "data": todo})


if __name__ == "__main__":
    app.run(debug=False)