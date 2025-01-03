# Write your code here :-)
import requests
from bs4 import BeautifulSoup

search_query = 'cats'
url = f'https://imgur.com/{search_query}'

res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.find_all('img')

    image_urls = [img['src']for img in img_tags]

    for i, img_url in enumerate(image_urls, start = 1):
        print(f'image{i}: {img_url}')

else:
    print('Failed to retrieve data from the website')
