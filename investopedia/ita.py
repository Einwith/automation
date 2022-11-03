import mechanicalsoup
import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class API:
    def __init__(self, useName, passWord):
        self.browser2 = mechanicalsoup.Browser()
        #self.browser = mechanicalsoup.StatefulBrowser()
        #self.browser.open("https://www.howthemarketworks.com", verify=False)
        self.userLogin = False;
        self.useName = useName
        self.passWord = passWord
        self.USNewsLinkList = []


    def login(self):
        self.browser.open("https://www.howthemarketworks.com", verify=False)
        while (not self.userLogin):
            try:
                self.browser.open("https://www.howthemarketworks.com/login")
                self.browser.select_form('form[action="/login"]')
                # self.browser.get_current_form().print_summary()
                self.browser["UserName"] = self.useName
                self.browser["Password"] = self.passWord
                response = self.browser.submit_selected()
                self.userLogin = True;
            except mechanicalsoup.LinkNotFoundError:
                print("log in failed")
                self.userLogin = False;

    def marketStatus(self):
        self.browser.open("https://www.howthemarketworks.com", verify=False)
        if (self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            status = self.browser.get_current_page().find("p", class_="text-center")
            if (str(status.text) == "This contest has not started yet"):
                print("Market is openning")
            else:
                status = str(status.text).split('\n')[1].replace("...", "")
                print(status)
        else:
            print("you need to log in first")
            self.login()

    def buy(self, companyName, ammount):
        print('buy')
        self.browser.open("https://www.howthemarketworks.com", verify=False)
        if (self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            self.browser.select_form('form[action="/trading/placeorder"]')
            self.browser["OrderSide"] = 1
            self.browser["OrderType"] = 1
            self.browser["Symbol"] = companyName
            self.browser["Quantity"] = ammount
            self.browser.submit_selected()
        else:
            print("you need to log in first")
            self.login()

    def sell(self, companyName, ammount):
        self.browser.open("https://www.howthemarketworks.com", verify=False)
        if (self.userLogin):
            self.browser.open("https://www.howthemarketworks.com/trading/equities")
            self.browser.select_form('form[action="/trading/placeorder"]')
            self.browser["OrderSide"] = 2
            self.browser["OrderType"] = 1
            self.browser["Symbol"] = companyName
            self.browser["Quantity"] = ammount
            self.browser.submit_selected()
        else:
            print("you need to log in first")
            self.login()

    def getUSNewsList(self):
        print('getUSNewsList')
        self.browser2.get('https://money.usnews.com/investing/stocks/rankings')
        print('getUSNewsList')
        elementList = self.browser2.soup.select('.sector-lists__SectorBlock-sc-1fjbxx2-1 a')
        print('getUSNewsList')
        for e in elementList:
            print(e.get_attribute('href'))
            self.USNewsLinkList.append(e.get_attribute('href'))
        self.browser2.delete_all_cookies()

    def pickStock(self):
        print('pickStock')
        stockPicked = False
        while not stockPicked:
            index = random.randint(0, len(self.USNewsLinkList) - 1)
            self.browser2.get(self.USNewsLinkList[index])
            soup = self.browser.soup
            dom = etree.HTML(str(soup))
            price = str(dom.xpath('//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/div[2]/div/div[1]/span[1]'))
            price = price.replace('$', '')
            price = price.replace(',', '')
            price = float(price)

            trend = str(dom.xpath('//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/div[2]/div/div[3]/span[1]')[0]['id'])
            print(str(trend))
            # trend = self.driver2.find_element("xpath",
            #                                  '//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/div[2]/div/div[3]/span[1]')
            # trend = trend.find_element(By.CSS_SELECTOR, 'title').get_attribute('id')

            if str(trend) == 'gallery-arrow-Upward-trend--90':
                if price < 500 < getCash():
                    amount = int(500 / price)
                    self.buy(str(dom.xpath(
                        '//*[@id="app"]/article/div/div[5]/div[1]/div/div/div[2]/ol/li[1]/div/div[1]/a/p/span')[0]['id']))
                    stockPicked = True
            self.browser2.delete_all_cookies()

    def initialBuy(self):
        print('initialBuy')
        self.getUSNewsList()
        for x in range(1):   #20
            self.pickStock()

    def getCash(self):
        print('getCash')
        self.browser.open("https://www.howthemarketworks.com/profile", verify=False)
        cash = self.browser.get_current_page().select('#cashBalance')[0].text
        cash = cash.replace('Cash Balance: $', '')
        cash = cash.replace(',', '')
        return float(cash)


test = API("einwith", "m%jd4a@!Nk)aiPn")
#test.login()
test.getUSNewsList()
#print(test.getCash())
#test.trade("AMD", 200)

# browser.follow_link("https://www.howthemarketworks.com/trading/equities")


# print(response.text)
# browser.launch_browser()

# browser.get_current_form()


# browser.follow_link("login")
# browser.select_form('#login form')

# mainPage = browser.get_current_page


# message = browser.get_current_page().find("a", class_ ="account-links")
# browser["login"] = "justinphan3110@gmail.com"
# browser["password"] = "justinphan3110"
# reso = browser.submit_selected()


# page = browser.get_current_page()
# messages = page.find("h2", class_="shelf-title")
# if messages:
#     print(messages.text)
# assert page.select(".logout-form")
# print(page.title.text)