from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fetch_disasters():

    driver = webdriver.Chrome()
    driver.get("https://www.gdacs.org/")

    time.sleep(8) 
    disasters = []
    titles = driver.find_elements(By.CSS_SELECTOR, "div.alert_box_title")

    for title in titles:

        try:
            event_type = title.text.strip()
        except:
            event_type = "N/A"

        try:
            parent = title.find_element(By.XPATH, "./following::span[1]")
            location = parent.text
        except:
            location = "N/A"

        try:
            date = title.find_element(By.XPATH, "./following::span[contains(@class,'alert_date')]").text
        except:
            date = "N/A"

        try:
            magnitude = title.find_element(By.XPATH, "./following::span[contains(@class,'magnitude')]").text
        except:
            magnitude = "N/A"

        disasters.append({
            "event": event_type,
            "location": location,
            "date": date,
            "magnitude": magnitude
        })

    driver.quit()
    return disasters