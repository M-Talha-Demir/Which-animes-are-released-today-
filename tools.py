import requests
from bs4 import BeautifulSoup


def url_2_soup(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    return soup


def word_2_digit(word):
    numbers = "0123456789"
    number = 0
    last = 0
    c = -1
    for w in word:
        c += 1
        if w in numbers:
            number = number*10 + int(w)
            last = c
    time = ' '
    if len(word) > last+1:
        time = word[last+2]
    if time == 's':
        return number, "hour"
    elif time == 'g':
        return number, "day"
    elif time == 's':
        return number, "minute"
    else:
        return number


def find_ep(a):
    if ". Bölüm" in a:
        index = a.index(". Bölüm")
        word = a[index - 3:index]
        ep = word_2_digit(word)
        index_ep = a.index(str(ep))
        return ep, index_ep
    else:
        return "", 0


def crop_ep(a,i_ep):
    if not i_ep==0:
        a = a[0:i_ep]
        return a.split("izle")[0]
    else:
        return a.split("izle")[0]
