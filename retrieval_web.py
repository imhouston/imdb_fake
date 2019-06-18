#!/usr/bin/env python

from flask import Flask, request, jsonify

SOLR_HOST = ""

app = Flask(__name__)


def query_search(query_json: dict):
    # query_string = "http://" + SOLR_HOST
    # res = requests.get(query_string)
    # query_result = res.json()
    return {}


def add_sponsor(sponsor_id: str):
    pass
    # query_string = "http://" + SOLR_HOST
    # res = requests.get(query_string)
    # query_result = res.json()
    return {}


@app.route("/search", methods=['POST'])
def search_api():
    req = request.get_json()
    search_results = query_search(req)

    return jsonify(search_results)


@app.route("/sponsor", methods=['GET'])
def sponsor_api():
    if request.args.get('id'):
        sponsor_id = request.args.get('id')
    sponsor_status = add_sponsor(sponsor_id)
    return jsonify(sponsor_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
