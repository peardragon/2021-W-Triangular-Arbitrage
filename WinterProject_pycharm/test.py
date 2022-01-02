from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "C:/Users/BaeJaeyong/anaconda3/" \
       "envs/winter_project_env/Scripts/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC")