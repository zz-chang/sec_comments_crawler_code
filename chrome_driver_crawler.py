import csv
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

# 进行设置
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path='../chromedriver', options=option)

with open('./stealth.min.js') as f:
    js = f.read()

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

# 手动登录
offical_url = 'https://seekingalpha.com/'
browser.get(offical_url)
time.sleep(60)

# 开始采集
c = 0
with open('./article_list_all_history.csv', 'r', encoding='utf-8-sig', errors='ignore') as f:
    reader = csv.reader(f)
    for line in reader:
        c += 1
        if c <= 124199:
            # print(line, len(line))
            continue

        if c > 125000:  # end = 98462
            break
        # print(line[8])
        aid = line[8].split('-')[0].split('/')[-1]
        print(c, "~~~~~~~~~~", aid)

        url = "https://seekingalpha.com/api/v3" + line[8].split('-')[0].replace('article', 'articles')
        print(url)

        fname = "./sa_news_data_mac/js_news_" + str(aid) + ".json"
        f = open(fname, 'w', encoding='utf-8')
        while True:
            browser.get(url)
            time.sleep(2)
            content = browser.find_element('xpath', './/body').get_attribute('innerText')
            if 'data' in content:
                f.writelines(content)
                f.close()
            else:
                print(url, content)
                time.sleep(200)
                continue
            break

        time.sleep(2 + random.random() * 2)
