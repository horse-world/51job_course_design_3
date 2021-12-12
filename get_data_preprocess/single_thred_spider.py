import json
from varible import format_url, HEADER, format_write, SAVEFILE_PATH
import requests
from bs4 import BeautifulSoup

file = open(file=SAVEFILE_PATH + "51job_data.csv", mode="w", encoding="utf-8")

for j in range(1, 2001, 1):
    response = requests.get(url=format_url(page=j), headers=HEADER)
    while response.status_code != 200:
        response = requests.get(url=format_url(page=j), headers=HEADER)

    html_tree = BeautifulSoup(response.text, "html.parser")
    list_info = html_tree.select("div[id='app'] + script")
    dict_info = json.loads(list_info[0].text[len("  window.__SEARCH_RESULT__ = "):])
    for i in dict_info["engine_search_result"]:
        file.write(format_write(i=i))
    print("spider {} page over.".format(j))

file.close()
