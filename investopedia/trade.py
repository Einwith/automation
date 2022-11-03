#trade button


from selenium import webdriver


class Trade():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver")

    def clickTradeButton(self): #click trade button on current page
        self.driver.get('https://www.investopedia.com/simulator/portfolio')
        trade = self.driver.find_element("xpath", '//*[@id="app"]/div/main/div/div[2]/a[2]/span')
        trade.click()

    def openTradePage(self): #open new trade page
        self.driver.get('https://www.investopedia.com/simulator/portfolio')
        trade = self.driver.find_element("xpath", '//*[@id="app"]/div/main/div/div[2]/a[2]/span')
        trade.click()