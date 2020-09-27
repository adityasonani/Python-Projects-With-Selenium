from selenium import webdriver
from time import sleep
import numpy as np


class Bot:
    def __init__(self):
                                                        # Below specify the chrome driver path
        self.driver = webdriver.Chrome(executable_path="# Here specify the chrome driver path")
        self.driver.get("https://www.instagram.com")
        sleep(3)
        self.driver.find_element_by_name("username").send_keys("#add uname here")    #username
        self.driver.find_element_by_name("password").send_keys("#add pd here")       #password and good to go.
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]").click()
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div") 
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
        sleep(3)
    

    def get_unfollowers(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        sleep(2)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div")
        scroll_box = box.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        sleep(2)
        last, ht = 0, 1
        while last != ht: 
            last = ht   
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        sleep(2)
        links = scroll_box.find_elements_by_tag_name("a")
        global names
        names = [name.text for name in links if name.text != '']
        sleep(2)
        box.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]").click()
        sleep(3)
        print("Following are: ", names)

    
    def get_followers(self):
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        sleep(2)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div")
        scroll_box = box.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        sleep(2)
        last, ht = 0, 1
        while last != ht: 
            last = ht   
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        sleep(2)
        link = scroll_box.find_elements_by_tag_name("a")
        name = [name.text for name in link if name.text != '']
        sleep(2)
        box.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]").click()
        sleep(3)
        print("Followers are: ", name)

        sleep(2)
        morons = np.setdiff1d(names,name)
        print("Following who don't follow you back: ", morons)
        self.driver.quit()
        exit()
   
        
if __name__ == "__main__":
    my_bot = Bot()
    my_bot.get_unfollowers()
    my_bot.get_followers()
