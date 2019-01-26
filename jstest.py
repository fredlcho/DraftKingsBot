# from requests_html import HTMLSession
# session = HTMLSession()
# r = session.get('https://www.draftkings.com/draft/contest/68293899')
# r.html.render()
# page = r.html.find(selector='.Tab_tab')
# for x in page:
#     if x.text == "ALL":
#         print(x.text)


from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("https://www.draftkings.com/draft/contest/68293899")
button = browser.find_element_by_xpath("//*[contains(text(),'ALL')]")
button.click()

time.sleep(20)
page = browser.page_source
#time.sleep(20)
listss = browser.find_elements_by_css_selector('.PlayerNameCell_player-name-cell-text')
for x in listss:
    print(x.text)
print(len(listss))
