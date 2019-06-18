#!/usr/bin/env python

from flask import Flask, request, jsonify, Response

SOLR_HOST = ""

app = Flask(__name__)


def query_search(query_json: dict):
    # query_string = "http://" + SOLR_HOST
    # res = requests.get(query_string)
    # query_result = res.json()

    result = [{"id": "1",
               "title": "filmName1",
               "year": "1900",
               "rating": "5.5",
               "genres": ["genre1", "genre2"],
               "directors": ["director1", "director2"],
               "releaseDates": ["releaseDate1", "releaseDate2"],
               "top3Cast": ["actor1”", "actor2", "actor3"],
               "storyline": "example storyline",
               "synopsis": "example synopsis"},

              {"id": "2",
               "title": "filmName2",
               "year": "1901",
               "rating": "6.5",
               "genres": ["genre1", "genre2"],
               "directors": ["director1", "director2"],
               "releaseDates": ["releaseDate1", "releaseDate2"],
               "top3Cast": ["actor1”", "actor2", "actor3"],
               "storyline": "example storyline 2",
               "synopsis": "example synopsis 2"}]

    return result


# def add_sponsor(sponsor_id: str):
    # pass
    # query_string = "http://" + SOLR_HOST
    # res = requests.get(query_string)
    # query_result = res.json()
    # return {}


@app.route("/search", methods=['POST'])
def search_api():
    if request.is_json:
        try:
            req = request.get_json()
        except:
            return Response("Invalid JSON", status=400)
    else:
        return Response("Send JSON format", status=400)

    search_results = query_search(req)
    return jsonify(search_results)


# @app.route("/sponsor", methods=['GET'])
# def sponsor_api():
    # if request.args.get('id'):
        # sponsor_id = request.args.get('id')
    # sponsor_status = add_sponsor(sponsor_id)
    # return jsonify(sponsor_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
