from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    charset = ''
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_lowercase:
        charset += string.ascii_lowercase
    if use_numbers:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()_-+=<>?/[]{}|"

    if not charset:
        return ''

    password = []

    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()_-+=<>?/[]{}|"))

    while len(password) < length:
        password.append(random.choice(charset))

    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    password = generate_password(
        length=int(data.get('length', 16)),
        use_uppercase=data.get('uppercase', True),
        use_lowercase=data.get('lowercase', True),
        use_numbers=data.get('numbers', True),
        use_symbols=data.get('symbols', True)
    )
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
