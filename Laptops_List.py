from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from prettytable import PrettyTable


class Lister():

    def __init__(self,uri):
        self.uri = uri


    def set_up(self):
        print "Setting up...\n"
        print "Opening FireFox Browser.."
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print "Entering url in the browser.."+ self.uri
        self.driver.get(url=self.uri)
        self.run()

    def run(self):
        self.laptop_list = []
        try:
            self.search_field = self.driver.find_element_by_class_name("LM6RPg")
            print "Found search field ....\n"
            # getting the search field element by class name
        except NoSuchElementException as e:
            print e
        self.search_field.clear()
        self.search_field.send_keys("Laptops")
        print "Entering Laptops in search Field\n"# sending the search text to search field
        self.search_field.submit()
        try:
            fr = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul')
            items = fr.find_elements_by_tag_name("li")
            for item in range(len(items)):
                if items[item].text == 'Popularity':
                    xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/section/ul/li[' + str(item + 1) + ']'
        except WebDriverException as e:
            print e
        page_number = 1
        while page_number <= 10:
            try:
                self.driver.find_element_by_xpath(xpath).click()
                x = self.driver.find_elements_by_class_name("_3wU53n")
                print "Getting all the Laptops name from "+ "page" + str(page_number)+ "\n"
                for i in range(len(x)):
                    try:
                        A = x[i].text
                        self.laptop_list.append(A)
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



a= Lister("https://www.flipkart.com")
a.set_up()

