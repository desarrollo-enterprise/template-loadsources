"""
#####################################
# Author: Ernesto Quito Gonzales    #
# Date: 02/07/2019                  #
#####################################
"""
from setting import setting_web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class WebScrap:
    urls = ''
    credential = ''

    def __init__(self, urls, credential):
        self.urls = urls
        self.credential = credential

    def give_credential(self):
        user = self.credential["user"]
        password = self.credential["password"]

        print(f"""USUARIO:\t\t{user}
CONTRASEÑA:\t\t{password}""")

        # Here you could write the code selenium to enter to the web and has the searching in the web.
        


a = WebScrap(setting_web['url'], setting_web['credential'])
a.give_credential()
