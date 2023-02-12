from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogOut:
    def test_logout(self, driver):
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
        print('Произведен вход в аккаунт')
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        #assert WebDriverWait(driver, 5).until(
            #EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        WebDriverWait(driver, 50)
        print('Соверешн переход в личный кабинет')

        driver.find_element(By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
        WebDriverWait(driver,50000)
        print("Соверешн выход из аккаунта")
