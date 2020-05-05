import requests


url = 'https://upload.wikimedia.org/wikipedia/en/0/00/The_Child_aka_Baby_Yoda_%28Star_Wars%29.jpg'
r = requests.get(url, allow_redirects=True)

open('anime.srt', 'wb').write(r.content)

