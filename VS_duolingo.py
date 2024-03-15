from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pg


driver=webdriver.Chrome()
        
driver.get("https://www.duolingo.com/lesson/unit/21/level/7")

#Pause until logged in and in a story
pg.prompt("Yay?")

while True:
    
    elements = driver.find_elements(By.CSS_SELECTOR, '[data-test="stories-element"]')
    text_elements=[]
    for element in elements:
        try:
            placeholder=[]
            placeholder.append(element.text)
            placeholder.append(element.get_attribute("class"))
            text_elements.append(placeholder)
        except:
            pass
    text_elements = [element for element in text_elements if element[0].strip()]
    

    choices = driver.find_elements(By.CSS_SELECTOR, '[data-test="stories-choice"]')
    text_choices=[]
    # Iterate through the elements and do something
    for choice in choices:
        try:
            text_choices.append(choice.text)
            text_choices.append(choice.get_attribute("class"))
            text_choices.append(choice.tag_name)
        except:
            pass
    
    espana = driver.find_elements(By.XPATH, '//*[@lang="es"]')
    text_espana=[]
    for spain in espana:
        try:
            text_espana.append(spain.text)
        except:
            pass
    

    continue_buttons = driver.find_elements(By.CLASS_NAME, "_30qMV")
    #print(len(continue_buttons))
    for each in continue_buttons:
        autofocus_value = each.get_attribute("autofocus")
        if autofocus_value == "true":
            print("Continue")
            each.click()
    

    print("Choices: ",text_choices)
    print("Espana: ",text_espana)
    if len(choices) > 0 or len(espana) > 0:
        if len(choices) >= len(espana):
            print(text_elements[(-(len(choices))):])
        else:
            print(text_elements[(-(len(espana))):])
    time.sleep(1)
    #lang="es"
