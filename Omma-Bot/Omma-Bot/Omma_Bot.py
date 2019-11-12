import PyPDF2
import time
from collections import OrderedDict
import datetime
import os
import urllib
import selenium
from selenium import webdriver
import sys
import re
import solveCaptcha
from selenium import webdriver
myKey = '0e2e0f8685cb63d6269ba8cf4b398048'
options = webdriver.ChromeOptions() 
path = 'Users\\Mennatullah Sobhy\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
options.add_argument("user-data-dir=C:\\"+path+"") #Path to your chrome profile
webDriver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
def SolveCaptcha(webDriver):
    dataKey = webDriver.find_element_by_xpath('//iframe').get_attribute("src").split('&k=', '&co')[0]
    postUrl = 'https://2captcha.com/in.php?key=' + myKey + '&method=userrecaptcha&googlekey=' + dataKey + '&pageurl=' + webDriver.current_url
    windows_before  = driver.current_window_handle
    driver.execute_script("window.open( " + url + " )")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows_after = driver.window_handles
    txtResponseID = webDriver.find_element_by_tag_name('body').text
    time.sleep(10)
    responseURL = 'https://2captcha.com/res.php?key='+myKey +'&action=get&id=' + txtResponseID
    while True:
        webDriver.get(responseURL)
        if webDriver.find_element_by_tag_name('body') == 'CAPCHA_NOT_READY':
            pass
        else:
            break
    TOKEN_FROM_2CAPTCHA = webDriver.find_element_by_tag_name('body')
    webDriver.find_element_by_xpath('//textarea[@class = "g-recaptcha-response"]').innerHTML = TOKEN_FROM_2CAPTCHA;
def LoadFn():
    while True:
        try:
            #waiting to load the page
            Load = webDriver.find_element_by_xpath('//body').text
            if not 'Loading, please wait' in Load:
                break
            else:
                pass
        except:
            pass
ChoosenStep = input(" Step(1): Create new user accounts\n Step(2): Login and create new patient application\n Step(3): Login and view status of existing patient application\n Step(4): Update accessibility records\n Choose your Step: ") 
if ChoosenStep == '1':
    #Step(1): Create new user accounts
    #webDriver = webdriver.Chrome()
    #webDriver.maximize_window()
    dCheckForNew = True
    nItemCount = 0
    while dCheckForNew == True:
        #Check for new Patients
        nItemCount = nItemCount + 1
        firstname = 'Mennatullah'
        lastname = 'Sobhy'
        email = 'mennatullah.sobhy.88@gmail.com'
        phonenumber = '0232223333'
        password = 'PWD@1234q'
        DOB = '12121988'
        webDriver.get('https://ok-public.mycomplia.com/#!/ok/register')
        while True:
            try:
                #waiting to load the page
                Load = webDriver.find_element_by_xpath('//body').text
                if not 'Loading, please wait' in Load:
                    break
                else:
                    pass
            except:
                pass
        webDriver.find_element_by_name('firstName').clear()
        webDriver.find_element_by_name('firstName').send_keys(firstname)
        webDriver.find_element_by_name('lastName').clear()
        webDriver.find_element_by_name('lastName').send_keys(lastname)
        webDriver.find_element_by_name('email').clear()
        webDriver.find_element_by_name('email').send_keys(email)
        webDriver.find_element_by_name('confirmEmail').clear()
        webDriver.find_element_by_name('confirmEmail').send_keys(email)
        webDriver.find_element_by_name('phoneNumber').clear()
        webDriver.find_element_by_name('phoneNumber').send_keys(phonenumber)
        webDriver.find_element_by_xpath('//md-select').click()
        webDriver.find_element_by_id('select_option_9').click()
        webDriver.find_element_by_xpath('//input[@placeholder = "Date of Birth"]').send_keys(DOB)
        time.sleep(3)
        webDriver.find_element_by_xpath('//input[@placeholder = "Confirm Date of Birth"]').send_keys(DOB)
        time.sleep(2)
        webDriver.find_element_by_name('password').clear()
        webDriver.find_element_by_name('password').send_keys(password)
        webDriver.find_element_by_name('reenterPassword').clear()
        webDriver.find_element_by_name('reenterPassword').send_keys(password)
        time.sleep(2)
        webDriver.find_element_by_xpath('//div[@class = "md-container md-ink-ripple"]').click()
        print('Please pass CAPTCHA .. ')
        while True:
            try:
                webDriver.find_element_by_xpath('//div[@class = "recaptcha-checkbox-checkmark"]')
                break
            except:
                time.sleep(10)
        print('Account has been created for Patient # ' + str(nItemCount))
elif ChoosenStep == '2':
    #Step(2): Login and create new patient application
    #email = 'youssef.mohammed.mahdy@gmail.com'
    email = 'mennatullah.sobhy.88@gmail.com'
    password = 'PWD@1234q'
    firstname = 'Mennatullah'
    middlename = 'Sobhy'
    lastname = 'Kamal'
    Suffix = ''
    eighteenPlus = 'Yes'
    phonenumber = '0232223333'
    password = 'PWD@1234q'
    country = ''
    DOB = '12121988'
    DocumentType = ''
    DocumentID = ''
    DocumentDate = ''
    physicalAddressZip4 = ''
    physicalAddressZipCode = ''
    physicalAddressStreet = ''
    physicalAddressUnitNoAptNo = ''
    physicalAddressCity = ''
    county = ''
    state = ''
    mailingAddressStreet = ''
    mailingAddressUnitNoAptNo = ''
    mailingAddressCity = ''
    Mapcounty = ''
    Mapstate = ''
    mailingAddressZipCode = ''
    mailingAddressZip4 = ''
    #Go to the page of Signing In
    webDriver.get('https://ok-public.mycomplia.com/#!/signin')
    #Wait the page the load
    LoadFn()
    while True:
        try:
            #Check if the page is loaded perfectly or not
            webDriver.find_element_by_xpath('//input[@id = "username"]').send_keys(email)
            break
        except:
            if 'Your connection was interrupted' in webDriver.find_element_by_xpath('//body').text:
                webDriver.get('https://ok-public.mycomplia.com/#!/signin')
            else:
                pass
    webDriver.find_element_by_xpath('//input[@id = "password"]').send_keys(password)
    print('Please pass CAPTCHA .. ')
    #while True:
        #   try:
        #      webDriver.find_element_by_xpath('//div[@class = "recaptcha-checkbox-checkmark"]')
        #     break
        #except:
            #   time.sleep(10)
    webDriver.find_element_by_xpath('//button[@class = "md-raised md-primary md-button md-ink-ripple"]').click()
    while True:
        st = webDriver.current_url
        if st == 'https://ok-public.mycomplia.com/#!/licenses':
            break
        else:
            pass
    try:
        webDriver.find_element_by_xpath('//md-dialog')
        webDriver.find_element_by_xpath('//div[@class = "md-ripple-container"]').click()
        webDriver.find_element_by_xpath('//div[@class = "md-ripple-container"]').click()
    except:
        pass
    webDriver.find_element_by_xpath('//button[@aria-label = "Create New Application"]').click()
    webDriver.find_element_by_xpath('//md-radio-button[@aria-label="New Patient Registration"]').click()
    webDriver.find_element_by_xpath('//button[@class="md-raised md-primary md-button md-ink-ripple md-default-theme"]').click()
    while True:
        try:
            webDriver.find_element_by_xpath('//input[@name="genInfoFirstName"]')
            break
        except:
            pass
        webDriver.find_element_by_xpath('//input[@name="genInfoFirstName"]').send_keys(firstname)
        webDriver.find_element_by_xpath('//input[@name="genInfoMiddleName"]').send_keys(middlename)
        webDriver.find_element_by_xpath('//input[@name="genInfoLastName"]').send_keys(lastname)
        if '.' in Suffix:
            Suffix.replace('.','')
        webDriver.find_element_by_xpath('//md-option[@value="'+Suffix.lower()+'"]').click()
        webDriver.find_element_by_xpath('//md-radio-button[@value="Yes"]').click()
        webDriver.find_element_by_xpath('//input[@name="genInfoPhone"]').send_keys(phonenumber)
        webDriver.find_element_by_xpath('//md-option[@value="USA"]').click()
        webDriver.find_element_by_xpath('//input[@class="md-datepicker-input ng-pristine ng-untouched ng-valid ng-not-empty ng-valid-mask"]').send_keys(DOB)
        webDriver.find_element_by_xpath('//md-option[@value="permanentPatientLicense"]').click()
        Type = DocumentType.split(' ')[0].lower + DocumentType.split(' ')[1]
        webDriver.find_element_by_xpath('//md-option[ @value = "' + Type + '" ]').click()
        webDriver.find_element_by_xpath('//input[@name="genInfoIdNumber"]').send_keys(DocumentID)
        webDriver.find_element_by_xpath('//input[@class="md-datepicker-input ng-pristine ng-valid ng-empty ng-valid-mask ng-touched"]').send_keys(DocumentDate)
        webDriver.find_element_by_xpath('//button[@class = "md-raised md-primary black-icon mobile-50 md-button ng-scope md-ink-ripple"]')
        time.sleep(2)
        while True:
            try:
                webDriver.find_element_by_xpath('//input[@name = "physicalAddressStreet"]')
            except:
                pass
        webDriver.find_element_by_xpath('//input[@name = "physicalAddressStreet"]').send_keys(physicalAddressStreet)
        webDriver.find_element_by_xpath('//input[@name = "physicalAddressUnitNoAptNo"]').send_keys(physicalAddressUnitNoAptNo)
        webDriver.find_element_by_xpath('//input[@name = "physicalAddressCity"]').send_keys(physicalAddressCity )        
        webDriver.find_element_by_xpath('//md-option[ @value = "' + county + '" ]').click()
        webDriver.find_element_by_xpath('//md-option[ @value = "' + state + '" ]').click()
        webDriver.find_element_by_xpath('//input[@name = "physicalAddressZipCode"]').send_keys(physicalAddressZipCode )        
        webDriver.find_element_by_xpath('//inputp[@name = "physicalAddressZip4"]').send_keys(physicalAddressZip4)
        nVerifyButton = 0
        #verify the address
        for element in webDriver.find_elements_by_xpath('//button[@class = "md-raised md-primary white-icon md-button field-button"]'):
            if element.text.strip() == 'Verify Address':
                nVerifyButton = nVerifyButton + 1
                element.click()
                break
        if (physicalAddressStreet == mailingAddressStreet and physicalAddressUnitNoAptNo == mailingAddressUnitNoAptNo and  physicalAddressCity == mailingAddressCity):
            for element in webDriver.find_elements_by_xpath('//button[@class = "md-raised md-primary white-icon md-button field-button"]'):
                if element.text.strip() == 'Copy from Street Address':
                    element.click()
                    break
        else:
            while True:
                
                webDriver.find_element_by_xpath('//input[@name = "mailingAddressStreet"]').send_keys(mailingAddressStreet)
                webDriver.find_element_by_xpath('//input[@name = "mailingAddressUnitNoAptNo"]').send_keys(mailingAddressUnitNoAptNo)
                webDriver.find_element_by_xpath('//input[@name = "mailingAddressCity"]').send_keys(mailingAddressCity )        
                webDriver.find_element_by_xpath('//md-option[ @value = "' + Mapcounty + '" ]').click()
                webDriver.find_element_by_xpath('//md-option[ @value = "' + Mapstate + '" ]').click()
                webDriver.find_element_by_xpath('//input[@name = "mailingAddressZipCode"]').send_keys(mailingAddressZipCode )        
                webDriver.find_element_by_xpath('//inputp[@name = "mailingAddressZip4"]').send_keys(mailingAddressZip4)
                for element in webDriver.find_elements_by_xpath('//button[@class = "md-raised md-primary white-icon md-button field-button"]'):
                    if element.text.strip() == 'Verify Address':
                        nVerifyButton = nVerifyButton + 1
                        if nVerifyButton == 2:
                            element.click()
                            break
        webDriver.find_element_by_xpath('//button[@class = "md-raised md-primary black-icon mobile-50 md-button ng-scope md-ink-ripple"]')
        time.sleep(2)
        while True:
            try:
                webDriver.find_element_by_xpath('//input[@name = "physicalAddressStreet"]')
            except:
                pass
elif ChoosenStep == '3':
    #Step(3): Login and view status of existing patient application
    print('')
elif ChoosenStep == '4':
    #Step(4): Update accessibility records
    print('')
