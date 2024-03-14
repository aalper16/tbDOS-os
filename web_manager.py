from flask import Flask, render_template, redirect, request
from packages import process, current_time, process_toml

app = Flask(__name__)

@app.route('/')
def main():
    users = process_toml.get_data('reg/user.toml')  # Do not convert to string
    user = users.get('name', '')  # Get the 'name' key or use an empty string if not found
    coms = process_toml.get_data('reg/proc.toml')
    com = coms.get('msg', '')
    return render_template('main.html', user=user, com=com)

app.run(debug=True)
