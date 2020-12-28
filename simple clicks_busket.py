from seleniumbase import BaseCase

class NavigationTest(BaseCase):

    # задаем базовый урл и переменную-словарь
    def setup_class(self):
        self.base_url = "https://www.babyshop.com/"
        self.menu_dict = {"Brands": ['//a[@data-class="brand"]', self.base_url + "/brands/s/618"],
                          "Сlothing": ['//a[@data-class="babyclothes"]', self.base_url + "/clothing/s/619"]
                          }

    def test_basket(self):
        # go to the goods page
        self.get(self.base_url + 'edushape/s/2003')
        # hover and click on the 1st position

        self.sleep(3)
