# import necessary libraries
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
import re


driver = webdriver.Chrome()

#website link
url = "https://connectru.ryerson.ca/events"

driver.get(url)

page = driver.page_source
page_soup = soup(page, 'html.parser')

#finds all events within the specified divisions
all_events = page_soup.findAll("h3", {"style" : "font-size: 17px; font-weight: 600; overflow: hidden; margin: 2px 0px 5px; line-height: 20px; display: -webkit-box; max-width: 400px; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: ellipsis;"})

#finds all dates
all_dates = page_soup.findAll("div", {"style" : "white-space: nowrap; text-overflow: ellipsis; overflow: hidden; margin: 0px 0px 2px;"})

#finds all event hosts
all_hosts = page_soup.findAll("span", {"style" : "width: 91%; display: inline-block; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"})

#finds all links (sorta, currently buggy need to remove first and last few)
all_links = page_soup.select("a", {"style" : "text-decoration: none;"})

event_titles = []
event_dates = []
event_hosts = []
event_links = []


for event in all_events:
    event_titles.append(event.text)

for date in all_dates:
    event_dates.append(date.text)

for host in all_hosts:
    event_hosts.append(host.text)

""" #printing all the links currently working on
for link in all_links:
    print(link['href'])
    event_links.append(link['href'])
print(event_links) """

""" Exporting the data onto an excel File"""

import xlwt

i = 0

book = xlwt.Workbook()

sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok = True)

for event_title in all_events:
    sheet1.write(i, 0, event_titles[i])
    sheet1.write(i, 1, event_dates[i])
    sheet1.write(i, 2, event_hosts[i])
    i = i+1
    

book.save("test.xls")