from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # allows us to use keys on keyboard
import time
import clipboard

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path = PATH,options=options)

driver.get("https://shubham-websol-word-processing.netlify.app/")



# print title of tabs in console
print(driver.title)
driver.implicitly_wait(1000)

# # Find search bar 
search = driver.find_element_by_tag_name('textarea')
# # Enter the text to be processed 
search.send_keys('Hello There! I have the High Ground!')
driver.implicitly_wait(2000)
time.sleep(3)
# # Turn on dark mode
driver.find_element_by_xpath("//label[@class='switch']").click()
time.sleep(3)
# # Select convert to upper case
driver.find_element_by_xpath("//*[@id='root']/div/div[4]/div/button[1]").click()
time.sleep(3)
# # Select a background color for dark mode
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/input[2]").click()
time.sleep(3)
# # Turn off Dark Mode
driver.find_element_by_xpath("//label[@class='switch']").click()
time.sleep(3)
# # Select remove space
driver.find_element_by_xpath("//*[@id='root']/div/div[4]/div/button[3]").click()
time.sleep(3)

# # copy content from preview section and print in console
string = driver.find_element_by_xpath("//*[@id='root']/div/div[4]/div/div[3]/p").text
print(string)

# close entire browser
driver.quit()


# # Wait for element to load 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# try:
#     element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH,"")))
# finally:
#     driver.quit()



# close current tab
# driver.close()
