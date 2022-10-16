from flask import Flask, jsonify
from api_db import results_full, results_name, results_gender, results_path_avatar, results_residential_address

app = Flask(__name__)


@app.route('/post/users/', methods=['POST'])
def post_all():
    return jsonify(results_full)


@app.route('/post/users/full_name', methods=['POST'])
def post_full_name():
    return jsonify(results_name)


@app.route('/post/users/gender', methods=['POST'])
def post_gender():
    return jsonify(results_gender)


@app.route('/post/users/path_avatar', methods=['POST'])
def post_path_avatar():
    return jsonify(results_path_avatar)


@app.route('/post/users/residential_address', methods=['POST'])
def post_residential_address():
    return jsonify(results_residential_address)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
