from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from prettytable import PrettyTable

driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.flipkart.com")
try:
    search_field = driver.find_element_by_class_name("LM6RPg")   #getting the search field element by class name
except NoSuchElementException as e:
    print e

search_field.clear()
search_field.send_keys("Laptops")                               #sending the search text to search field
search_field.submit()
laptop_list = []
try:
    fr = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul')
    items = fr.find_elements_by_tag_name("li")
    for item in range(len(items)) :
        if items[item].text == 'Popularity':
            xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul/li['+str(item+1)+']'
except WebDriverException as e :
    print e
print laptop_list
page_number = 1
while page_number <= 10 :
    try:
        driver.find_element_by_xpath(xpath).click()
        x = driver.find_elements_by_class_name("_3wU53n")
        for i in range(len(x)):
            try:
                A = x[i].text
                print A
            except UnicodeEncodeError as e:
                print e
    except NoSuchElementException as e:
        print e
page_number += 1

table = PrettyTable(['sr.no','Name of the Laptop'])
for t in range(len(laptop_list)):
    table.add_row([t,laptop_list[t]])
print table







