from seleniumbase import BaseCase

class NavigationTest(BaseCase):

    # base url and vocabulary
    def setup_class(self):
        self.base_url = "https://www.babyshop.com/"

    def test01_site_open(self):
        # open the site
        self.get("https://www.babyshop.com")
        # click on the main menu
        self.click('//div[@class="navigation__item"][3]')
        # getting current url and variable curr_url
        curr_url = self.get_current_url()
        # checking expected and actual url
        self.assert_equal(curr_url, 'https://www.babyshop.com/clothing/s/619')


    def test02_find_item_through_the_search_box(self):
        self.get(self.base_url)
        # send_keys - writing the text into the search box
        self.send_keys('//*[@id="instant-search__input"]', "Sirona S i-Size Car Seat")
        # click on the button "search"
        self.click('//*[@id="instant-search"]/div[1]/button')
        self.sleep(2)
        # getting and counting the elements
        article_elements = self.find_visible_elements('//article')
        # checking expected and actual results
        self.assert_equal(6, len(article_elements), 'Should show 6 baby seats')


    def test03_add_to_basket_proceed_to_checkout_and_remove(self):
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

    def test04_change_language(self):

        self.get(self.base_url + 'dolce-gabbana/s/1495')
        # getting text in Eng
        eng_text = self.get_text('//article[1]/div[2]/h3/a/strong')
        # go to the language switch
        self.click('//div[@class="header__links header-links"]/a[1]')
        # select "Russian"
        self.click('//a[@title="Russian"]')
        self.sleep(0.1)
        # going to the section in Ru
        self.get('https://ru.babyshop.com/dolce-gabbana/s/1495')
        # getting text in Ru
        ru_text = self.get_text('//article[1]/div[2]/h3/a/strong')
        # texts are not equal
        self.assert_not_equal(eng_text, ru_text)