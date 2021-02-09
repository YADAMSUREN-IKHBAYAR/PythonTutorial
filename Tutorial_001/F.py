from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument('--disable-gpu')

option.add_argument('--proxy-server="direct://"')
option.add_argument('--proxy-bypass-list=*')

option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')

# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")
# option.add_argument("--disable-notifications")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

PATH=r"C:\MY_WORK_ENVIRONMENTS\001_SOURCE\github.com\Python\PythonTutorial\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=option)  

driver.get("https://www.facebook.com/tbayarkhuu/videos/637736603478010")

inputElement = driver.find_element_by_id("email")
inputElement.send_keys('ikhee.mn@gmail.com')

inputElement = driver.find_element_by_id("pass")
inputElement.send_keys('ikhee030117')

driver.find_element_by_id("loginbutton").click()





# for element in driver.find_elements_by_css_selector('span'):
#     element.click()


time.sleep(500)


