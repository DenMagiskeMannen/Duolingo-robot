# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:38:04 2024

@author: teodo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:21:38 2024

@author: teodo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:33:59 2024

@author: teodo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from faker import Faker
import threading
from selenium.webdriver.chrome.options import Options
import pyautogui as pg

email = ""
password = ""
 

#yKwvl


#options.add_argument(f"--window-position={x},{y}")
#driver = webdriver.Chrome(options=options)
"""
cool_driver=webdriver.Chrome()
cool_driver.get("https://www.duolingo.com/")
pg.prompt("Yay?")


for i in range(thredlies):
    cool_driver.execute_script("window.open('https://www.duolingo.com/lesson/unit/21/level/7','_blank');")

"""
#cookeisese=cool_driver.get_cookies()
thredlies=3

#aria-label="Lesson"
#aria-label="Story"
#_1eJKW _16r-S y_aHp _3xT0z
#_1eJKW _16r-S _6-Jk5 _3xT0z
#_1eJKW _16r-S _6-Jk5 _3xT0z
#_1eJKW _16r-S _3pULP _3xT0z


#_1reas
#Unclickable
#src="https://d35aaqx5ub95lt.cloudfront.net/images/path/icons/3ea75bf2164eed9218a7163be002af82.svg"

#Clickable
#src="https://d35aaqx5ub95lt.cloudfront.net/images/path/icons/5367427ba2aa472b8cc5ddb13ebabf2c.svg"
Clickable_Story=["https://d35aaqx5ub95lt.cloudfront.net/images/path/icons/5367427ba2aa472b8cc5ddb13ebabf2c.svg"]
Clickable_Story.append("https://d35aaqx5ub95lt.cloudfront.net/images/path/icons/7aa61c3f60bd961a60a46fb36e76c72f.svg")
#src="https://d35aaqx5ub95lt.cloudfront.net/images/path/icons/7aa61c3f60bd961a60a46fb36e76c72f.svg"

class Overseer():
    Found_stories=True
    def __init__(self,New_account=False):
        self.account=New_account
        self.name="Bob"
        #self.options=options
        self.options = Options()
        self.options.add_argument("--mute-audio")
        self.options.add_argument(f"--window-position={200},{25}")
        #self.options.headless = False
        self.driver=webdriver.Chrome(options=self.options)
        
        self.driver.get("https://www.duolingo.com/lesson/unit/21/level/7")
        
        if self.account==True:
            self.make_account()
        
        
    def Try_login(self,index):
        try:
            email_place = self.driver.find_element(By.ID, "web-ui1")
            password_place = self.driver.find_element(By.ID, "web-ui2")
            # Use find_elements to get a list of elements with the specified class
            login_buttons = self.driver.find_elements(By.CLASS_NAME, "_1fHYG")
            for button in login_buttons:
                #print(button.text)
                if button.text=="LOG IN":
                    print("FOUND")
                    email_place.clear()
                    #time.sleep(0.1)
                    email_place.send_keys(email)
                    password_place.clear()
                    #time.sleep(0.1)
                    password_place.send_keys(password)
                    button.click()
            # Choose the specific instance you want to interact with (for example, the first one)
            #login_button = login_buttons[index]
            
            #self.driver.execute_script("arguments[0].click();", login_button)
            print(f"{self.name} login YES")
            time.sleep(0.5)
        except:
            #print(f"{self.name} failed login")
            pass
            #print("Couldnt login")
        
    def refresh(self):
        self.driver.navigate().refresh()
        
    def get_stories(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "_1reas")

        for element in elements:
            src_attribute = element.get_attribute("src")
            #print("Src attribute:", src_attribute)
            if src_attribute in Clickable_Story:
                print("Src attribute:", src_attribute)
                
                #time.sleep(1)
                element.click()
                #time.sleep(1)
                #class="_30qMV _2N_A5 _36Vd3 _16r-S KSXIb _2CJe1 _12StQ"
                popup= self.driver.find_element(By.CLASS_NAME, "_30qMV _2N_A5 _36Vd3 _16r-S KSXIb _2CJe1 _12StQ")
                level=popup.get_attribute("href")
                print(level)
                #_30qMV _2N_A5 _36Vd3 _16r-S KSXIb _2CJe1 _12StQ
                
                
                
            
        self.Found_stories=True
        print("Found all stories!")
            
    def run(self):
        #_1eJKW
        
        count=1
        
        while True:
            try:
                
                lessons=self.driver.find_elements(By.CLASS_NAME, "_1eJKW")
                self.Try_login(2)
                if self.Found_stories==True:
                    if count%25==0:
                        self.driver.get("https://www.duolingo.com/leaderboard")
                    if count %250 == 0:
                        self.driver.get("https://www.duolingo.com/learn")
                        self.get_stories()
                    
               
                elif self.Found_stories==False:
                    if count%20==0:
                        self.driver.get("https://www.duolingo.com/learn")
                        self.get_stories()
                        
                #print(count)
                url=self.get_url()
                #print(url)
                if url == "https://www.duolingo.com/":
                    self.driver.get("https://www.duolingo.com/lesson/unit/21/level/7")
                
                time.sleep(1)
            except:
                pass
            
            count+=1
            time.sleep(0.1)
            
    def get_url(self):
        return(self.driver.current_url)
    
    def make_account(self):
        pass
        
#https://www.duolingo.com/lesson/unit/21/level/7?isLoggingIn=true


#https://www.duolingo.com/lesson/unit/21/level/7
#https://www.duolingo.com/lesson/unit/3/level/12
actuelle_lessons=[[3,6],[3,12]]
#NoSuchElementException:
class robot():
    rbots=[]
    def __init__(self,x,y,amount):  
        fake = Faker()
        self.name = fake.name()
        self.amount=amount
        #self.options=options
        self.options = Options()
        self.options.add_argument("--mute-audio")
        
        #self.options.add_argument("--headless=new")
        self.options.add_argument(f"--window-position={x},{y}")
        self.driver=webdriver.Chrome(options=self.options)
        self.driver.get("https://www.duolingo.com/lesson/unit/21/level/7")
        """
        for cookie in cookeisese:
            self.driver.add_cookie(cookie)
            """
        title = self.driver.title
        self.experience=0
        
        print(f"{self.name} has been born, with destinies of {self.amount}")
        self.rbots.append(self)
        self.driver.implicitly_wait(0.9)
    def __str__(self):
        return(self.name)
    
    def Try_login(self,index):
        try:
            email_place = self.driver.find_element(By.ID, "web-ui1")
            password_place = self.driver.find_element(By.ID, "web-ui2")
            # Use find_elements to get a list of elements with the specified class
            login_buttons = self.driver.find_elements(By.CLASS_NAME, "_1fHYG")
            for button in login_buttons:
                #print(button.text)
                if button.text=="LOG IN":
                    #print("FOUND")
                    email_place.clear()
                    #time.sleep(0.1)
                    email_place.send_keys(email)
                    password_place.clear()
                    #time.sleep(0.1)
                    password_place.send_keys(password)
                    button.click()
            # Choose the specific instance you want to interact with (for example, the first one)
            #login_button = login_buttons[index]
            
            #self.driver.execute_script("arguments[0].click();", login_button)
            #print(f"{self.name} login YES")
            time.sleep(0.5)
        except:
            #print(f"{self.name} failed login")
            pass
            #print("Couldnt login")
    
    def Account(self):
        #onetrust-accept-btn-handler
        #Eg_1d already have an account?
        cookies=self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies.click()
        account=self.driver.find_elements(By.CLASS_NAME, "Eg_1d")
        account[1].click()
    
    def keep_playing(self):
        try:
            
            dont_kill_yaslef=self.driver.find_elements(By.CLASS_NAME, "_30qMV")
            for loc in dont_kill_yaslef:
                loc.click()
        except:
            pass
    
    def continue_button(self,bypass=False):
        try:
            continue_button = self.driver.find_element(By.CLASS_NAME, "_30qMV")
            autofocus_value = continue_button.get_attribute("autofocus")
            #print(autofocus_value)
            if autofocus_value == "true":
                continue_button.click()
            elif bypass == True:
                continue_button.click()
            elif autofocus_value == None:
                pass
                #print("Couldnt find continue button")
        except:
            pass
            #print("Couldtn locate cont")
    def streak_thing_button(self):
        try:
            continue_button = self.driver.find_elements(By.CLASS_NAME, "yKwvl")
            random_button=random.choice(continue_button)
            random_button.click()
            continue_button = self.driver.find_elements(By.CLASS_NAME, "_1fHYG")
            random_button=random.choice(continue_button)
            random_button.click()
            #_1fHYG
        except:
            pass
    
    
    def often_boxs(self):
        try:
            possibilities = self.driver.find_elements(By.CLASS_NAME, "_21Icd")
            rando=random.choice(possibilities)
            rando.click()
            
        except:
            pass
    def many_boxes(self):
        try:
            possibilites = self.driver.find_elements(By.CLASS_NAME, "_1deIS")
            #print(possibilites[1])shuffle(possibilites)
            for rando in possibilites:
                rando=random.choice(possibilites)
                rando.click()
        except:
            pass
    def fucka(self):
        try:
            shits=self.driver.find_elements(By.CLASS_NAME, "_3p1ox")
            shitty_rando=random.choice(shits)
            shitty_rando.click()
            #print("Fuckka")
        except:
            pass
    
    def get_url(self):
        return(self.driver.current_url)
    
    def back(self):
        self.driver.back()
        
    def find_story(self):
        try:
            stories=[]
            clickables=self.driver.find_elements(By.CLASS_NAME, "_1eJKW _16r-S y_aHp _3xT0z")
            for clic in clickables:
                stor=clic.get_attribute("aria-label")
                print(stor)
                if stor == "Story":
                    stories.append(clic)
            rando=random.choice(stories)
            rando=stories[0]
            rando.click()
            time.sleep(0.3)
            #_30qMV _2N_A5 _36Vd3 _16r-S KSXIb _2CJe1 _12StQ
            practic=self.driver.find_elements(By.CLASS_NAME, "_30qMV _2N_A5 _36Vd3 _16r-S KSXIb _2CJe1 _12StQ")
            practic.click()
        except:
            pass
    def delete(self):
        self.driver.quit()
        self.rbots.remove(self)
    
    def run(self):
        count=0
        amount=0
        print(f"!!{self.name}!! is at run {amount}")
        
        while amount < self.amount:
            try:
                time.sleep(0.1)
                self.experience=amount*5
                self.continue_button()
                self.often_boxs()
                self.many_boxes()
                
                if count % 5==0:
                    self.continue_button(True)
                    #Vil flytte fucka til utenfor
                    self.fucka()
                    url=self.get_url()
                    if url == "https://www.duolingo.com/learn":
                        #self.back()
                        #self.find_story()
                        rando=random.choice(actuelle_lessons)
                        print(rando)
                        self.driver.get(f"https://www.duolingo.com/lesson/unit/{rando[0]}/level/{rando[1]}")
                        amount+=1
                        print(f"{self.name} is at run {amount}")
                if count % 10==0:
                    #self.Account()
                    self.Try_login(2)
                if count % 30==0:
                    self.streak_thing_button()
                if count % 75 == 0:
                    rando=random.choice(actuelle_lessons)
                    self.driver.get(f"https://www.duolingo.com/lesson/unit/{rando[0]}/level/{rando[1]}")

                count+=1
                #print(f"{self.name} cycle {count}")
            except:
                pass
        print(f"{self.name} has finished job with {amount} runs")
        
        self.delete()
        
        
    @classmethod
    def tally_xp(cls):
        total_xp=0
        for robby in cls.rbots:
            total_xp+=robby.experience
        print(f"Current Total EXP gained!: {total_xp}")
        
            
        


    





#But like, fuck chatgpt
class Fcuk_you_chat:
    threads = []
    names=[]
    def __init__(self,x,y):
        t = threading.Thread(target=self.threading_duolingo_robot,args=(x,y), daemon=True)
        print(self.names)
        t.start()
        threads.append(self)
        
    def threading_duolingo_robot(self,x,y,amount_run=100):
        placeholder=robot(x,y,amount_run)
        self.names.append(placeholder.name)
        placeholder.run()
        self.threads.remove(self)
    
#This could probably be done a whole lot more neatly then a new class, buuuuuut....
class Overseer_threads:
    WATCHERS=[]
    def __init__(self):
        t = threading.Thread(target=self.actual_thread, daemon=True)
        #print(self.names)
        self.WATCHERS.append(self)
        t.start()
        
    def actual_thread(self):
        PH=Overseer()
        PH.run()
        self.WATCHERS.remove(self)
    
screen=[1920,1080]
min_x=int(screen[0]/(-2.1))
max_x=int(screen[0]//1.938)
print(min_x,max_x)
#1.938
amount_of_room=max_x-min_x




jump_amount_window_distance=int(amount_of_room/thredlies)
threads = Fcuk_you_chat.threads
Watchers=Overseer_threads.WATCHERS
#names=Fcuk_you_chat.names
x_posses=[]
for i in range(thredlies):
    x_posses.append(max_x-(jump_amount_window_distance*i))

print(x_posses)

def give_next_x(previous):
    count=0
    Found=False
    if previous == None:
        Next = x_posses[0]
        Found=True
    while not Found:
        if  previous==x_posses[-1]:
            Next=x_posses[0]
            Found=True
        elif x_posses[count]==previous:
            Next=x_posses[count+1]
            Found=True
        count+=1
    print(previous,Next)
    return(Next)


prev=None
while True:
    time.sleep(1)
    #print(len(threads))
    
    
    if (len(threads))<thredlies:
       x_pos=give_next_x(prev)
       bob=Fcuk_you_chat(x_pos,25)
       prev=x_pos
       #print(len(robot.rbots))
       #print(len(threads))
       for i in range(10):
           time.sleep(1)
    elif (len(Watchers))<1:
        REAL_bob=Overseer_threads()
    robot.tally_xp()
    


   
   

    

for rob in robot.rbots:
    rob.driver.quit()
