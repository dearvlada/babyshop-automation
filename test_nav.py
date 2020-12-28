from seleniumbase import BaseCase


class NavigationTest(BaseCase):

    def test_site_open(self):
        # Откроем сайт
        self.open('https://www.babyshop.com')
