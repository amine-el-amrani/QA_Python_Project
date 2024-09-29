from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)