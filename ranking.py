#pip install beautifulsoup4 jupyter urllib3 selenium
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

URL = "https://www.youtube.com/feed/trending"
YOUTUBE_URL = "https://www.youtube.com"
options = Options()
options.set_headless(True)
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
html = driver.page_source.encode('utf-8')

soup = BeautifulSoup(html, "html.parser")

for i, content in enumerate(soup.select_one("#dismissable").find_all("ytd-video-renderer")):
  video_title = content.select_one("#video-title").get_text().strip()
  channel_name = content.select_one("#text > a").get_text().strip()
  play_count = content.select_one("#metadata-line > span:nth-child(1)").get_text().strip()
  post_date = content.select_one("#metadata-line > span:nth-child(2)").get_text().strip()
  image_url = content.select_one("#img").get('src')
  video_path = content.select_one("#video-title").get('href')

  print('%d位' % (i+1))
  print(video_title)
  print(channel_name)
  print(play_count)
  print(post_date)
  print(image_url)
  print(YOUTUBE_URL+video_path)
  print("------------------")