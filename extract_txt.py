import requests
import pandas as pd
import numpy as np
import json

corpus = []
final_file_name = 'arisbotle_data.txt'
txt_list = 'txt_list.json'

def open_json_url_list(json_url_list):
    list_url = []
    with open(json_url_list) as aristotle_texts:
        list_url.append(json.load(aristotle_texts))
    return list_url[0]

def return_corpus_text(url_data):
    first_section = return_first_split(url_data)
    last_section = return_last_split(url_data, first_section)
    return last_section

def return_first_split(url_data):
    test_get = requests.get(url_data['url'])
    url_full_text = json.dumps(test_get.text)
    first_split = url_full_text.split(url_data['first_split'])
    first_clean = first_split[1:]
    return "".join(first_clean)

def return_last_split(url_data, first_clean):
    last_split = first_clean.split(url_data['last_split'])
    final_clean = last_split[:-1]
    final_clean = "".join(final_clean)
    final_clean = final_clean.replace("\\r\\n\\r\\n","") \
            .replace("\\r","") \
            .replace("\\n","") \
            .replace("\\","")
    return final_clean

list_url = open_json_url_list(txt_list)
corpus = [return_corpus_text(url_data) for url_data in list_url]

with open(final_file_name, 'w') as outfile:  
    json.dump(corpus, outfile)