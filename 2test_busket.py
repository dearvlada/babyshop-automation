from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

class NavigationTest(BaseCase):

    # задаем базовый урл и переменную-словарь
    def setup_class(self):
        self.base_url = "https://www.babyshop.com/"
        self.menu_dict = {"Brands": ['//a[@data-class="brand"]', self.base_url + "/brands/s/618"],
                          "Сlothing": ['//a[@data-class="babyclothes"]', self.base_url + "/clothing/s/619"]
                          }

    def test_basket(self):
        # go to the goods page 123456
        self.get(self.base_url + 'edushape/s/2003')
        # click on the 1st position
        self.click('//article[1]')
        #fmdhgfhdkh
        self.sleep(3)
