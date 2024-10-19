from bs4 import BeautifulSoup as bs
import requests


class ParseNews:
    def __init__(self):
        self.url = "https://www.playground.ru/news?p={0}"

    async def get_news(self, news_num):
        print("news_num: ", news_num)
        page = news_num // 30 + 1
        print("page:", page)
        # news_num = stopped_on % 30
        
        content = requests.get(self.url.format(page)).content
        soup = bs(content, "html.parser")
        posts = soup.find_all("div", {"class": "post"})
        info = []
        for post in posts:
            img = post.find("img")
            datetime = post.find("time").text
            news_url = post.find("div", {"class": "post-title"}).find("a").get("href")
            info.append(
                {
                    "datetime": datetime,
                    "img": img.get("src"),
                    "caption": img.get("alt"),
                    "url": news_url
                }
            )

        return info
