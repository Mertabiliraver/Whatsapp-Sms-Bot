from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class redbull():
    # hız versin diye :d
    number_list = []
    def __init__(self,driver = webdriver.Firefox()):
        dosya = open("number.txt","r",encoding="utf-8")
        oku = dosya.read()
        kelime = ""
        for numara in oku:
 
            if  numara == "\n":
                number_list.append(kelime)
                kelime = ""
                
            else:
                kelime += str(numara)
     
        a = 0
        
        yazılacak = "deneme mesajı"
       
        driver.get("https://web.whatsapp.com/send?phone=90{}&text={}".format("5389321203","Sistem başlatıldı."))
        time.sleep(3)
        driver.find_element_by_class_name("_1U1xa").click()
        print("Telefon kod onaylaması bekleniliyor...")
        
        time.sleep(6)
        
        for i in number_list:
            
            driver.get("https://web.whatsapp.com/send?phone=90{}&text={}".format(i,yazılacak))
            time.sleep(3)
            driver.find_element_by_class_name("_1U1xa").click()
            print("+1")
            a += 1
            
            if a == 9:
                time.sleep(9)
                a = 0
redbull()   
