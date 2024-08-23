from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="C:\\Users\\home\\Desktop\\EXTRA MEDIA\\setup\\Edge driver\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name ="Aai"
msg = "zaal ka j1"
count = 10
difference_in_two_messages_in_sec=4
first_msg_waiting_time=0

input("click after scan code")

user = driver.find_element_by_xpath(f"//span[@title='{name}']")
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

time.sleep(first_msg_waiting_time)
for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
    time.sleep(difference_in_two_messages_in_sec)