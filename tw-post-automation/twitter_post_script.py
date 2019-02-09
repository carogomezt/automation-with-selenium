# -*- coding: utf-8 -*-
"""
Script that uses Selenium to automate the post on twitter
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


def login_tw(driver, user, password):
    """
    Login into a twitter account

    :param driver: Selenium object that contains the session information
    :param user: Twitter username
    :param password: Twitter password
    """
    print('Logging on Twitter')
    login_button = driver.find_element_by_link_text('Log in')
    login_button.click()
    elem = driver.find_element_by_class_name('js-username-field')
    elem.send_keys(user)
    elem = driver.find_element_by_class_name('js-password-field')
    elem.send_keys(password)
    c = driver.find_element_by_xpath('//form/div[2]/button')
    c.click()


def post_twitter(message):
    """
    Post into a twitter account

    :param message: Message to post on twitter
    """
    user = os.environ['TW_USR']
    password = os.environ['TW_PWD']
    print('Open Facebook page')
    driver = driver_initialize('https://www.twitter.com')
    login_tw(driver, user, password)
    print('Enter the text we want to post to Twitter')
    post_box = driver.find_element_by_id('tweet-box-home-timeline')
    post_box.send_keys(message)
    submit_button_xpath = '//form/div[3]/div[2]/button'
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
    post_button = driver.find_element_by_xpath(submit_button_xpath)
    post_button.click()
    sleep(5)
    print('Post published')
    driver.close()


if __name__ == '__main__':
    messagge = 'This is a post with selenium 🙃'
    post_twitter(messagge)
