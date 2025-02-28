# coding:utf-8
import random
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
from tqdm import tqdm

# 目标：通过chatGPT对政策文章摘要主要内容
# 阶段一：尝试阶段，使用100篇文章做摘要、存储检索


class Result:
    def __init__(self,query,answer):
        self.query=query
        self.answer=answer


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)

lines = []
with open("D:\\baiwang\\data\\pdfdata\\articles\\result.json", 'r', encoding='utf-8') as f:
    lines = f.readlines()

results = []

try:
    for i in tqdm(range(len(lines))):
        line = lines[i]
        body = json.loads(line)
        title = body['title']
        content = body['content']
        query = "提取下列内容中的政策名称和内容摘要：" + title + '. ' + content
        prompt_input = WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div/div[2]/form/div/div[2]/textarea')))
        prompt_input.clear()
        prompt_input.send_keys(query)
        # 发送按钮 /html/body/div[1]/div[1]/div[2]/div/main/div[2]/form/div/div[2]/button
        send_button = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[1]/div[2]/div/main/div/div[2]/form/div/div[2]/button')
        time.sleep(2)
        send_button.click()
        time.sleep(1)
        prompt_input.send_keys("让我想一下")
        time.sleep(60)
        prompt_input = WebDriverWait(driver, timeout=300).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div/div[2]/form/div/div[2]/button')))
# /html/body/div[1]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div/div/div[2]/div[1]/div
# /html/body/div[1]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[2]
        contents = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div/div/div[2]/div[1]/div')
        result = contents[-1].text
        print(result)
        results.append(json.dumps({'summary' : result, 'title' : title, 'content' : content}, ensure_ascii=False) + '\n')
except Exception as e:
    print(e)
finally:
    with open("G:\\baiwang\\code\\sd_coding\\pragram1_step1-1.json", 'w', encoding='utf-8') as f:
        f.writelines(results)
