import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#Открыть сайт и залогиниться
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("info2020prv@yandex.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
#Открыть форму паспорта
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
#Заполнение формы
#ФИО
driver.find_element(By.ID, "surname").send_keys("Нефедова")
driver.find_element(By.ID, "name").send_keys("Маруся")
driver.find_element(By.ID, "patronymic").send_keys("Николаевна")
#Дата рождения
driver.find_element(By.NAME, "date").click()
driver.find_element(By.XPATH, '//*[@id="birthday"]/div/input').send_keys('22.11.2001')
driver.find_element(By.XPATH, '//*[@id="birthday"]/div/input').send_keys(Keys.ENTER)
#Серия паспорта
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("1234")
#Номер паспорта
driver.find_element(By.ID, "passportNumber").click()
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("567899")
#Дата выдачи
driver.find_element(By.NAME, "date").click()
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys('01.12.2021')
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys(Keys.ENTER)
#Код подразделения
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("160000")
#СНИЛС
driver.find_element(By.ID, "cardId").click()
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("12345678910")
#Кем выдан
driver.find_element(By.ID, "issued").click()
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("МВД по РТ")
#Адрес
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Казань ул Некрасова д 19 кв 3")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ENTER)
#Проскроллить
driver.execute_script("window.scrollTo(0, 450)")
time.sleep(1)
#Телефон
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("9170000000")
"""
Checkbox
driver.find_element(By.ID, "privacy").click()
"""
#Прикрепить и отправить
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
time.sleep(1)
img_input.send_keys("C:/Users/Mak/PycharmProjects/pythonProject/img/1.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.btn.fill").click()
#Диплом
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".active .document-tile:nth-child(2)").click()
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("C:/Users/Mak/PycharmProjects/pythonProject/img/2.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.btn.fill").click()
#Договор
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(3) .document-tile:nth-child(1)").click()
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("C:/Users/Mak/PycharmProjects/pythonProject/img/договор.pdf")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.btn.fill").click()
#Заявление
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(3) .document-tile:nth-child(2)").click()
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("C:/Users/Mak/PycharmProjects/pythonProject/img/заявление.pdf")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.btn.fill").click()
#Согласие
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(3) .document-tile:nth-child(3)").click()
img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("C:/Users/Mak/PycharmProjects/pythonProject/img/согласие.pdf")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.btn.fill").click()
driver.close
time.sleep(1)
#Открыть админку и залогиниться
driver.get("https://adminqa.neapro.site/login ")
driver.maximize_window()
driver.find_element(By.ID, "admin_email").send_keys("moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
driver.find_element(By.NAME, "commit").click()
#Зайти в учетку
driver.find_element(By.LINK_TEXT, "Студенты").click()
driver.find_element(By.LINK_TEXT, "Документы").click()
sidebar = driver.find_element(By.ID, 'sidebar')
driver.execute_script("arguments[0].setAttribute('style', 'right: 0px; position: absolute;')", sidebar)
driver.find_element(By.XPATH, '//*[@id="q_user_id_input"]/span/span[1]/span').click()
sidebar_user = driver.find_element(By.CLASS_NAME, 'select2-search__field')
sidebar_user.send_keys('info2020prv@yandex.ru')
time.sleep(2)
sidebar_user.send_keys(Keys.ARROW_DOWN)
sidebar_user.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="new_q"]/div[6]/input[1]').click()
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, 'index_as_table')))
time.sleep(2)
#Подтвердить документы
elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
    elements[0].click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(2)
elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
    elements[0].click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(2)
elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
    elements[0].click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(2)
    elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
     elements[0].click()
     driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
     driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
     time.sleep(2)
     elements = driver.find_elements(By.XPATH, '//span[contains(text(),"Ожидание")]')
if elements and elements[0].is_displayed():
    elements[0].click()
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
    driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
    time.sleep(1)
#Выход из админки
driver.find_element(By.ID, "logout").click()
time.sleep(1)
#Разлогиниться
driver.get("https://qa.neapro.site/cabinet/documents/")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div[1]/a').click()

WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'logout_name')))
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'logout_name').click()
time.sleep(1)
driver.close()