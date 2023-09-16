
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
def get_data(url):
    options = webdriver.ChromeOptions()
    try:
        driver = webdriver.Chrome(options=options)

        driver.maximize_window()
        driver.get(url=url)
        time.sleep(5)
        try:

            cookie_button = driver.find_element(By.XPATH,"/html/body/div[7]/div/div/mat-dialog-container/mts-accept-cookies-popup/div/div/div[2]/button")
            cookie_button.click()
            time.sleep(1)

        except NoSuchElementException:
            pass


        driver.execute_script('window.scrollBy(0, 100)')
        time.sleep(1)


        driver.find_element(By.CSS_SELECTOR, "body > div.g-page-wrapper > div > div.mts16-footer__to-bottom-content > div.content__wrap > mts-tariffs-catalog > div.tabs.tabs_relative.tabs_combined > div > div > div > mts-actual-tariffs-catalog > div > div.filters__content.filters__content-full-width > mts-actual-tariffs > div.filters__content-item > mts-actual-tariffs-group > div > button").click()
        time.sleep(5)

        with open('../parser_MTS/data/index.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
