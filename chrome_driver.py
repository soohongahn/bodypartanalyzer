from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By

s = Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/imghp?hl=en&authuser=0ogbl")
elem = driver.find_element(By.NAME, "q")

search = "knee"

elem.send_keys(search)
elem.send_keys(Keys.RETURN)

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
bodyPart = "Knee"

count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")
        imageName = bodyPart + "_" + str(count) + ".jpg"
        urllib.request.urlretrieve(imgUrl, "./" + bodyPart + "/" + imageName)
        count += 1
    except:
        pass

driver.close()