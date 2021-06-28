#test_json.py

from app import app
from flask import json

def test_processjson(app,client):
    response = app.test_client().post(
        '/v1/sanitized/input/',
        req=json.dumps({'payload':'xyz@gmail.com'}),
        content_type='application/json',
    )
    req=json.loads(response.get_data(as_text=True))

    assert response.status_code==200
    assert string_check.search(payload)==None




