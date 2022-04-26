from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

chrome_driver_path = Service(r"C:\Users\Lenovo\Desktop\atom folder\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.python.org/")
question = driver.find_element(By.NAME, "q")

print(question.get_attribute("placeholder"))

python_logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(python_logo)
print(python_logo.size)

doc_link = driver.find_element(by=By.CSS_SELECTOR, value= ".documentation-widget a")
print(doc_link)

upcoming_event = driver.find_element(by=By.CSS_SELECTOR, value=".event-widget").text
print(upcoming_event)


driver.quit()

url = requests.get("https://www.python.org/").text
soup = BeautifulSoup(url, "html.parser")

events = soup.select(selector="h2 .widget-title")
print(events)

for element in events:
    print(element.get_text())

''' 
chrome_driver_path = Service(r"C:\Users\Lenovo\Desktop\atom folder\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

title = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(title.text)

title.click()

all_portals = driver.find_element_by_link_text("Elon Musk")
all_portals.click()


search = driver.find_element(by=By.NAME, value="search")
search.send_keys(" linear regression")
search.send_keys(Keys.ENTER)
'''


'''' 
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.CLASS_NAME, value="top")
first_name.send_keys("nuri")

last_name = driver.find_element(by=By.CLASS_NAME, value="middle")
last_name.send_keys("tas")

mail = driver.find_element(by=By.CLASS_NAME, value="bottom")
mail.send_keys("fsfs@fsdfs")
mail.send_keys(Keys.ENTER)

'''

''' 
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

for i in range(21312321):
    cookie.click()

print(cookie)

'''