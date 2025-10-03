import requests
from bs4 import BeautifulSoup

web = requests.get("https://torob.com/browse/230/%D9%85%D8%A7%D9%86%DB%8C%D8%AA%D9%88%D8%B1-monitor/")
soup = BeautifulSoup(web.text , 'html.parser')

title = soup.title.string

items = soup.find_all("span", class_="ProductCard_desktop_card__SV3LG")
images = soup.find_all('img')

print("عنوان صفحه:", title)
print("عناوین:")
for item in items:
    print("*", item.text.strip())

print("لینک تصاویر:")
for img in images:
    print("+", img.get("src"))