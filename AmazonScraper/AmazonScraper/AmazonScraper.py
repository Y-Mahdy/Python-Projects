from selenium import webdriver
import time
from collections import OrderedDict
import datetime
import os
def download(driver, target_path):
    """Download the currently displayed page to target_path."""
    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})

    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    # set page format
    # inside the execution script, webpage is "this"
    page_format = 'this.paperSize = {format: "A4", orientation: "portrait" };'
    execute(page_format, [])

    # render current page
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [])

browser = webdriver.PhantomJS('phantomjs')
url = 'https://www.amazon.com/gp/css/order-history?ie=UTF8&ref_=nav_nav_orders_first&'
browser.get(url)
with open('amazon-pass.txt', 'r') as fPass:
    txtpass = fPass.readline()
with open('amazon-user.txt', 'r') as fUser:
    txtuser = fUser.readline()
with open('US-pass.txt', 'r') as famazonPass:
    txtUSpass = famazonPass.readline()
with open('US-user.txt', 'r') as famazonUser:
    txtUSuser = famazonUser.readline()
browser.find_element_by_xpath('//input[@type="email"]').send_keys(txtuser)
try:
   browser.find_element_by_xpath('//input[@type="password"]').send_keys(txtpass)
except:
   browser.find_element_by_xpath('//input[@id = "continue"]').click()
   browser.find_element_by_xpath('//input[@type="password"]').send_keys(txtpass)
browser.find_element_by_xpath('//input[@id="signInSubmit"]').click()
#browser.get('file:///E:/Jobs/Menna%20-%20Mamdoh%20Kwait/Your%20Orders.html')
all_orders = browser.find_elements_by_xpath('//div[@class = "a-box-group a-spacing-base order"]//div//div//div//div[@class="a-row a-size-base"]//ul//a')
for order in all_orders: 
    OrderLink = 'https://www.amazon.com' + order.get_attribute("href")
    browser.get(OrderLink)
    #browser.get('file:///E:/Jobs/Menna%20-%20Mamdoh%20Kwait/Amazon.com%20-%20Order%20113-1746843-3631450.html')
    MerchantsName = browser.find_element_by_xpath('//span[@class = "a-size-small a-color-secondary"]//a').text.split('seller profile')
    MerchantName = MerchantsName[0]
    InvoiceNumber = OrderLink.split('orderID=')[1]
    PDFName = InvoiceNumber + '.pdf'
    all_Buttons = browser.find_elements_by_xpath('//a[@role = "button"]')
    for button in all_Buttons:
        if 'View or Print invoice' in button.text:
          browser.get('https://www.amazon.com' + button.get_attribute("href"))
          #browser.get('file:///E:/Jobs/Menna%20-%20Mamdoh%20Kwait/Order%20Details.html')
          download(browser, PDFName)
          break
    #browser.get('file:///E:/Jobs/Menna%20-%20Mamdoh%20Kwait/Amazon.com%20-%20Order%20113-1746843-3631450.html')
    all_TrachButtons = browser.find_elements_by_xpath('//a[@role = "button"]')
    for Trackbutton in all_TrachButtons:
        if 'Track package' in Trackbutton.text:
          browser.get('https://www.amazon.com' + Trackbutton.get_attribute("href"))
          #browser.get('file:///E:/Jobs/Menna%20-%20Mamdoh%20Kwait/Tracking.html')
          ShipmentTrackingNumber = browser.find_element_by_xpath('//span[@class="a-declarative"]//a[@data-ref="ref=pt2_detail_track_id_br"]').text.replace('Tracking ID ','')
          break
    browser.get('https://www.myus.com/')
    browser.find_element_by_xpath('//a[@class="link-signin"]').click()
    browser.find_element_by_xpath('//input[@id="UserName"]').send_keys(txtUSuser)
    browser.find_element_by_xpath('//input[@id="Password"]').send_keys(txtUSpass)
    try:
        browser.find_element_by_xpath('//div[@class="g-recaptcha"]').click()
        time.sleep(10)
    except:
        LogText = 'Captcha Problem'
    browser.find_element_by_xpath('//button[@class="btn-big wrap"]').click()
    browser.find_element_by_xpath('//input[@id="js-upload-file"]').send_keys(os.path.realpath(__file__).replace('Test.py',PDFName))
    browser.find_element_by_xpath('//input[@id="Merchant"]').send_keys(MerchantName)
    browser.find_element_by_xpath('//input[@id="TrackingNumber"]').send_keys(ShipmentTrackingNumber)
    browser.find_element_by_xpath('//input[@id="MasterOrderNumber"]').send_keys(InvoiceNumber)
    browser.find_element_by_xpath('//button[@class="btn-secondary"]').click()