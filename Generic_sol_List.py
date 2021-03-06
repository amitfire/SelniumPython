import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from prettytable import PrettyTable
# defining global variables
driver = ''
browser = ''
url = ''
search_keyword = ''
def main():
    # taking arguments from the command line
    global browser,url,search_keyword,driver
    parser = argparse.ArgumentParser(description='Processing of browser name and url')
    parser.add_argument('-B', '--browser',help = 'Name of the browser',default= 'FireFox')
    parser.add_argument('-U', '--url',help = 'Name of the url link',default= 'https://www.flipkart.com')
    parser.add_argument('-S', '--searchKeyword',help = 'serch keyword for searching in the browser',default='Laptops')
    args = parser.parse_args()
    browser = args.browser
    url =  args.url
    search_keyword = args.searchKeyword
    #Calling Lister Class
    lister_object = Lister()


class Browser():
    #Browser Class for selection of browser as per input
    global driver,browser,url,search_keyword
    def __init__(self):
        print "In Browser class"
        self.browser = browser
        self.uri = url
        if self.browser == 'FireFox':
            driver= self.initate_firefox()    # Firefox browser initiated
        self.get_url()

    def initate_firefox(self):
        print "Opening FireFox Browser.."
        self.driver = driver
        self.driver = webdriver.Firefox()        # Managing Firefox Browser
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_url(self):
        print "Entering url in the browser.." + self.uri     # Entering URL specified in the browser
        self.driver.get(url=self.uri)


class Lister():
    # Lister Class
    global search_keyword
    def __init__(self):
        print 'In Lister Class'
        b = Browser()
        self.driver = b.driver          # getting driver attribute of Browser class
        self.search_keyword = search_keyword   # getting search keyword like 'Laptop'
        self.run()


    def run(self):
        self.laptop_list = []
        try:
            self.search_field = self.driver.find_element_by_class_name("LM6RPg")
            print "Found search field ....\n"
            # getting the search field element by class name
        except NoSuchElementException as e:
            print e
        self.search_field.clear()                 # cleared search field
        self.search_field.send_keys(str(self.search_keyword))    # sending search keyword to search field
        print "Entering %s in search Field\n"%(self.search_keyword )
        self.search_field.submit()
        try:
            # finding the elements sorted in some order like 'Popularity','Relevance','New First'
            fr = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul')
            items = fr.find_elements_by_tag_name("li")
            for item in range(len(items)):
                if items[item].text == 'Popularity':
                    #Popularity selected
                    xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul/li[' + str(item + 1) + ']'
        except WebDriverException as e:
            print e
        page_number = 1
        while page_number <= 10:   # iterating over total no. of pages
            try:
                while True:
                    try:
                        self.driver.find_element_by_xpath(xpath).click()  # clicking Popularity order
                    except WebDriverException as e :
                        print e
                    else:
                        continue

                x = self.driver.find_elements_by_class_name("_3wU53n")

                print "Getting all the %s name from "+ "page" + str(page_number)+ "\n"%self.search_keyword
                for i in range(len(x)):
                    try:
                        A = x[i].text
                        self.laptop_list.append(A) # Appending list of laptops with their details
                    except UnicodeEncodeError as e:
                        print e
            except NoSuchElementException as e:
                print e
            page_number += 1
        self.teardown()

    def teardown(self):
        name_list = []
        details_list = []
        table = PrettyTable(['sr.no', 'Name of the Laptop','Details'])
        for ele in range(len(self.laptop_list)):
            name_list.append(str(self.laptop_list[ele].split('-')[0]))
        for ele in range(len(self.laptop_list)):
            details_list.append(str(self.laptop_list[ele].split('-')[1:3]))

        for t in range(len(self.laptop_list)):
            table.add_row([t, name_list[t],str(details_list[t]).replace('u','')])
        print table






if __name__ == '__main__':
    #Main Function
    main()