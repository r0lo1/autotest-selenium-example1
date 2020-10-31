#!/bin/env python3
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import HandbookPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.common.exceptions import NoSuchElementException 

import math
import time
class HandbookPage(BasePage):
    def by_book(self):
        self.name = self.browser.find_element(*HandbookPageLocators.NAME).text
        self.price = self.browser.find_element(*HandbookPageLocators.PRICE).text
        by_book_link = self.browser.find_element(*HandbookPageLocators.BY_SUBMIT)
        by_book_link.click()
        self.solve_quiz_and_get_code()
        self.cart = self.browser.find_element(*HandbookPageLocators.CART).text
        self.name2 = self.cart = self.browser.find_element(*HandbookPageLocators.NAME2).text
        assert self.name!=self.name2 or self.cart!=self.price, print("Error {} {} {} {}".format(self.name,self.cart,self.price,self.name2))

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"            

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"                

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()            
        except NoAlertPresentException:
            print("No second alert presented")
