# Flipkart - Web Scrapping program - Nandulal Krishna @nlkguy

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import itertools


def url_get():
    #https://www.flipkart.com/search?q=[----search term----]

    base_url='https://www.flipkart.com/search?q='

    term_q=input("\nEnter the Product name or Query : ")
    
    main_url=base_url+term_q

    return main_url


page_url = str(url_get())
page_open = urlopen(page_url) 
page_html = page_open.read()
page_open.close()
page_soup = soup(page_html,"html.parser")


all_items = page_soup.find_all('div',class_="_2pi5LC col-12-12")

print("\nCurrent page has "+ str(len(all_items)) +" items are listed")
print("\n-----------------------------------------\n")

conf=input("Show the results (y or n) : ")
str(conf)

if conf =='n':
    print("\nProgram Ended")
    quit()


item_name = page_soup.find_all('div',class_="_4rR01T")
item_price = page_soup.find_all('div',class_="_30jeq3 _1_WHN1")
item_stars = page_soup.find_all('div',class_="_3LWZlK")


for (name,price,stars) in zip(item_name,item_price,item_stars):
    print("\n Name : " + str(name.text))
    print("\n Price : " + str(price.text))
    print("\n Star Rating : " + str(stars.text))
    print("\t-----------------------------------------")

print("\n\tProgram Ended")
print("\t" + str(len(all_items)) +" items are Printed \n\t______-------______\n")


