from flask import Flask, render_template, abort

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Message Zero','Message One','Message Two']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(404)
