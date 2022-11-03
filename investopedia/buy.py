from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import math
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium_stealth import stealth




class Investopedia:
    def __init__(self):
        # options = Options()
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        # options.add_argument('user-agent={0}'.format(user_agent))
        # chrome_options = webdriver.ChromeOptions();
        # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        # driver = webdriver.Chrome(options=chrome_options);
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # caps = options.to_capabilities()
        # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
        #                           desired_capabilities=caps)
        self.driver1 = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver", options=options)
        self.driver2 = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver", options=options)

        self.driver2.get('https://money.usnews.com/investing/stocks/rankings')
        self.USNewsLinkList = []
        elementList = self.driver2.find_elements(By.CSS_SELECTOR, '.sector-lists__SectorBlock-sc-1fjbxx2-1 a')
        for e in elementList:
            self.USNewsLinkList.append(e.get_attribute('href'))
        self.driver2.delete_all_cookies()

    def buy(self, stockAbbr):
        trade = self.driver1.find_element("xpath", '//*[@id="app"]/div/main/div/div[2]/a[2]/span')
        trade.click()

        symbol = self.driver1.find_element(By.CSS_SELECTOR, '[placeholder="Look up Symbol/Company Name"]')
        symbol.click()
        symbol.send_keys(stockAbbr)
        suggestion = self.driver1.find_element(By.CSS_SELECTOR, ".d-flex > .symbol-name")
        suggestion.click()

        price = (self.driver1.find_element(By.CSS_SELECTOR, ".tv-symbol-price-quote__value .js-symbol-last")).text
        priceAssert = price
        priceAssert = priceAssert.replace('.', '1').isdigit()
        if priceAssert != True:
            raise Exception("line 22, price is not a number: " + price)
        price = int(price)
        cash = (self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="cash"]')).text
        cash = cash.replace(',', '')
        cash = int((self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="cash"]')).text) - 90000

        if price < 500 < cash:
            quantityBuy = int(500 / price)

        quantity = self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="quantity-input"]')
        quantity.click()
        quantity.send_keys(str(quantityBuy))

        preview = self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="preview-button"]')
        preview.click()

        submitOrder = self.driver1.find_element(By.CSS_SELECTOR, 'data-cy="submit-order-button"')
        submitOrder.click()

    def sell(self, sellButtonSelector):
        sellButtonClick = self.driver1.find_element(By.CSS_SELECTOR, sellButtonSelector).click()

        showMax = self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="quantity-button"]')
        showMax.click()

        preview = self.driver1.find_element(By.CSS_SELECTOR, '[data-cy="preview-button"]')
        preview.click()

        submitOrder = self.driver1.find_element(By.CSS_SELECTOR, 'data-cy="submit-order-button"')
        submitOrder.click()

    def monitor(self, sellButtonSelector):
        time.sleep(600)
        portfolio = self.driver1.find_element("xpath", '//*[@id="app"]/div/main/div/div[2]/a[1]/span')
        portfolio.click()
        holdingsTable = self.driver1.find_element(By.CSS_SELECTOR, '.holdings-table table')
        rows = holdingsTable.find_elements(By.CSS_SELECTOR, 'tr')
        for row in rows:
            row.click()
            rowInfo = self.driver.find_element(locate_with(By.TAG_NAME, "tr").below(row))
            todaysChange = rowInfo.find_element(By.CSS_SELECTOR,
                                                '[data-cy="expanded-row-day-gain-dollar"] div').text.strip()
            todaysChange = todaysChange[todaysChange.rfind('(')+1:-2]
            totalGainLoss = rowInfo.find_element(By.CSS_SELECTOR,
                                                 '[data-cy="expanded-row-total-gain-dollar"] div').text.strip()
            totalGainLoss = totalGainLoss[totalGainLoss.rfind('(') + 1:-2]
            math.isclose(0.1 + 0.2, 0.3)
            if todaysChange <= -4.00 or totalGainLoss <= -4.00:
                self.sell('[data-cy="expanded-row-sell-action"]')
                time.sleep(600)
                self.buy(self.pickStock())
                time.sleep(600)




    def pickStock(self):
        stockPicked = False
        while not stockPicked:
            index = random.randint(0, len(self.USNewsLinkList) - 1)

            self.driver2.get(self.USNewsLinkList[index])
            print(self.USNewsLinkList[index])
            trend = self.driver2.find_element("xpath",
                                             '//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/div[2]/div/div[3]/span[1]')
            trend = trend.find_element(By.CSS_SELECTOR, 'title').get_attribute('id')

            if trend == 'gallery-arrow-Upward-trend--90':
                self.buy(self.driver2.find_element("xpath",
                                                  '//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/a/p/span').text)
                stockPicked = True
            self.driver2.delete_all_cookies()

    def initialBuy(self):
        self.driver1.get('https://www.investopedia.com/simulator/trade/stocks')
        self.login()
        for x in range(1):   #20
            self.pickStock()

    def initializedList(self):
        self.USNewsLinkList = self.driver.find_elements(By.CSS_SELECTOR, '.sector-lists__SectorBlock-sc-1fjbxx2-1 a')

    def login(self):
        time.sleep(10)
        email = self.driver1.find_element("xpath", '//*[@id="username"]')
        email.click()
        time.sleep(2)
        email.send_keys('prank1363246@gmail.com')
        pw = self.driver1.find_element("xpath", '//*[@id="password"]')
        time.sleep(2)
        pw.click()
        time.sleep(2)
        pw.send_keys('?*8$e768W2)d_?,')
        time.sleep(2)
        loginBtn = self.driver1.find_element("xpath", '//*[@id="login"]')
        loginBtn.click()

    def runProgram(self):
        # self.driver1.get('https://www.investopedia.com/simulator/trade/stocks')
        # self.login()
        self.initialBuy()
        while True:
            self.monitor()






bot = Investopedia()

bot.initialBuy()




#monitor the app 10 minutes after the buy/sell
#monitor only during business hours, start monitoring at 10:30am, stop monitoring at 5pm
#prank1363246@gmail.com
#?*8$e768W2)d_?,