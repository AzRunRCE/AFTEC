import time
from selenium import webdriver
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
_user = input("Identifiant :")
_pass =raw_input("Mot de passe :")
_count = input("Nombre d'heure :")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://eduservices.lms.crossknowledge.com/interfaces/login.php")
user = wait.until(EC.element_to_be_clickable((By.ID, 'fldUserName')))
user.send_keys(_user)
passwd = wait.until(EC.element_to_be_clickable((By.ID, 'fldPassword')))
passwd.send_keys(_pass)
passwd.send_keys(Keys.RETURN)
driver.implicitly_wait(10) 
i = 0
_count = int(_count * 4)
while i < _count:
   nb =  randint(1904, 2772)
   driver.get("https://eduservices.lms.crossknowledge.com/candidat/product_sheet.php?trainingcontent_id=" + str(nb))
   driver.implicitly_wait(10) 
   duration = driver.find_element_by_class_name("productDuration").text
   title =   driver.find_element_by_xpath("//*[@id='pageContent']/table/tbody/tr/td[2]/h1").text
   duration = duration.replace("\t", "")
   if "15 min." in duration:
      doc =   wait.until(EC.element_to_be_clickable((By.ID, 'learningObjectContainerOverlap')))
      print(title +" : " + driver.current_url)
      doc.click()
      time.sleep(10)
      i = i + 1