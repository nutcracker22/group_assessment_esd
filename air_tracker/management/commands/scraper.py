import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time


URL = "https://www.scottishairquality.scot/latest/summary"

def get_website():
    website = requests.get(URL)
    doc = BeautifulSoup(website.text, "html.parser")
    return doc


def find_Aberdeen(website):
    table = website.find("table", class_="responsive-enabled table table-bordered table-striped")
    return table


def retrieve_station_links(table):
    list_of_links = []
    for link in table.find_all("a"):
        list_of_links.append("https://www.scottishairquality.scot" + link.get("href"))
    return list_of_links


def open_station_website(link):
    driver.get(link)
    driver.find_element(By.LINK_TEXT, "Site Information").click()
    #station_site = requests.get(link)
    s = BeautifulSoup(driver.page_source, 'html.parser')
    return s


def scrape_table(page):
    div = page.find("div", id="siteinformation")
    data_table = div.find("table")
    tds = data_table.find("tbody").find_all("td")
    station_details = Station_details.objects.create(
        site_name=tds[0].text,
        site_type=tds[1].text,
        latitude=tds[3].text.split(" ")[0],
        longitude=tds[3].text.split(" ")[1],
        site_comments=tds[6].text,
    )
    station_details.save()
#    site_name = tds[0].text
#    site_type = tds[1].text
#    site_latitude = tds[3].text.split(" ")[0]
#    site_longitude = tds[3].text.split(" ")[1]
#    site_comment = tds[6].text
#    return site_name, site_type, site_latitude, site_longitude, site_comment


def scrape_starter():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    doc = get_website()
    table_aberdeen = find_Aberdeen(doc)
    link_list = retrieve_station_links(table_aberdeen)
    for link in link_list:
        station = open_station_website(link)
        data = scrape_table(station)


def finishing():
    time.sleep(10)
    driver.quit()
