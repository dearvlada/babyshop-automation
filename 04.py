def test_find_items(self):
    self.get(self.base_url)
    # send_keys - это печать текста в поле (отправка клавиш)
    self.send_keys('//*[@id="search-form"]/input', "Sirona S i-Size Car Seat")
    # клик на кнопке поиска
    self.click('//*[@id="search-form"]/button')
    # получаем  все элементы по заданному х-пазу и считаем длинну списка
    count = len(self.find_elements("//article"))
    # сверяем длину и ожидаемый результат
    self.assert_equal(count, 5)
    # пример, как можно задать паузу
    self.sleep(2)