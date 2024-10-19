from bs4 import BeautifulSoup as bs
import requests
import psycopg2


def start_parse():
    url = "https://www.playground.ru/news?p={0}"

    content = requests.get(url.format(1)).content

    #  всего помещается 30 новостей

    soup = bs(content, "html.parser")
    posts = soup.find_all("div", {"class": "post"})
    for i, post in enumerate(posts):
        print(post.find("img"))

if __name__ == '__main__':
    start_parse()
