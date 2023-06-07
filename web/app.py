from flask import Flask, render_template, request
from .rating import read_rating, create_user
from os import system
from jinja2 import Environment

def enumerate_filter(input_list):
    return enumerate(input_list)


system('service ssh start')
app = Flask(__name__)
app.jinja_env.filters['enumerate'] = enumerate_filter

@app.route("/")
def home():
    rating  = read_rating()
    rating = sorted(rating.items(), key=lambda x: x[1][0], reverse=True)
    return render_template('rating.html', rating=rating)

@app.route('/user/<name>')
def user(name=None):
    rating  = read_rating()
    return render_template('user_rating.html', name=name, rating=rating)

@app.route('/create-user', methods=['POST'])
def create_user_page():
    username = request.form['username']
    if username.isalnum() and not username.isdigit():
        create_user(username)
        return render_template('status_page.html', status='Success', message=f'New user {username} successfully created. Default password is 1234')
    return render_template('status_page.html', status='Failure', message=f'Failed to create new user {username}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')