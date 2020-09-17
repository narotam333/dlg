from flask import Flask, abort
from flask import jsonify
app = Flask(__name__)


@app.route('/total')
def total():
    try:
        numbers_to_add = list(range(10000001))
        tot_val = sum(numbers_to_add)
        return jsonify({'total': tot_val})
    except Exception as e:
        abort(400, str(e))


if __name__ == '__main__':
    app.run()
