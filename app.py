from flask import Flask, url_for, redirect,request, render_template, make_response
from db import getTaskList, addTask
app = Flask(__name__)

# tasklist = [['Walk Dog', True], ['Wash Dishes', False], ['Watch Movie', True]]


@app.route('/')
def home():
    tasklist = getTaskList()
    return render_template('tasklist.html', TaskList = tasklist)

@app.route('/add', methods = ['POST'])
def add():
    taskname = request.form['taskName']
    duedate = request.form['dueDate']
    addTask(taskname, duedate)
    return redirect(url_for('home'))

if __name__ == '__main__': 
    app.run(debug = True, port=5000)