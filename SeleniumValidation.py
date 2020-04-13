from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Ing Juan\Desktop\Selenium\chromedriver\chromedriver.exe")
driver.get("http://python.org")
driver.close()

