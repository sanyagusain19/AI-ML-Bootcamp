from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fetch_startups():
    driver = webdriver.Chrome()

    driver.get("https://techcrunch.com/category/startups/")
    time.sleep(5)

    titles = driver.find_elements(By.CSS_SELECTOR, "a.loop-card__title-link")
    authors = driver.find_elements(By.CSS_SELECTOR, "a.loop-card__author")

    startups = []

    for title, author in zip(titles, authors):
        startups.append({
            "title": title.text,
            "author": author.text
        })

    driver.quit()

    return startups