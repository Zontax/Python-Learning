from bs4 import BeautifulSoup
import requests, csv

# with open(r"index.html", encoding='utf-8') as file:
#    src = file.read()
# print(src)

URL = 'https://hpk.edu.ua/replacements'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
soup = BeautifulSoup(requests.get(URL).text, 'lxml')
title = soup.title
print(title)

page_p = soup.find_all("strong")
for item in page_p:  # Перебирає всі елементи р
    print(item)

# user_name = soup.find("div", class_="news-body").find("p")  # Пошук по тегам і класам в тегах
# print('\n' + user_name.text)
