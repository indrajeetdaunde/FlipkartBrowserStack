import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='D:\\Personal\\Python Selenium\\drivers\\chrome\\chromedriver.exe')
driver.get('https://www.flipkart.com/')
driver.maximize_window()

driver.find_element_by_css_selector("button[class='_2KpZ6l _2doB4z']").click()
driver.find_element_by_css_selector("input[name='q']").send_keys("Samsung Galaxy S10")
driver.find_element_by_css_selector("button[type=submit] svg").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='_1AtVbE col-12-12']/div/div/section/div[1]")))

driver.find_element_by_xpath("//div[@class='_2q_g77']/section/div[3]").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='_1AtVbE col-12-12']/div/div/section/div[1]")))

driver.find_element_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/div/div/div/section[6]/div[2]/div/div/div/label/div[1]").click()

#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='_1AtVbE col-12-12']/div/div/section/div[1]")))
time.sleep(5)

driver.find_element_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/div/div/div/section[3]/label/div[2]").click()

sortBy = driver.find_elements_by_xpath("//div[@class='_5THWM1']")
for sort in sortBy:
    sortMenu = sort.find_element_by_xpath("div[4]").text
    print(sortMenu)
    if sortMenu == 'Price -- High to Low':
        sort.find_element_by_xpath("div[4]").click()

time.sleep(5)
searchProduct = driver.find_elements_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/div")

print(len(searchProduct))

products = []

for product in searchProduct:
    productName = driver.find_element_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/div[2]/div/div/div/a/div[2]/div[1]/div[1]").text
    print(productName)
    products.append(productName)

print(products)

driver.close()
