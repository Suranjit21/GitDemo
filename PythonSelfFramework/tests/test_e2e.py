import pytest
import self as self
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions



from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


# from OopsDemo.secondTry.conftest import setup
# from OopsDemo.secondTry.secondBaseClass import BaseClass
# from OopsDemo.secondTry.secondHomepage import Home
#
#
# from tests.utilities.CheckoutPage import CheckoutPage
# from tests.utilities.ConfirnPage import ConfirmPage



# @pytest.mark.usefixtures("ourSetup")
# from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

   def tests_e2e(self):

       self.driver.find_element_by_css_selector("a[href*='shop']").click()
       # home = Home(self.driver)
       # home.clickShop().click()

       cards = self.driver.find_elements_by_css_selector(".card-title a")
       i = -1
       for card in cards:
           i = i + 1
           cardText = card.text

           if cardText == "Blackberry":
               self.driver.find_element_by_xpath("//app-card-list [@class='row']/app-card[4]/div/div[2]/button").click()

       self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
       self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

       self.driver.find_element_by_id("country").send_keys("ind")

       wait = WebDriverWait(self.driver, 10).until(
           expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

       self.driver.find_element_by_link_text("India").click()

       self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

       self.driver.find_element_by_css_selector("[type='submit']").click()




       # print("hey champss. tessting to see if my code changes ernt rhough ")



       print("hello there")


       print ("try the new push and pull")

       print("this is kinda fun tbh")
       print("we really out hre")
#