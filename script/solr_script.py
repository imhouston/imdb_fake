import pandas as pd

some_list = list()

with open('MYMOVIE.csv', encoding="utf-8") as file:
    for line in file:
        line_text = line[:-1]

        if len(line_text.split('\t')) == 10:
            some_list.append(line_text.split('\t'))


df = pd.DataFrame(some_list)

headers = df.iloc[0]
df = pd.DataFrame(df.values[1:], columns=headers)

def string_to_list(text: str):
    text = str(text)
    text.strip()
    text = text.replace("{", "")
    text = text.replace("}", "")
    text = text.replace("'", "")
    text = text.replace('"', '')
    my_list = text.split(',')
    return my_list

def storyline_strip(text: str):
    return text.strip('"').strip()

df.release_dates = df.release_dates.apply(string_to_list)
df.genres = df.genres.apply(string_to_list)
df.directors = df.directors.apply(string_to_list)
df.top_3_cast = df.top_3_cast.apply(string_to_list)

df.astype(str)
df.storyline = df.storyline.apply(storyline_strip)

import requests
url = 'http://localhost:8983/solr/imdb_core/update/json/docs?commit=true'
payload = df.to_json(orient='records')
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)
print(r.text)
