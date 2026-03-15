from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

website = "https://gnn.gamer.com.tw/index.php?k=5"
path = "/home/on99/Downloads/chromedriver-linux64/chromedriver"

options = Options()
options.binary_location = "/usr/bin/brave-browser"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

#to find the element using xpath
#driver.find_elements(by="xpath", value='//h1[@class="GN-lbox2D"]/a')