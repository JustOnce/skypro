from json import dumps

from flask import Flask, request

app = Flask(__name__)


def load_users():
    from lesson10_1.task6.users import users
    return users


@app.route('/filter/')
def filter_dict():
    users = load_users()
    result = []

    for user in users:
        for key, value in request.args.items():
            if key not in user:
                continue

            if user[key].lower() != value.lower():
                break
        else:
            result.append(user)

    return dumps(result)


def sort_dict():
    users = load_users()

    return f''


if __name__ == '__main__':
    app.run()
