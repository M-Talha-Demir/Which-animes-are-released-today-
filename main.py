from bs4 import BeautifulSoup
from selenium import webdriver
import time
from tools import url_2_soup, word_2_digit, find_ep, crop_ep

url = 'https://www.turkanime.co/'
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
html = BeautifulSoup(driver.page_source, 'lxml')
animeList = html.find("div", {"id": "orta-icerik"})
count = 0
print("Animes on the Home Page are;")
for anime in animeList:
    if type(anime) is not None:
        if not anime.find_all("div",{"class":"panel-title"}) == []:
            name_of_anime = anime.find_all("div",{"class":"panel-title"})[0].a.get("data-original-title")
            link_of_anime = anime.div.a.get("href")
            time_of_anime = anime.find_all("span", {"class": "media-object", "style":"margin-top:5px;"})[1].text
            num, time_type = word_2_digit(time_of_anime)
            episode, i_ep = find_ep(name_of_anime)
            name_of_anime = crop_ep(name_of_anime, i_ep)
            print(f"{str(count).ljust(5)} Name of Anime: {name_of_anime.ljust(110)} This anime was uploaded {num} {time_type} ago. Episode: {episode}")
            count += 1
    else:
        pass

print("\n \nThe anime that will be broadcast today are;")
count = 0

url = 'https://www.turkanime.co/takvim'
driver.get(url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
html = BeautifulSoup(driver.page_source, 'lxml')
animeList = html.find("div",{"class":"list-group takvimList"})

for anime in animeList:
    if type(anime) is not None:
        if not anime.find_all("h4",{"class":"list-group-item-heading"}) == []:
            # print(anime.find_all("div",{"class":"panel-title"})[0].a.get("data-original-title"))
            name_of_anime = anime.find_all("h4",{"class":"list-group-item-heading"})[0].text
            link_of_anime = anime.get("href")
            print(f"{str(count).ljust(5)} Name of Anime: {name_of_anime.ljust(110)}")
            count += 1
    else:
        pass

driver.quit()
