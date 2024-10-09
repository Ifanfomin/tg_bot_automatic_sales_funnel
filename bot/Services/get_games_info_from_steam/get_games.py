from bs4 import BeautifulSoup as bs
import requests
import psycopg2
from config import config



def start_parse():
    names = [
        "Рогалики",
        "Стратегии",
        "Головоломки",
        "Кооперативные"
    ]

    game_info = {
        "image": "",
        "name": "",
        "developer": "",
        "price": "",
        "genre": "",
        "date": "",
        "alone": "",
        "koop": "",
        "description": "",
        "sysreq": "",
        "popularity": 0,
    }

    conn = psycopg2.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME
    )
    cursor = conn.cursor()

    for name in names:
        with open(name + ".html", "r") as file:
            soup = bs(file.read(), "html.parser")
            games = soup.find_all("div", {"class": "_3rrH9dPdtHVRMzAEw82AId"})
            for game in games:
                url = game.find("a").get("href")
                data = requests.get(url)
                soup = bs(data.text, "html.parser")
                print(game)
                print(soup.find("img", {"class": "game_header_image_full"}).get("src"))
                game_info["image"] = soup.find("img", {"class": "game_header_image_full"}).get("src")
                game_info["name"] = soup.find("div", {"id": "appHubAppName"}).text
                game_info["developer"] = ", ".join([a.text for a in soup.find("div", {"id": "developers_list"}).find_all("a")])
                if "game_purchase_price" in data.text:
                    game_info["price"] = "".join(soup.find("div", {"class": "game_purchase_price"}).text.split())
                else:
                    game_info["price"] = "Нет в продаже"
                game_info["genre"] = name
                game_info["date"] = soup.find("div", {"class": "date"}).text
                game_info["alone"] = "есть" if "Single-player" in [div.text for div in soup.find("div", {"class": "game_area_features_list_ctn"}).find_all("div", {"class": "label"})] else "нет"
                game_info["koop"] = "есть" if any([koop_type in [div.text for div in soup.find("div", {"class": "game_area_features_list_ctn"}).find_all("div", {"class": "label"})] for koop_type in ["Online Co-op", "Shared/Split Screen Co-op", "Online PvP", "Online Co-op"]]) else "нет"
                game_info["description"] = " ".join(soup.find("div", {"id": "game_area_description"}).text.split(".")[0].split())
                if "game_area_sys_req_leftCol" in data.text:
                    game_info["sysreq"] = soup.find("div", {"class": "game_area_sys_req_leftCol"}).find("ul", {"class": "bb_ul"}).text
                else:
                    try:
                        game_info["sysreq"] = soup.find("div", {"class": "game_area_sys_req_full"}).find("ul", {"class": "bb_ul"}).text
                    except:
                        game_info["sysreq"] = soup.find("div", {"class": "game_area_sys_req_full"}).find("p").text
                # print(soup.find_all("div", {"class": "user_reviews_summary_row"})[1].find("span", {"class": "responsive_hidden"}).text)
                game_info["popularity"] = int("".join(soup.find_all("div", {"class": "user_reviews_summary_row"})[1].find("span", {"class": "responsive_hidden"}).text.split("(")[-1].split(")")[0].split(",")))

                print(game_info)

                cursor.execute(
                    "INSERT INTO games (image, name, developer, price, genre, date, alone, koop, description, sysreq, popularity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(game_info.values()))
                conn.commit()


if __name__ == '__main__':
    start_parse()