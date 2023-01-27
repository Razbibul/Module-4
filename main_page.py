from base_page import BasePage
from selenium.webdriver.common.by import By



class MainPage(BasePage): # Таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка..
    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()