from selenium.webdriver.common.by import By


class ProductListPage:

    sort_by_label = (By.XPATH, "//div[@class='_5THWM1']/span")
    list_of_menus = (By.XPATH, "//div[@class='_1KOcBL']/section")
    list_of_sorting_options = (By.XPATH, "//div[@class='_5THWM1']/div")
    list_of_products = (By.XPATH, "//div[@class='_1YokD2 _2GoDe3']/div[2]/div")

    def __init__(self, driver):
        self.driver = driver

    def get_sort_by_label(self):
        return self.driver.find_element(*ProductListPage.sort_by_label)

    def get_list_of_menus(self):
        return self.driver.find_elements(*ProductListPage.list_of_menus)

    def get_list_sorting_options(self):
        return self.driver.find_elements(*ProductListPage.list_of_sorting_options)

    def get_list_of_products(self):
        return self.driver.find_elements(*ProductListPage.list_of_products)
