import requests
import pandas as pd
import numpy as np
import json

corpus = []
final_file_name = 'arisbotle_data.txt'
txt_list = 'aris_test.json'

def open_json_url_list(json_url_list):
    with open(json_url_list) as aristotle_texts:
        list_url.append(json.load(aristotle_texts))
    return list_url[0]

list_url = open_json_url_list(txt_list)

for url_data in list_url:
    # get data from url
    url_title = url_data['title']
    test_get = requests.get(url_data['url'])
    url_full_text = json.dumps(test_get.text)
    first_split = url_full_text.split(url_data['first_split'])
    print(len(first_split))

    # take all data after first split
    first_clean = first_split[1:]
    first_clean = "".join(first_clean)
    last_split = first_clean.split(url_data['last_split'])
    print(len(last_split))

    # take all data but the last split
    final_clean = last_split[:-1]
    final_clean = "".join(final_clean)
    final_clean = final_clean.replace("\\r\\n\\r\\n","") \
            .replace("\\r","") \
            .replace("\\n","") \
            .replace("\\","")
    final_length = len(final_clean)

    # append data to corpus
    print(f"Length of {url_title}: {final_length}")
    corpus.append(final_clean)

with open(final_file_name, 'w') as outfile:  
    json.dump(corpus, outfile)

