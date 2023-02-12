from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()


class TestLogin:
    def test_login_with_LK(self,driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешен')


    def test_login_not_with_LK(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешен через личный кабинет')

    def test_login_with_register(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.LINK_TEXT, 'Войти').click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешен через регистрацию')

    def test_login_with_rebootPassword(self, driver):
        current_url = driver.current_url

        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        driver.find_element(By.LINK_TEXT, 'Войти').click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Вход успешен через восстановление пароля ')












