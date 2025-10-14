from selenium import webdriver

driver= webdriver.Chrome()

driver.get("https://freelancer.com.br/")

driver.maximize_window()

driver.quit()