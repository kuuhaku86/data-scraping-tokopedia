from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Scraper:
  def __init__(self):
    self.driver = webdriver.Firefox()

  def get_data(self):
    self.driver.get('https://www.tokopedia.com/search?navsource=&ob=5&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&q=sepatu')
    
    counter_page = 0
    datas = []

    while counter_page < 10:
      for _ in range(0, 6500, 500):
        time.sleep(0.1)
        self.driver.execute_script("window.scrollBy(0,500)")

      elements = self.driver.find_elements(by=By.CLASS_NAME, value='css-y5gcsw')
      for element in elements:
        img = element.find_element(by=By.CLASS_NAME, value='css-1c345mg').get_attribute('src')
        name = element.find_element(by=By.CLASS_NAME, value='css-1b6t4dn').text
        price = element.find_element(by=By.CLASS_NAME, value='css-1ksb19c').text
        city = element.find_element(by=By.CLASS_NAME, value='css-1kdc32b').text

        datas.append({
          'img': img,
          'name': name,
          'price': price,
          'city': city
        })

      counter_page += 1
      next_page = self.driver.find_element(by=By.XPATH, value="//button[@class='css-1ix4b60-unf-pagination-item' and text()='" + str(counter_page + 1) + "']")
      next_page.click()
    
    return datas