"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""



from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]


@app.route('/')
def home():
    return render_template('index.html', tasks=TASKS)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        status = request.form.get('status')
        priority = request.form.get('priority')

        new_task = {
            'id': len(TASKS) + 1,
            'title': title,
            'status': status,
            'priority': priority
        }

        TASKS.append(new_task)
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/task/<int:id>')
def task_detail(id):
    task = None
    for t in TASKS:
        if t['id'] == id:
            task = t
            break

    return render_template('task.html', task=task, task_id=id)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
