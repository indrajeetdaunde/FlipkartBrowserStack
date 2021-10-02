from selenium.webdriver.common.by import By

from BrowserStackTest.PageObjects.ProductListPage import ProductListPage


class FlipkartHomePage:

    signup_close_button = (By.CSS_SELECTOR, "button[class='_2KpZ6l _2doB4z']")
    search_product_textbox = (By.XPATH, "//input[@name='q']")
    search_product_button = (By.CSS_SELECTOR, "button[type='submit'] svg")

    def __init__(self, driver):
        self.driver = driver

    def click_close_signup_button(self):
        return self.driver.find_element(*FlipkartHomePage.signup_close_button)

    def get_search_product_str(self):
        return self.driver.find_element(*FlipkartHomePage.search_product_textbox)

    def click_search_product_button(self):
        self.driver.find_element(*FlipkartHomePage.search_product_button).click()
        product_list_page = ProductListPage(self.driver)
        return product_list_page
