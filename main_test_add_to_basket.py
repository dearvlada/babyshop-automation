from seleniumbase import BaseCase

class NavigationTest(BaseCase):

    # base url and vocabulary
    def setup_class(self):
        self.base_url = "https://www.babyshop.com/"
        self.menu_dict = {"Brands": ['//a[@data-class="brand"]', self.base_url + "/brands/s/618"],
                          "Сlothing": ['//a[@data-class="babyclothes"]', self.base_url + "/clothing/s/619"]
                          }

    def test_add_to_basket_proceed_to_checkout_and_remove(self):
        # go to the goods page
        self.get(self.base_url + 'edushape/s/2003')
        # saving the name of 1st position
        item_name = self.get_text('//article[1]/div[@class="card__content"]/h3/a/strong')
        # click on the 1st position
        self.click('//article[1]')
        # add to cart
        self.click('//button[@class="product-form__btn btn"]')
        # checkout
        self.click('//a[@class="btn product-form__btn--go-to-cart"]')
        # saving the name in the basket
        basket_name = self.get_text('//div[2]/a[1]/span[2]')
        # names should be matching
        self.assert_equal(item_name,basket_name)
        # delete the position
        self.click('//a[2]/span')
        self.sleep(1)
        # getting the message that cart is empty
        empty_text = self.get_text('//div/header/h1')
        # text sould be matching
        self.sleep(1)
        self.assert_equal(empty_text, "Your cart is empty")
        self.sleep(1)
