from selenium import webdriver

browser1 = webdriver.Chrome('C:/Webdrivers/chromedriver.exe')
browser1.set_window_position(5, 0)
browser1.set_window_size(500, 1500)
browser2 = webdriver.Chrome('C:/Webdrivers/chromedriver.exe')
browser2.set_window_position(520, 0)
browser2.set_window_size(500, 1500)
browser1.get('https://www.cleverbot.com')
browser2.get('https://www.cleverbot.com')

firstin = browser1.find_element_by_name('stimulus')
firstin.send_keys('hi')
firstin.submit()

counter= 2
while True:
    if counter == 1:
        line2= browser2.find_element_by_id('line1')
        if str(line2.text).endswith('.') or str(line2.text).endswith('?') or str(line2.text).endswith('!'):
            in1= browser1.find_element_by_name('stimulus')
            in1.send_keys(line2.text)
            in1.submit()
            counter= 2

    elif counter == 2:
        line1= browser1.find_element_by_id('line1')
        if str(line1.text).endswith('.') or str(line1.text).endswith('?') or str(line1.text).endswith('!'):
            in2= browser2.find_element_by_name('stimulus')
            in2.send_keys(line1.text)
            in2.submit()
            counter= 1
