from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pg


driver=webdriver.Chrome()
        
driver.get("https://www.duolingo.com/lesson/unit/21/level/7")

#Pause until logged in and in a story
pg.prompt("Yay?")

while True:
    
    #elements = driver.find_elements(By.CSS_SELECTOR, '[data-test="stories-element"]')
    #text_elements=[]
    #for element in elements:
       # text_elements.append(element.text)
        #text_elements.append(element.get_attribute("class"))
    #print(text_elements)

    choices = driver.find_elements(By.CSS_SELECTOR, '[data-test="stories-choice"]')
    text_choices=[]
    # Iterate through the elements and do something
    for choice in choices:
        text_choices.append(choice.text)
        text_choices.append(choice.get_attribute("class"))
        text_choices.append(choice.tag_name)
    continue_buttons = driver.find_elements(By.CLASS_NAME, "_30qMV")
    #print(len(continue_buttons))
    for each in continue_buttons:
        autofocus_value = each.get_attribute("autofocus")
        if autofocus_value == "true":
            print("Continue")
    print(text_choices)
    time.sleep(1)