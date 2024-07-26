
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    try:
        results = db.session.execute(query).fetchall()
        return render_template('index.html', results=results)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    db.create_all()
    app.run()
