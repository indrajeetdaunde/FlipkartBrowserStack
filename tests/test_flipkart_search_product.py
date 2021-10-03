import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from BrowserStackTest.PageObjects.FlipkartHomePage import FlipkartHomePage
from BrowserStackTest.TestData.FlipkartHomePageData import FlipkartHomePageData
from BrowserStackTest.utility.BaseClass import BaseClass


class TestFlipkartSearchProduct(BaseClass):

    def test_flipkart_search_product(self, get_data):
        log = self.get_logger()
        flipkart_home_page = FlipkartHomePage(self.driver)
        log.info("Close Signup Pop up")
        flipkart_home_page.click_close_signup_button().click()
        flipkart_home_page.get_search_product_str().send_keys(get_data["search_product"])
        product_list_page = flipkart_home_page.click_search_product_button()
        self.verify_link_presence("div[class='_5THWM1'] span")
        list_of_menus = product_list_page.get_list_of_menus()

        i = -1
        for menu_brand in list_of_menus:
            i = i + 1
            brand_menu_name = menu_brand.text
            if brand_menu_name == 'BRAND\nSAMSUNG':
                product_list_page.get_list_of_menus()[i].click()
                break

        self.verify_link_presence("div[class='_5THWM1'] span")

        j = -1
        for menu_assured in list_of_menus:
            j = j + 1
            assured_menu_name = menu_assured.text
            if assured_menu_name == '?':
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='_1KOcBL']/section[3]"))))
                break

        sorting_options = product_list_page.get_list_sorting_options()
        k = -1
        for sorting_option in sorting_options:
            k = k + 1
            sort_option = sorting_option.text
            if sort_option == 'Price -- High to Low':
                self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='_5THWM1']/div[4]"))))
                break

        self.verify_link_presence("div[class='_5THWM1'] span")
        list_of_products = product_list_page.get_list_of_products()
        product_list = []
        price_list = []
        product_link = []
        product_dict = {}
        productlist = []
        print(len(list_of_products))
        for m in range(0, 24):
            m = m + 1
            product_name = product_list_page.get_list_of_products()[m]
            try:
                p_name = product_name.find_element_by_xpath("div/div/div/a/div[2]/div/div[1]").text
                product_list.append(p_name)
                p_price = product_name.find_element_by_xpath("div/div/div/a/div[2]/div[2]/div[1]/div/div").text
                price_list.append(p_price)
                p_link = product_name.find_element_by_xpath("div/div/div/a").get_attribute('href')
                product_link.append(p_link)
                product_dict["Product"] = p_name
                product_dict["Price"] = p_price
                product_dict["Link"] = p_link
                productlist.append(product_dict["Product"])
                productlist.append(product_dict["Price"])
                productlist.append(product_dict["Link"])
            except StaleElementReferenceException as Exception:
                print("StaleElementReferenceException while getting the text")
                p_name = product_name.find_element_by_xpath("div/div/div/a/div[2]/div/div[1]").text
                product_list.append(p_name)
                p_price = product_name.find_element_by_xpath("div/div/div/a/div[2]/div[2]/div[1]/div/div").text
                price_list.append(p_price)
                p_link = product_name.find_element_by_xpath("div/div/div/a").get_attribute('href')
                product_link.append(p_link)
                product_dict["Product"] = p_name
                product_dict["Price"] = p_price
                product_dict["Link"] = p_link
                productlist.append(product_dict["Product"])
                productlist.append(product_dict["Price"])
                productlist.append(product_dict["Link"])
            if m == 24:
                break
        print(product_list)
        print(len(product_list))
        print(price_list)
        print(len(product_list))
        print(product_link)
        print(len(product_link))
        print(product_dict)
        print(productlist)

    @pytest.fixture(params=FlipkartHomePageData.flipkart_homepage_data)
    def get_data(self, request):
        return request.param
