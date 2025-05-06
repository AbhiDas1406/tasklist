from flask import Flask, url_for, redirect,request, render_template, make_response
app = Flask(__name__)

tasklist = [['Walk Dog', True], ['Wash Dishes', False], ['Watch Movie', True]]

@app.route('/')
def home():
    return render_template('tasklist.html', TaskList = tasklist)

if __name__ == '__main__': 
    app.run(debug = True, port=5000)