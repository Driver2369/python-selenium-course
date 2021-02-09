from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # 2) wait until price is $100 or lower
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

    # 3) click on Book
    browser.find_element_by_id("book").click()



    # 4) read x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print(x)

    # 3) calculate y
    y = calc(x)

    # 4) put answer as y
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    # 5) click on Submit

    button = browser.find_element_by_("solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()