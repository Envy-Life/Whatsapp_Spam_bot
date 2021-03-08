from selenium import webdriver
import yaml

info = yaml.load(open('spam.yml'))
url = info["whatsapp"]["url"]
spam_number = info["whatsapp"]["spam_number"]
driver = webdriver.Chrome()

driver.get(url)


driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
temp_1 = input("message : ")
for i in range(spam_number) :
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(temp_1)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
