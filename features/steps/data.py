import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



@given("I navigate to the data page")
def user_on_product_newpage(context):
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    print(base_url)
    open_url = urljoin(base_url, '/data/')
    context.browser.get(open_url)


@when("I choose a station and click \'submit\'")
def user_chooses_station(context):
    # use print(context.browser.page_source) to aid debugging
    #print(context.browser.page_source)
    name_textfield = context.browser.find_element(By.CLASS_NAME, "data-page-filter-form")
    #select_element = name_textfield.find_element(By.NAME, 'station_name')
    select_element = name_textfield.find_element(By.CLASS_NAME, 'data-page-select')
    select_object = Select(select_element)
    union_street = select_object.select_by_visible_text('Union Street')
    submit = context.browser.find_element(By.ID, "data-page-submit-button")
    time.sleep(3)
    submit.click()
    time.sleep(3)


@then("I should see the data for that station")
def product_added(context):
    assert 'Union Street' in context.browser.page_source
