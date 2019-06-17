#!/usr/bin/env python

from flask import Flask, render_template, send_from_directory, url_for, redirect, request, jsonify
from api_request import query_search, add_sponsor_movie

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_index', methods=['POST'])
def search_index():
    some_results = query_search()
    pass
    return render_template('index.html', results=some_results)


@app.route('/show_result', methods=['POST'])
def show_movie_info():
    # some_movie - json with movie info
    some_movie = dict()
    pass

    return render_template('movie_info.html', movie=some_movie)


@app.route('/choose_sponsor', methods=['POST'])
def choose_sponsor():
    return render_template('sponsor.html')


@app.route('/search_sponsor', methods=['POST'])
def search_sponsor():
    # query_search()
    some_results = list()
    pass
    return render_template('sponsor.html', results=some_results)


@app.route('/add_sponsor', methods=['POST'])
def add_sponsor_button():
    # add_sponsor_movie()
    pass
    return


if __name__ == '__main__':
    app.run()
