from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Cache (stores results after first scrape)
_movies_cache = None


def fetch_top_movies():
    global _movies_cache

    # Return cached data if available
    if _movies_cache is not None:
        return _movies_cache

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.imdb.com/chart/top/")

        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
            )
        )

        movie_cards = driver.find_elements(
            By.CSS_SELECTOR,
            "li.ipc-metadata-list-summary-item"
        )

        movies = []

        for movie in movie_cards:

            title = movie.find_element(
                By.CSS_SELECTOR,
                "h4.ipc-title__text"
            ).text

            rating = movie.find_element(
                By.CLASS_NAME,
                "ipc-rating-star--rating"
            ).text

            details = movie.find_elements(
                By.CLASS_NAME,
                "ipc-inline-list__item"
            )

            texts = [d.text for d in details]

            year = texts[0] if len(texts) > 0 else "N/A"
            runtime = texts[1] if len(texts) > 1 else "N/A"
            certificate = texts[2] if len(texts) > 2 else "N/A"

            try:
                poster = movie.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                poster = ""

            movies.append({
                "title": title,
                "rating": rating,
                "year": year,
                "runtime": runtime,
                "certificate": certificate,
                "poster": poster
            })

        _movies_cache = movies
        return movies

    finally:
        driver.quit()