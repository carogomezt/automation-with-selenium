import unittest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchVersion(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.headless = True
        options.set_preference('dom.webnotifications.enabled', False)
        self.driver = webdriver.Firefox(options=options)

    def search_page(self):
        self.driver.get('https://www.google.com/')
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('Selenium pip')
        search_field.submit()
        result_xpath = '//div[1]/a[1]/div/cite'
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, result_xpath)))
        page_url = self.driver.find_element_by_xpath(result_xpath)
        return page_url

    def test_search_by_text(self):
        page_url = self.search_page()
        page_url_text = page_url.text
        time.sleep(3)
        self.assertEqual(page_url_text, 'https://pypi.org/project/selenium/')

    def test_selenium_last_release(self):
        page_url = self.search_page()
        page_url.click()
        package_name = self.driver.find_element_by_class_name(
            '-js-relative-time')
        package_version = package_name.text
        time.sleep(3)
        self.assertIn('2019', package_version)

    def test_selenium_version(self):
        page_url = self.search_page()
        page_url.click()
        package_name = self.driver.find_element_by_class_name(
            'package-header__name')
        curr_time = str(time.time()).split('.')[0]
        file_name = 'selenium-version{date}.png'.format(date=curr_time)
        self.driver.save_screenshot(file_name)
        package_version = package_name.text.split(' ')[1]
        time.sleep(3)
        self.assertEqual(package_version, '3.141.0')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
