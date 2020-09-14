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

# for i, content in enumerate(soup.select_one("#dismissable").find_all("ytd-video-renderer")):

# soup.find("div", {"id": "SearchResultsListings"})
# searchResultsListings = soup.select_one("#SearchResultsListings")
# for (i,content) in enumerate(searchResultsListings.find_all("grid__item")):
#   print(content.text)
# div1 = soup.select_one("#SearchResultsListings > div.grid__item")
# print(div1.text)
print("*****")
print(soup.find("div", {"id": "SearchResultsListings"}).find_all("div", {"class": "grid__item"})[0].text )
print("---------")
for i, content in enumerate(soup.find("div", {"id": "SearchResultsListings"}).find_all("div", {"class": "grid__item"})):
  # print(content)
  app_title = content.find("h4", {"class": "ui-app-card__name"}).text
  print("apptitle:",app_title)
  # /html/body/div[5]/main/section[2]/div/div[2]/div[2]/div[1]
  # //*[@id="SearchResultsListings"]/div[1]

# for i, content in enumerate(soup.select_one("#dismissable").find_all("ytd-video-renderer")):
#   video_title = content.select_one("#video-title").get_text().strip()
#   channel_name = content.select_one("#text > a").get_text().strip()
#   play_count = content.select_one("#metadata-line > span:nth-child(1)").get_text().strip()
#   post_date = content.select_one("#metadata-line > span:nth-child(2)").get_text().strip()
#   image_url = content.select_one("#img").get('src')
#   video_path = content.select_one("#video-title").get('href')

#   print('%d位' % (i+1))
#   print(video_title)
#   print(channel_name)
#   print(play_count)
#   print(post_date)
#   print(image_url)
#   print(YOUTUBE_URL+video_path)
#   print("------------------")


driver.close()
driver.quit()