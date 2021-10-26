# import necessary libraries
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
import re
import xlwt

"""
    Intance variables
"""
#counter for the excel sheet
i = 0

#arrays to hold the desired values
event_titles = []
event_dates = []
event_hosts = []
event_links = []


"""
    Setting up driver and link
"""
#using Chrome as web driver
driver = webdriver.Chrome()

#website link
url = "https://connectru.ryerson.ca/events"

#web driver accesses and stores the information from url
driver.get(url)
page = driver.page_source
page_soup = soup(page, 'html.parser')

"""
    Finding the desired tags for events
"""

#finds all events titles
all_events = page_soup.findAll("h3", {"style" : "font-size: 17px; font-weight: 600; overflow: hidden; margin: 2px 0px 5px; line-height: 20px; display: -webkit-box; max-width: 400px; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: ellipsis;"})

#finds all dates
all_dates = page_soup.findAll("div", {"style" : "white-space: nowrap; text-overflow: ellipsis; overflow: hidden; margin: 0px 0px 2px;"})

#finds all event hosts
all_hosts = page_soup.findAll("span", {"style" : "width: 91%; display: inline-block; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"})

#finds all links (sorta, currently buggy need to remove first and last few)
events_div = page_soup.find('div', id='event-discovery-list')


"""
    Storing the information in appropriate arrays
"""

#printing all the links currently working on
aTags = events_div.find_all('a')
for a in aTags:
    print(a['href']) # your event href is here
    urlfront = "connectru.ryerson.ca"
    event_links.append(urlfront + a['href'])

    

for event in all_events:
    event_titles.append(event.text)

for date in all_dates:
    event_dates.append(date.text)

for host in all_hosts:
    event_hosts.append(host.text)

""" 
    Exporting the data onto an excel File
"""

book = xlwt.Workbook()

sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok = True)

sheet1.write(0, 0, "Title")
sheet1.write(0, 1, "Date/Time")
sheet1.write(0, 2, "Host")
sheet1.write(0, 3, "Link")

for event_title in all_events:
    sheet1.write(i+1, 0, event_titles[i])
    sheet1.write(i+1, 1, event_dates[i])
    sheet1.write(i+1, 2, event_hosts[i])
    sheet1.write(i+1, 3, event_links[i])
    i = i+1
    
book.save("test.xls")