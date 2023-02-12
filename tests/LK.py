from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()

class TestLK:
    def test_swipe_to_lk(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        WebDriverWait(driver, 500).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешен')
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert WebDriverWait(driver, 500).until(EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        print('Соверешен переход в личный кабинет')

    def test_swipe_to_burger(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        WebDriverWait(driver, 500).until(EC.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешный')
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert WebDriverWait(driver, 500).until(
            EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        print('Произведен вход в личный кабинет')
        driver.find_element(By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2']")
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print("Проивзеден вход на главную страницу через эмблемму бургера")

    def test_choose_burger_ingridient(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        print('Выбран Элемент Соуса')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
        print('Элемент Начинки выбран')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()
        print('Элемент булки выбран')


