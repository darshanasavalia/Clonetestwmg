
from selenium.webdriver.common.by import By
import time


class Login_page():
    text_username_xpath = "//input[@id='email-phone-field']"
    button_continue_xpath = "//button[normalize-space()='Continue']"
    text_password_xpath = "//input[@placeholder='Enter password']"
    button_signin_xpath = "//button[normalize-space()='Sign In']"
    button_logout_xpath = "//div[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def user_name(self,username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)
        time.sleep(3)

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.button_continue_xpath).click()
        time.sleep(2)
        print("click continue")

    def password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)
        time.sleep(2)
        print("click password")

    def click_signin(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()
        time.sleep(2)
        print("click signin")

        # driver= webdriver.Chrome()
        # #URL
        # driver.get('https://developmentwow.wedmegood.com/')
        # driver.maximize_window()
        # time.sleep(3)
        # driver.find_element(By.XPATH,"//span[@id='login-btn']").click()
        # time.sleep(3)
        # # userid
        # driver.find_element(By.XPATH,"//input[@id='email-phone-field']").send_keys("test123@gmail.com")
        # time.sleep(3)
        # #continue
        # driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()
        # time.sleep(3)
        # # password
        # driver.find_element(By.XPATH,"//input[@placeholder='Enter password']").send_keys("1234567")
        # #sign in button click
        # driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
        # time.sleep(3)