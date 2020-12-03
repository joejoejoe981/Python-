from selenium import webdriver

driver = webdriver.Chrome('/Users/wuzheyou/PycharmProjects/JOE/chromedriver')

driver.get('https://pokemondb.net/pokedex/national')

print(driver.page_source)

driver.quit()