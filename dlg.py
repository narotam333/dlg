from flask import Flask, abort
from flask import jsonify
app = Flask(__name__)


@app.route('/total')
def total():
    """
    total function returns the sum of number for the list. Its using python sum function. For the requirments of
    of assignment the list is hardcorded for time being.
    :return:sum of the number of list
    """
    try:
        numbers_to_add = list(range(10000001))
        tot_val = sum(numbers_to_add)
        return jsonify({'total': tot_val})
    except Exception as e:
        abort(400, str(e))


if __name__ == '__main__':
    app.run()
