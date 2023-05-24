from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de usuario de ejemplo
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username not in users or users[username] != password:
        return redirect(url_for('index'))
    else:
        return "Inicio de sesión exitoso"

if __name__ == '__main__':
    app.run(debug=True)
