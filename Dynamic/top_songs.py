from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fetch_top_songs():
    driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF")

    time.sleep(10) 
    songs = []
    rows = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tracklist-row']")
    for row in rows:
        try:
            title = row.find_element(By.CSS_SELECTOR, "a").text
        except:
            title = "N/A"

        try:
            artist = row.find_elements(By.CSS_SELECTOR, "a")[1].text
        except:
            artist = "N/A"

        songs.append({
            "title": title,
            "artist": artist
        })
    driver.quit()
    return songs