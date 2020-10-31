#!/bin/env python3
from pages.handbook_page import HandbookPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_handbook_cart_add(browser,link):
   #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   
   page = HandbookPage(browser, link)
   page.open()
   page.by_book()
   #time.sleep(50)

@pytest.mark.missing_element
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):

   page = HandbookPage(browser, link)
   page.open()
   page.by_book()
   page.should_not_be_success_message()
    
#Открываем страницу товара 
#Добавляем товар в корзину 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.missing_element
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser,link):
 
   page = HandbookPage(browser, link)
   page.open()
   page.should_not_be_success_message()
#Открываем страницу товара 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.missing_element 
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser,link):
 
   page = HandbookPage(browser, link)
   page.open()
   page.by_book()
   page.should_not_be_success_message_disappeared()
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared


   
