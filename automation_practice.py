###Login to the website => select women evening dress => select colour and sieze => add item to the basket => checkout"
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver import ActionChains, DesiredCapabilities

# WRITE HERE YOUR USER LOGIN
user_login = "***"

# WRITE HERE YOUR PASSWORD
user_password = "***"


website_url = "http://automationpractice.com/index.php"

# #create Firefox session
driver = webdriver.Firefox()
driver.get(website_url)
wait = WebDriverWait(driver, 5)

#create Chrome session:
# driver = webdriver.Chrome()
# driver.get(website_url)
# wait = WebDriverWait(driver, 5)

#login to the store
login_button = driver.find_element_by_link_text("Sign in")
login_button.click()

login = driver.find_element_by_id("email")
login.clear()
login.send_keys(user_login)

password = driver.find_element_by_id("passwd")
password.clear()
password.send_keys(user_password)

#click Submit button
sign_in = driver.find_element_by_id("SubmitLogin")
sign_in.click()


assert driver.find_element_by_link_text("Sign out")
account_info = driver.find_element_by_css_selector(".info-account")
print(account_info.text)


#from menu select women > dresses > evening dresses
women_clothes = driver.find_element_by_link_text("Women")
hover = ActionChains(driver).move_to_element(women_clothes)
hover.perform()

evening_dresses = WebDriverWait(driver, 1).until(condition.element_to_be_clickable((By.LINK_TEXT,"Evening Dresses"))).click()

assert driver.find_elements_by_css_selector(".content_scene_cat_bg")

#Choose "printed dress" and pick colour beige dress in M size, and add to basket
beige_dress = driver.find_element_by_id("color_16").click()
dress_size = driver.find_element_by_id("group_1").click()
dress_size_M = WebDriverWait(driver, 2).until(condition.element_to_be_clickable((By.CSS_SELECTOR,
            "#group_1 > option:nth-child(2)"))).click()
add_to_cart = driver.find_element_by_css_selector("button.exclusive").click()

#proceed to checkout
proceed_to_checkout = WebDriverWait(driver, 1).until(condition.element_to_be_clickable((By.CSS_SELECTOR,
                    "a.btn:nth-child(2) > span:nth-child(1)"))).click()

assert driver.find_elements_by_css_selector("#cart_title")

proceed_to_checkout_cart_summary = driver.find_element_by_css_selector(".standard-checkout > span:nth-child(1)").click()
comment_about_order = driver.find_element_by_css_selector("textarea.form-control").send_keys("Pack it like a christmas gift")
proceed_to_checkout_addresses = driver.find_element_by_css_selector("button.button:nth-child(4)").click()

terms_of_service = driver.find_element_by_css_selector("#cgv").click()
proceed_to_checkout_shipping = driver.find_element_by_css_selector("button.button:nth-child(4)").click()

assert driver.find_element_by_css_selector(".page-heading")

#pay by bank wire
pay_by_bank_wire = driver.find_element_by_css_selector(".bankwire").click()

#confirm order
confirm_order = driver.find_element_by_css_selector("button.button-medium").click()

#order confirmation
assert driver.find_element_by_css_selector(".cheque-indent > strong:nth-child(1)")


driver.quit()
