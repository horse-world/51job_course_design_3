import requests
from varible import format_url, HEADER, format_write, SAVEFILE_PATH
from bs4 import BeautifulSoup
import json
import threading
import time
import os


def fragment(start, stop, file):
    for j in range(start, stop + 1, 1):
        try:
            response = requests.get(url=format_url(page=j), headers=HEADER)
            while response.status_code != 200:
                response = requests.get(url=format_url(page=j), headers=HEADER)
        except requests.exceptions.Timeout:
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


start_time = time.localtime()
for number in range(0, 101, 1):
    threading.Thread(target=fragment, args=(
        number * 20, number * 20 + 19,
        open(file=SAVEFILE_PATH + "51job_data2{}.csv".format(number), mode="w", encoding="utf-8"))
                     ).start()

while len(threading.enumerate()) != 1:
    pass

print(start_time)
print(time.localtime())
# 22.44.37-22.46.58

# 合并文件
file3 = open("../data/final_51job_data3.csv", mode="w", encoding="utf-8")
for number in range(0, 101, 1):
    file2 = open(file=SAVEFILE_PATH + "51job_data2{}.csv".format(number), mode="r", encoding="utf-8")
    file3.write(file2.read())
    file2.close()
    os.remove(SAVEFILE_PATH + "51job_data2{}.csv".format(number))
file3.close()
