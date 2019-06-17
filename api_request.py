import requests
from typing import List

HOST = ""


def query_search(query_text: str, search_priority: dict, field_priority: bool, group_by: dict) -> List[dict]:
    # query_string = "http://" + HOST + "/movies/"
    res = requests.get(query_string)
    query_result = res.json()

    return query_result


def add_sponsor_movie(id: str):
    # query = "http://" + HOST

    # Get answer?
    pass
