# -*- coding: utf-8 -*-
"""
Script that uses Selenium to automate the post on facebook groups
"""
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver_initialize(url):
    """
    Starts a Firefox driver in the defined URL in headless mode

    :param url: URL to load once the driver starts
    """
    options = Options()
    # options.headless = True
    options.set_preference('dom.webnotifications.enabled', False)
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    return driver


def login_fb(driver, user, password):
    """
    Login into a facebook account

    :param driver: Selenium object that contains the session information
    :param user: Facebook username
    :param password: Facebook password
    """
    print('Logging on Facebook')
    elem = driver.find_element_by_id('email')
    elem.send_keys(user)
    elem = driver.find_element_by_id('pass')
    elem.send_keys(password)
    c = driver.find_element_by_id('loginbutton')
    c.click()


def post_fb_group(message, group_links):
    """
    Post into a facebook group

    :param message: Message to share in groups
    :param group_links: List of groups
    """
    user = os.environ['FB_USR']
    password = os.environ['FB_PWD']
    print('Open Facebook page')
    driver = driver_initialize('https://www.facebook.com/')
    login_fb(driver, user, password)
    for group in group_links:
        # Go to the Facebook Group
        driver.get(group)
        xpath = '//*[@name="xhpc_message_text"]'
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        post_box = driver.find_element_by_xpath(xpath)
        print('Enter the text we want to post to Facebook')
        post_box.send_keys(message)
        sleep(10)
        print('Get the "Post" button and click on it')
        submit_button_xpath = '//*[@data-testid="react-composer-post-button"]'
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
        post_button = driver.find_element_by_xpath(submit_button_xpath)
        post_button.click()
        print('Post published')
        sleep(5)
    driver.close()


if __name__ == '__main__':
    messagge = '📢Queremos contarte que estamos buscando ponentes para nuestras \
próximas charlas, si quieres compartir tus conocimientos con la comunidad de \
Python Pereira esta es tu oportunidad! 🐍💻 \
\nhttps://www.facebook.com/pythonpereira/posts/620993295010701'
    group_links = ['https://www.facebook.com/groups/pythonco/']
    post_fb_group(messagge, group_links)
