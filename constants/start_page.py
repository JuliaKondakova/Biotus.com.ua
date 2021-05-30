"""Store locators and useful constants"""

# Links
START_PAGE_URL = 'https://biotus.com.ua//'

# Locators
USER_ICON_XPATH = '//a[@class="ajaxlogin-login"]'

#  Sign in locators
SIGN_IN_LOGIN_FIELD_XPATH = '//input[@name ="login[username]"]'
SIGN_IN_PASSWORD_FIELD_XPATH = '//input[@name ="login[password]"]'
SING_IN_BUTTON_XPATH = '//button[@class="button action login"]'
SIGN_IN_LOGIN_ERROR_TEXT = "Неверный логин или пароль."
SIGN_IN_LOGIN_ERROR_XPATH = f"//*[contains(text(), '{SIGN_IN_LOGIN_ERROR_TEXT}')]"

# Registration locators
REGISTRATION_BUTTON_XPATH = "//span[contains(text(),'Создать учётную запись')]"
# '//li[@data-role="collapsible" and @class="am-title"]'
SING_UP_FIRSTNAME_XPATH = '//input[@id="firstname" and @name="firstname"]'
SING_UP_LASTNAME_XPATH = '//input[@id="lastname" and @name="lastname"]'
SING_UP_EMAIL_XPATH = '//input[@id="username" and @title="Эл. почта или телефон"]'
SING_UP_PASSWORD_XPATH = '//input[@type="password" and @name="password"]'
SING_UP_PASSWORD_CONFIRMATION_XPATH = '//input[@type="password" and @name="password_confirmation"]'
SIGN_UP_BUTTON_XPATH = '//button[@type="button" and @class="button action save_user"]'

# My kabinet locators
MY_KABINET_XPATH = '//span[contains(text(), "Мой кабинет")]'
CONTROL_PANEL_XPATH = '//*[contains(text(), "Панель управления")]'
HELLO_MESSAGE_XPATH = '//p[@class="hello"]'
HELLO_MESSAGE_TEXT = "Здравствуйте, {firstname} {lastname}!"

SIGN_OUT_BUTTON_XPATH = "//*[contains(text(), 'Выход')]"

# Feedback locators
FEEDBACK_BUTTON_XPATH = '//a[contains(text(), "Обратная связь")]'
FEEDBACK_NAME_XPATH = '//input[@name="name" and @id="name"]'
FEEDBACK_EMAIL_XPATH = '//input[@name="email" and @id="email"]'
FEEDBACK_PHONE_XPATH = '//input[@name="telephone" and @id="telephone"]'
FEEDBACK_COMMENT_XPATH = '//*[@name="comment" and @id="comment"]'
SEND_FEEDBACK_BUTTON_XPATH = '//button[@title="Отправить" and @class="button"]'
FEEDBACK_MESSAGE_TEXT = "Спасибо за ваше обращение с комментариями и вопросами. Мы ответим вам очень скоро."
FEEDBACK_MESSAGE_XPATH = f'//div[contains(text(),"{FEEDBACK_MESSAGE_TEXT}")]'