import os
import time
import logging
from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.lenovo.com/ar/es/araff/gatekeeper/showpage?toggle=PasscodeGatekeeper"


def send_email(to_address):
    logging.info(f"Sending email to '{to_address}'")
    message = Mail(
        from_email=os.environ.get('FROM_ADDRESS'),
        to_emails=to_address,
        subject='[Bot] Legion 5 is available!',
        html_content=f"Please check stock <a href={URL}>here</a>, use this code: {os.environ.get('COUPON_CODE')}")
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        logging.info(f"Email sent, status code = {response.status_code}")
    except Exception as e:
        logging.error(e.message)


def load_lenovo_page():
    logging.info("Loading Lenovo page...")
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    op.add_argument("--log-level=3")

    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=op)
    driver.get(URL)
    driver.find_element(By.ID, "gatekeeper.passcode.id").click()
    element = driver.find_element(By.CSS_SELECTOR, ".button-called-out")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.ID, "gatekeeper.passcode.id").send_keys(os.environ.get('COUPON_CODE'))
    driver.find_element(By.CSS_SELECTOR, ".button-called-out").click()
    logging.info("Loaded Lenovo page successfully")
    return driver


def check_stock(driver):
    logging.info(" CHECKING STOCK ".center(50, '*'))
    elements = driver.find_elements(By.CSS_SELECTOR, ".rci-msg")
    if len(elements) > 0 and driver.find_element(By.CSS_SELECTOR, ".rci-msg").text == "Out of Stock":
        send_email(os.environ.get('TO_ADDRESS'))
        logging.info("Hurry up, buy it now!")
        return True
    logging.info("Still out of stock :(")
    return False


def init_config():
    load_dotenv()
    logging.basicConfig(level=os.environ.get('LOGGING_LEVEL'),
                        format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def main():
    init_config()
    logging.info(" STARTING LENOVO WATCHDOG ".center(100, '*'))
    try:
        driver = load_lenovo_page()
        while not check_stock(driver):
            driver.refresh()
            time.sleep(int(os.environ.get('REFRESH_INTERVAL')))
        driver.quit()
    except Exception as e:
        logging.error(f"Ups! Something went wrong: {e}")
    logging.info(" FINISHED LENOVO WATCHDOG ".center(100, '*'))

main()
