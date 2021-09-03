from flask import Flask, render_template, request

from const import CANDIDATES
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    result = CANDIDATES[:]

    if request.method == 'GET':
        position = request.args.get('position')

        if position:
            result = []

            for candidate in CANDIDATES:
                if position.lower() in candidate['position'].lower():
                    result.append(candidate)

    return render_template('candidates.html', candidates=result)


if __name__ == '__main__':
    app.run()
