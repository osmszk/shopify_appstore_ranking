#pip install beautifulsoup4 jupyter urllib3 selenium
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

URL = "https://apps.shopify.com/browse/all?app_integration_kit=off&app_integration_pos=off&pricing=all&requirements=off&sort_by=installed"
# options = Options()
# options.set_headless(True)
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
html = driver.page_source.encode('utf-8')

soup = BeautifulSoup(html, "html.parser")

result = ''
for i, content in enumerate(soup.find("div", {"id": "SearchResultsListings"}).find_all("div", {"class": "grid__item"})):
  
  app_title = content.find("h4", {"class": "ui-app-card__name"}).text.replace(',', " ")
  discription = content.find("p", {"class": "ui-app-card__details"}).text.replace(',', " ")
  review_text = content.find("div", {"class": "ui-star-rating__text"}).text #3.3 of 5 stars(646reviews)
  review_rate = review_text[:3]
  review_count = review_text.split('(')[1].split('reviews')[0] #replace('reviews)', '')
  developer = content.find("div", {"class": "ui-app-card__developer-name"}).text[3:].replace(',', " ")
  print("apptitle:", app_title)
  print("discription:", discription)
  print("review:", review_rate, review_count)
  print("developer:", developer)
  result = result + "{0},{1},{2},{3},{4}".format(app_title,discription,developer,review_rate,review_count)
  result = result + '\n'
  print("-----------")

driver.close()
driver.quit()

with open("output.csv", "w") as text_file:
    print(result, file=text_file)