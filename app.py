from flask import Flask
from flask import request
from flask import jsonify
import re

app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=["POST"])
def processjson():
    req = request.get_json()
    payload= req['payload']
    string_check = re.compile('[-=_!#$%^&*()<>?/|}1==1{~:]')

    if string_check.search(payload)==None:
        return jsonify({'result': 'sanitized'})
    else:
        return jsonify({'result': 'Unsanitized'})

if __name__ == "__main__":
    app.run(debug=True)
