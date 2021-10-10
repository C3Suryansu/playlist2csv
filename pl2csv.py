from bs4 import BeautifulSoup
import requests
import pytube
from datetime import datetime
import pandas as pd

data = {}
titles = []
links = []
times = []
url = input("Enter youtube playlist link : ")
x = pytube.contrib.playlist.Playlist(url)
for link in x.url_generator():
    s = BeautifulSoup(requests.get(link).text, "html.parser")
    title = s.find("title").text
    titles.append(title)
    links.append(link)
    times.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
data = {'sl.no': [i for i in range(len(titles))],
        'title' : titles, 
        'link': links,
        'datetime': times}
csv_name = x.title
df = pd.DataFrame.from_dict(data)
df.to_csv(f'{csv_name}.csv', index = False)