import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchVersion(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        options.set_preference('dom.webnotifications.enabled', False)
        self.driver = webdriver.Firefox(options=options)

    def test_search_by_text(self):
        self.driver.get('https://www.google.com/')
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.send_keys('Selenium pip')
        self.search_field.submit()
        result_xpath = '//div[1]/a[1]/div/cite'
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, result_xpath)))
        self.page_url = self.driver.find_element_by_xpath(result_xpath)
        page_url_text = self.page_url.text
        self.assertEqual(page_url_text, 'https://pypi.org/project/selenium/')

    def test_selenium_version(self):
        self.driver.get('https://www.google.com/')
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.send_keys('Selenium pip')
        self.search_field.submit()
        result_xpath = '//div[1]/a[1]/div/cite'
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, result_xpath)))
        self.page_url = self.driver.find_element_by_xpath(result_xpath)
        self.page_url.click()
        package_name = self.driver.find_element_by_class_name(
            'package-header__name')
        self.driver.save_screenshot('selenium-version.png')
        package_version = package_name.text.split(' ')[1]
        self.assertEqual(package_version, '3.141.0')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
