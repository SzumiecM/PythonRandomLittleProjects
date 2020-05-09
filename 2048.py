from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

browser = webdriver.Chrome('C:/Webdrivers/chromedriver.exe')

browser.get('http://2048game.net')


def case(n, html):
    if n%4 == 0:
        html.send_keys(Keys.UP)
    elif n%4 == 1:
        html.send_keys(Keys.RIGHT)
    elif n%4 == 2:
        html.send_keys(Keys.DOWN)
    elif n%4 == 3:
        html.send_keys(Keys.LEFT)

n= 1
while True:
    try:
        x = browser.find_element_by_xpath("//script[@src='https://platform.twitter.com/js/button.dd024c345fc26f7c7a8d9938b67e5d3d.js']")
        time.sleep(2)
        browser.close()
        break;
    except:
        pass
    #n = random.randint(1,4)
    html = browser.find_element_by_tag_name('html')
    case(n, html)
    #time.sleep(0.05)
    n += 1




