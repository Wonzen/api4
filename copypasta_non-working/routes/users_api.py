from flask import Blueprint, jsonify
from copypasta.users.usersModel import UserModel

main = Blueprint("users_blueprint", __name__)


@main.route('/api/user_api')
def post_users():
    try:
        users = UserModel.post_users()
        return jsonify(users)

    except Exception as ex:

        return jsonify({'message': str(ex)}), 500
