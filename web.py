from flask import Flask, render_template, redirect, request
from packages import process_toml
import toml

app = Flask(__name__)
sp = False
name = process_toml.get_data('reg/user.toml').get('name')  # Kullanıcı adını global olarak tanımlayın

@app.route('/')
def index():
    global name
    return render_template('index.html', name=name)

