from selenium import webdriver

class Login():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver")
    def log(self):
        self.driver.get('https://openlibrary.org/')
        site = self.driver.find_element("xpath", '//*[@id="header-bar"]/ul[2]/li[1]/a')
        site.click()

        email = self.driver.find_element("xpath", '// *[ @ id = "username"]')
        email.click()
        email.send_keys('prank1363246@yahoo.com')
        pw = self.driver.find_element("xpath", '// *[ @ id = "password"]')
        pw.click()
        pw.send_keys('1997zxc911')

        loginBtn = self.driver.find_element("xpath", '// *[ @ id = "register"] / div[5] / button')
        loginBtn.click()



bot = Login()
bot.log()
#prank1363246@yahoo.com
#1997zxc911
