from bs4 import BeautifulSoup
import requests, csv

URL = 'https://hpk.edu.ua/replacements'
r = requests.get(URL)

with open(r"Parser v1.0/index.html", encoding='utf-8') as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title.text + "\n")

page_p = soup.find_all("p")
for item in page_p:  # Перебирає всі елементи р
    print(item.text)

user_name = soup.find("div", class_="main").find(
    "h1")  # Пошук по тегам і класам в тегах
print('\n' + user_name.text)
