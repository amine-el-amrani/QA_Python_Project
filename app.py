from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database (for simplicity)
users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"}
]

# GET: Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET: Retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    return jsonify(user)

# POST: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        abort(400)
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": request.json['name']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT: Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    if not request.json or 'name' not in request.json:
        abort(400)
    user['name'] = request.json['name']
    return jsonify(user)

# DELETE: Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=False)