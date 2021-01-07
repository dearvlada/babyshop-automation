from seleniumbase import BaseCase

class NavigationTest(BaseCase):


    #launch the vocabulary and var
    def setup_class(self):
        self.base_url = "https://www.babyshop.com/"
        self.menu_dict = {"Brands":['//a[@data-class="brand"]', self.base_url+"/brands/s/618"],
                     "Сlothing":['//a[@data-class="babyclothes"]', self.base_url+"/clothing/s/619"]
            }

    def test_basket(self):
        #go to the goods page
        self.get(self.base_url+'dolce-gabbana/s/1495')
        #hover and click on the 1st position
        self.hover_and_click('//article[3]', '//article[3]//div[@class="quickshop-btn__holder"]')
        #choose size
        self.click('//article[3]//div[@class="quickshop-btn__holder"]')
        self.click('//div[@id="dropdown-list"]/ul/li[1]/a/label')
        #add to card
        self.click('//button[@class="product-form__btn btn"]')
        self.sleep(3)
