
from PageObjects.Login_Page import Login_page

class Test_001_Login:
    baseURL = "https://developmentwow.wedmegood.com/login?referrer=/hyderabad-wedding&whatsappClicked=0"
    username = "test123@gmail.com"
    password = "1234567"

    def test_HomePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        self.driver.close()
        if act_title == "Weddings, Indian Wedding Planning Online - WedMeGood":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp= Login_page(self.driver)
        self.lp.user_name(self.username)
        self.lp.click_continue()
        self.lp.password(self.password)
        self.lp.click_signin()
        self.driver.close()