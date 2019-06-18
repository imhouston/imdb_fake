#!/usr/bin/env python

from flask import Flask, request, Response
from jsonrpcserver import dispatch, method
import requests

SOLR_HOST = ""

app = Flask(__name__)


@method
def query_search(query_text: str):
    pass
    # query_string = "http://" + SOLR_HOST
    # res = requests.get(query_string)
    # query_result = res.json()
    return


@app.route("/", methods=['GET', 'POST'])
def index():
    req = request.get_data().decode()
    response = dispatch(req)
    return Response(str(response), response.http_status, mimetype="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
