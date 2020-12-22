# Flipkart - Web Scrapping program - Nandulal Krishna
# version current
#------------------------------------------------------------------------------
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import itertools
#from urlgetfunc import url_get # See urlgetfunc.py file 

#------------------------------------------------------------------------------

def url_get():
    #https://www.flipkart.com/search?q=[----search term----]
    base_url='https://www.flipkart.com/search?q='

    search_term=input("\nEnter the Product name or Query : ")
    main_url=base_url+search_term
    return main_url

#------------------------------------------------------------------------------

page_url = str(url_get()) # calling url_get()
page_open = urlopen(page_url) 
page_html = page_open.read()
page_open.close()
page_soup = soup(page_html,"html.parser")


#------------------------------------------------------------------------------

all_items = page_soup.find_all('div',class_="_2pi5LC col-12-12") # See Image01.png

print(f'{len(all_items)} items are found')

show = input("\nShow the results (y or n) : ")
save = input("\nSave the results (y or n) : ")

if str(show) =='n':
    print("\nProgram Ended")
    quit()

#------------------------------------------------------------------------------

item_name = page_soup.find_all('div',class_="_4rR01T")
item_price = page_soup.find_all('div',class_="_30jeq3 _1_WHN1")
item_stars = page_soup.find_all('div',class_="_3LWZlK")

#------------------------------------------------------------------------------

# Iterate on the bs4.element.ResultSet(sub category of List) using itertools
# Refer https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously

#for index ,(name,price,stars) in enumerate (zip(item_name,item_price,item_stars),start=1):
    #print("\n "+ str(index)+". Name : " + str(name.text))
    #print("\n\t Price : " + str(price.text))
    #print("\n\t Star Rating : " + str(stars.text))

#------------------------------------------------------------------------------

if str(save) =='y':
    filename = "products.csv"
    file = open(filename,"w") # Open the file
    headers = "Serial_Number,Product_Name,Price,Star_Rating\n"

    file.write(headers) # Write Header to 
    print("\n-----------------------------------------------------------------\n")
    print(headers)
    for index ,(name,price,stars) in enumerate (zip(item_name,item_price,item_stars),start=1):
        
        print(str(index) + ".  " + str(name.text).replace(",", " | ") + " , " + str(price.text) + " , " + str(stars.text) + "\n")

        file.write(str(index) + "," + str(name.text).replace(","," | ") + "," + str(price.text).replace(","," ") + "," + str(stars.text) + "\n")
       
    file.close()
    print(f"\n\tProduct Details Saved in {filename} ")

#------------------------------------------------------------------------------

print("\n\tProgram Ended")
print(f'\n\t{str(index)} items are Printed')



#References
#https://stackoverflow.com/questions/36076052/beautifulsoup-find-all-on-bs4-element-resultset-object-or-list

#------------------------------------------------------------------------------
# get url or search parameters for flipscrap_main.py
# https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off
# https://www.flipkart.com/search?q=smartphone (using text concatenation to add search query)

# https://www.flipkart.com/all-categories/pr?affid=amaledasse&wgtid=FK-AF-SB&sid=search.flipkart.com&q=smartphone
# above link is from affiliate search widget

#def get_para():
#------------------------------------------------------------------------------
