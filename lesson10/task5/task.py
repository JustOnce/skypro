from flask import Flask

app = Flask(__name__)

vocab = {
    'cat': 'dog',
    'python': 'go',
    'flask': 'django',
    'postgresql': 'mysql',
    'junior': 'middle'
}


if __name__ == '__main__':
    app.run()
