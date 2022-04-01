import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



@given("I navigate to the home page")
def user_on_product_newpage(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    print(base_url)
    open_url = urljoin(base_url, '/station/')
    context.browser.get(open_url)


@when("I choose a station and click on it")
def user_chooses_station(context):
    # use print(context.browser.page_source) to aid debugging
    #print(context.browser.page_source)
    name_textfield = context.browser.findElement(By.cssSelector("a[href*='/station/details/3/']"))
    click = name_textfield.click()
    time.sleep(3)


@then("I should see the details for that station")
def product_added(context):
    assert 'King Street' in context.browser.page_source
