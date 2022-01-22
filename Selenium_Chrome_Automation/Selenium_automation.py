from re import search
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



def login() : 
    driver.get('https://aumsam.amrita.edu/cas/login?service=https%3A%2F%2Faumsam.amrita.edu%2Faums%2FJsp%2FCore_Common%2Findex.jsp')

    username = driver.find_element_by_xpath('//*[@id="username"]')
    username.send_keys('')

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('')

    loginbar = driver.find_element_by_xpath('//*[@id="fm1"]/section[3]/input[3]')
    loginbar.click()

    del username
    del password
    del loginbar

    exit 

def google_search(command): 

    ruth1 = command.replace('search google', '')
    
    driver.get('https://www.google.com/')

    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(ruth1 + Keys.ENTER)
    

    exit 



