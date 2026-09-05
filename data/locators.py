from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
