# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver

class Music():
    def __init__(self):
        self.d = 'a'
       # driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(executable_path=r"/Users/xb/Downloads/chromedriver")

    def play(self):
        print(self.d)
        name = input("enter a youtube channel name")
        self.driver.get('https://www.youtube.com/c/'+name+'/videos')
        new = self.driver.find_element("xpath", '//*[@id="items"]/ytd-grid-video-renderer[1]')
        new.click()

bot = Music()
bot.play()