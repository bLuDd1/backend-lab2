import uuid
from flask import jsonify, request
from src import app
from datetime import datetime

users = {}
categories = {}


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
    return f"Category deleted by {user_id} id"


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


@app.get('/category')
def get_category():
    return list(categories.values())


@app.post('/category')
def create_category():
    category_data = request.args.get("data")
    category_id = uuid.uuid4().hex
    category = {"id": category_id, "data": category_data}
    categories[category_id] = category
    return category


@app.delete('/category/<category_id>')
def delete_category(category_id):
    del categories[category_id]
    return f"Category deleted by {category_id} id"


if __name__ == '__main__':
    app.run(debug=True)
