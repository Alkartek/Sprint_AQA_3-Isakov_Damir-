from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistation:
    def test_current_registation(self, driver):
        current_url = driver.current_url
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH,
                            "//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "Alkartek")
        driver.find_element(By.XPATH,
                            "//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "alkartek5456788@gmail.com")
        driver.find_element(By.XPATH,
                            "//fieldset[3]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "5456788")
        driver.find_element(By.XPATH,
                            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        assert WebDriverWait(driver,500).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        print('')

        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.NAME, "name").send_keys("alkartek5456788@gmail.com")
        driver.find_element(By.NAME, "Пароль").send_keys("5456788")
        driver.find_element(
            By.XPATH,
            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
        ).click()
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        print('Проивзеден успешный вход в аккаунт')

    def test_regist_fail_with_bad_password(self, driver):
        current_url = driver.current_url
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH,
                            "//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "Alkartek")
        driver.find_element(By.XPATH,
                            "//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "alkartek5456788@gmail.com")
        driver.find_element(By.XPATH,
                            "//fieldset[3]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
            "1234")
        driver.find_element(By.XPATH,
                            ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        resul = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").text
        assert resul == 'Некорректный пароль'
        print(f'Ожидаемый результат выполнен: {resul}')