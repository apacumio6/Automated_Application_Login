# This script will log into a gym tracking application, navigate to
# several pages, toggle a drop down and log in as the lead coach for
# a specific class.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import calendar

import datetime

driver = webdriver.Chrome('..\drivers\chromedriver.exe')

# maximize window
driver.maximize_window()
time.sleep(2)

# driver.set_page_load_timeout(5)
driver.get("https://app.wodify.com/WodifyAdminTheme/LoginEntry.aspx?OriginalURL=&AllowAutoRedirect=True")
time.sleep(3)

# enter username
driver.find_element_by_id("wtLayoutLogin_SilkUIFramework_wt8_block_wtUsername_wtUsername_wtUserNameInput").send_keys("apacumio6@gmail.com")

# enter password
driver.find_element_by_id("wtLayoutLogin_SilkUIFramework_wt8_block_wtPassword_wtPassword_wtPasswordInput").send_keys("1390market")

# log in
driver.find_element_by_id("wtLayoutLogin_SilkUIFramework_wt8_block_wtAction_wtAction_wtLoginButton").send_keys(Keys.RETURN)
time.sleep(4)

# switch to athlete view
driver.get("https://app.wodify.com/WOD/WOD.aspx")
time.sleep(3)

# navigate to the 'Coachboard'
driver.get("https://app.wodify.com/Coachboard/CoachboardEntry.aspx")
time.sleep(3)

# expose the date field
driver.find_element_by_id("settingsCollapsibleHeader").click()
time.sleep(3)

# testing one day for now
coaching_days = ['02/13/2018']#, '02/01/2018']
# select the dates i'm coaching, the class time and sign in
# cal = calendar.Calendar()
# for x in cal.itermonthdates(2018,3):
#     if x.weekday() in [0,1,2,3,4]:
for x in coaching_days:
        work_date = x#.strftime('%m/%d/%y')
        # print(x.weekday())

        # clear the date
        driver.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_W_Utils_UI_wt86_block_wtDateInputFrom").clear()
        # driver.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_W_Utils_UI_wt86_block_wtDateInputFrom").click()
        # time.sleep(0.5)
        # driver.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_W_Utils_UI_wt86_block_wtDateInputFrom").send_keys(Keys.CONTROL+Keys.SHIFT+Keys.ARROW_LEFT+Keys.ARROW_LEFT+Keys.ARROW_LEFT)
        time.sleep(2)

        # enter new date
        driver.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_W_Utils_UI_wt86_block_wtDateInputFrom").send_keys(work_date)
        driver.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_W_Utils_UI_wt86_block_wtDateInputFrom").send_keys(Keys.RETURN)
        time.sleep(5)

        # select the correct class time
        driver.find_element_by_id("AthleteTheme_wtLayout_block_wtMainContent_wtClass_Input").click()
        driver.find_element_by_id("AthleteTheme_wtLayout_block_wtMainContent_wtClass_Input").send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(2)

        main_container = driver.find_element_by_xpath("/html/body/form[@id='WebForm1']/div[@id='AthleteTheme_wtLayout_block_wtMainContainer']")
        sign_in_popup = main_container.find_element_by_id("AthleteTheme_wtLayout_block_wtSubNavigation_Coachboard_UI_wtStaffSignIn_block_wtPayrollPositionClassUserTableRecords_ctl03_wtSignInEmployeeLink").click()
        time.sleep(2)
        # # main container of pop up
        # main_container_pop = driver.find_element_by_xpath("/html/body/form[@id='WebForm1']/table[@class='DocumentPopup']")
        # password_field = main_container_pop.find_element_by_id("AthleteTheme_wt12_block_wtMainContent_wtPasswordInputBox").send_keys("1390market", Keys.ENTER)

        # enter password
        actions = ActionChains(driver)
        actions.send_keys("1390market")
        actions.pause(1)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        # # driver.execute_script("window.open('https://app.wodify.com/Coachboard_UI/PasswordVerification_Popup.aspx?UserId=449118&amp;LocationId=698');")
        # time.sleep(3)
        #

        # # driver.find_element_by_id("AthleteTheme_wt12_block_wtMainContent_wtPasswordInputBox").send_keys("1390market")
        # # driver.find_element_by_id("AthleteTheme_wt12_block_wtMainContent_wtPasswordInputBox").click()
        # time.sleep(3)
        #
        # # close tab
        # driver.find_element_by_id("AthleteTheme_wt12_block_wtMainContent_wt14").click()