from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh gpro0wi8 dwo3fsh8 ow4ym5g4 auili1gw du4w35lb gmql0nx0']//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi knj5qynh m9osqain']"))).click()
# driver.find_element_by_xpath("//span[contains(@class,'d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain')]").click()
# driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain']").click()


# for element in driver.find_elements_by_css_selector('span'):
#     element.click()

while True:
    try:
        meci = driver.find_elements_by_class_name('oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr')

        # for items in meci:
        #     title = items.text
        #     href = items.get_attribute('href')
        #     print(title)
        #     print(href)

        # time.sleep(3)
        # driver.find_element_by_css_selector('.next').click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr']//span[@class='j83agx80 fv0vnmcu hpfvmrgz']//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']"))).click()

        # time.sleep(3)
    except:
        break

time.sleep(10)


