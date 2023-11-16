import uuid
from flask import jsonify, request
from src import app
from datetime import datetime

users = {}


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    health_status = {'status': 'OK', 'date': current_date}
    return jsonify(health_status)


@app.get('/user/<user_id>')
def get_user(user_id):
    user = users[user_id]
    return user


@app.delete('/user/<user_id>')
def delete_user(user_id):
    del users[user_id]
    return ""


@app.post('/user')
def create_user():
    user_data = request.args.get("data")
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "data": user_data}
    users[user_id] = user
    return user


@app.get('/users')
def get_users():
    return list(users.values())


if __name__ == '__main__':
    app.run(debug=True)
