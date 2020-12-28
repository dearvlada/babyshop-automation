from seleniumbase import BaseCase


class NavigationTest(BaseCase):

    def test_site_open(self):
        # Откроем сайт
        self.get("https://www.babyshop.com")
        # Кликаем на пункт в главном меню, селениум находит его по xpath
        self.click('//div[@class="navigation__item"][3]')
        # получаем текущий урл в переменную curr_url
        curr_url = self.get_current_url()
        # проверка соответствия полученного и ожидаемого урл
        self.assert_equal(curr_url, 'https://www.babyshop.com/clothing/s/619')

    def setup_class(self):
        self.base_url = "https://www.babyshop.com"

    def test_find_items(self):
        self.get(self.base_url)
        # send_keys - это печать текста в поле (отправка клавиш)
        self.send_keys('//*[@id="instant-search__input"]', "Sirona S i-Size Car Seat")
        # клик на кнопке поиска
        self.click('//*[@id="instant-search__input"]')
        self.sleep(2)
        # получаем  все элементы по заданному х-пазу и считаем длинну списка
        article_elements = self.find_visible_elements("//card__link")
        # сверяем длину и ожидаемый результат
        self.assert_equal(len(article_elements), 6)
        # пример, как можно задать паузу
        self.sleep(2)
