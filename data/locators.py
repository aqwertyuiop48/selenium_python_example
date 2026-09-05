from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
