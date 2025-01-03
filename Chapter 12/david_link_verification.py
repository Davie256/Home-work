import requests, webbrowser
from bs4 import BeautifulSoup

def get_links_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            links.append(href)
    return links

def download_and_open_links(links):
    for link in links:

        try:
            res = requests.get(link)

            if res.status_code == 200:
                #with open('temp_page.html', 'wb') as f:
                #    f.write(res.content)

                webbrowser.open(link)

            else:
                 print(f'\nBroken Link = "{link}"')

        except:
            print(f'Error occured when opening this link: "{link}"')

def main():
    user_site = input('Enter your website page: ie "example.com"\n')
    url = 'https://' + str(user_site)
    links = get_links_from_url(url)
    download_and_open_links(links)

main()
