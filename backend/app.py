from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Ehsan"},
    {"id": 2, "name": "Chatty"}
]

# Home route
@app.route("/")
def home():
    return "Welcome Ehsan"

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Get a specific user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
