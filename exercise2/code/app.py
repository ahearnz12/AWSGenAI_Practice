from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
TASKS_FILE = 'tasks.json'

class Task:
    def __init__(self, name, priority):
        self.name = name
        try:
            self.priority = int(priority)
        except ValueError:
            self.priority = 1

    def to_dict(self):
        return {'name': self.name, 'priority': self.priority}

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(t['name'], t['priority']) for t in data]

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def add_task(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        self.save_tasks()

    def get_tasks(self):
        return [t.to_dict() for t in self.tasks]

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            return True
        return False

manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(manager.get_tasks())

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    manager.add_task(data['name'], data['priority'])
    return jsonify({'success': True})

@app.route('/api/tasks/<int:index>', methods=['DELETE'])
def remove_task(index):
    success = manager.remove_task(index)
    return jsonify({'success': success})

if __name__ == '__main__':
    app.run(debug=True)
