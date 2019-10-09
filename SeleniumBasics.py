from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Vipul Singh DF\Drivers\chromedriver_win32\chromedriver.exe")


driver.get("http://us145k12php01.apc.sitel-world.net/HPTrident/View/Login.aspx")

print(driver.title)

driver.maximize_window()

#Find Emlement
driver.find_element_by_id("TxtNTID").send_keys("rcabr032")
time.sleep(1)
driver.find_element_by_id("TxtPassword").send_keys("123")
time.sleep(1)
driver.find_element_by_id("Btnlogin").click()

time.sleep(5)

driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_dtFromdate_dateInput").send_keys("06/10/2019")
time.sleep(2)
driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_dtTodate_dateInput").send_keys("06/10/2019")
time.sleep(2)

#Wait  = WebDriverWait(driver,10)

driver.find_element(By.XPATH,"/html/body/form/div[5]/div[1]/div[2]/div[5]/div/input").click()


'''Conditional Statements
ele = driver.find_element_by_id("TxtNTID")
ele.is_displayed()
ele.is_enabled()
ele.is_selected()
'''

#driver.quit()

'''Navigations
#driver.back()
#driver.forward()'''
