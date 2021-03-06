#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest, time, os,shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select




folder = 'tests/livetest'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))



class ChromeSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        prefs = {"download.default_directory" : "/var/www/html/tests/livetest"}
        options.add_experimental_option("prefs",prefs)

        self.driver = webdriver.Chrome('/var/www/html/dist/api/chromedriver', chrome_options=options)
        self.driver.set_window_size(1400,800)



    #@unittest.skip("demonstrating skipping")
    def test_10_federal(self):
        print "Test Live Federal"
        driver = self.driver
        driver.get('https://sharepicgenerator.de')

        self.assertIn("Sharepicgenerator", driver.title)

        # gain access
        driver.execute_script("$('#test-access-opener').removeClass('d-none');")
        driver.find_element_by_id('test-access-opener').click()
        time.sleep(1)
        driver.find_element_by_id('test-access-password').send_keys( u"lennart" )
        driver.find_element_by_id('test-access-target-federal').click()
        driver.find_element_by_id('test-access-submit').click()
        time.sleep(1)


        print "click download"
        driver.find_element_by_id('download').click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "download"))
        )
        time.sleep(1)
        print "downloaded"

    @unittest.skip("demonstrating skipping")
    def test_20_bayern(self):
        print "Test Live Bayern"
        driver = self.driver
        driver.get('https://sharepicgenerator.de')

        self.assertIn("Sharepicgenerator", driver.title)

        # gain access
        driver.execute_script("$('#test-access-opener').removeClass('d-none');")
        driver.find_element_by_id('test-access-opener').click()
        time.sleep(1)
        driver.find_element_by_id('test-access-password').send_keys( u"lennart" )
        driver.find_element_by_id('test-access-target-bayern').click()
        driver.find_element_by_id('test-access-submit').click()
        time.sleep(1)

        driver.find_element_by_id('text').send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_id('text').send_keys( u"Test Bayern" )


        print "click download"
        driver.find_element_by_id('download').click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "download"))
        )
        print "downloaded"

        time.sleep(2)





    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()