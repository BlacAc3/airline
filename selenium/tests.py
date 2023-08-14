import os
import pathlib
import unittest
from selenium import webdriver

#Find the Uniform Resource Identifier of a file
def file_uri(filename):
    return  pathlib.Path(os.path.abspath(filename)).as_uri()

#Sets up webdriver using Google Chrome
driver = webdriver.Firefox()
counter_uri=file_uri("counter.html")

class WebpageTests(unittest.TestCase):
    
    
    def test_title(self):
        """Make sure title is correct"""
        driver.get(counter_uri)
        self.assertEqual(driver.title, "Counter")
        print("Checking title accuracy ---> TESTED OK")
        
    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(counter_uri)
        count=driver.find_element("tag name", "h1")
        int_count=int(count.text)
        new_count= int_count+1
        increase=driver.find_element("id", "plus")
        increase.click()
        self.assertEqual(int(driver.find_element("tag name", "h1").text), new_count)
        print("Increasing count ---> TESTED OK")
    
    def test_decrease(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(counter_uri)
        count=driver.find_element("tag name", "h1")
        int_count=int(count.text)
        new_count= int_count-1
        decrease=driver.find_element("id", "minus")
        decrease.click()
        self.assertEqual(int(driver.find_element("tag name", "h1").text), new_count)
        print("Decreasing count ---> TESTED OK")
    
    def test_multiple_increase(self):
        """Make sure header updated to 3 after 3 clicks of increase button"""
        driver.get(counter_uri)
        count=driver.find_element("tag name", "h1")
        int_count=int(count.text)
        new_count= int_count+4
        increase=driver.find_element("id", "plus")
        for i in range(4):
            increase.click()
        self.assertEqual(int(driver.find_element("tag name", "h1").text), new_count)
        print("Increasing count multiple times ---> TESTED OK")

if __name__ == "__main__":
    unittest.main()
        