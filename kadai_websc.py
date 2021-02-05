from bs4 import BeautifulSoup
import requests

url = "http://www.jma.go.jp/jp/yoho/319.html"
req = requests.get(url).text
soup = BeautifulSoup(req, "html.parser")

forecast_text = soup.find('pre', class_="textframe").text

print(forecast_text)

text = (forecast_text)

with open('test.txt' , 'w') as f:
    f.write(text)