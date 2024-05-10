import time

import pyotp
from selenium import webdriver
from selenium.webdriver.common.by import By


def enter_email(driver: webdriver.Chrome, uid: str, sleep: int = 1) -> None:
    while True:
        email = driver.find_elements(By.ID, "email")
        if email:
            email[0].send_keys(uid)
            return
        else:
            time.sleep(sleep)
            continue


def enter_password(driver: webdriver.Chrome, pwd: str, sleep: int = 1) -> None:
    while True:
        password = driver.find_elements(By.ID, "pass")
        if password:
            password[0].send_keys(pwd)
            return
        else:
            time.sleep(sleep)
            continue


def enter_login(driver: webdriver.Chrome, sleep: int = 1) -> None:
    while True:
        loginbutton = driver.find_elements(By.ID, "loginbutton")
        if loginbutton:
            loginbutton[0].click()
            return
        else:
            time.sleep(sleep)
            continue


def enter_twofactor_1(driver: webdriver.Chrome, twofa: str, sleep: int = 1) -> None:
    while True:
        logincode = driver.find_elements(By.ID, "approvals_code")
        if logincode:
            totp = pyotp.TOTP(twofa)
            code = totp.now()
            logincode[0].send_keys(code)
            return
        else:
            time.sleep(sleep)
            continue


def enter_twofactor_2(driver: webdriver.Chrome, sleep: int = 1) -> None:
    while True:
        submitbutton = driver.find_elements(By.ID, "checkpointSubmitButton")
        if submitbutton:
            submitbutton[0].click()
            return
        else:
            time.sleep(sleep)
            continue


def enter_twofactor_3(driver: webdriver.Chrome) -> None:
    submitbutton = driver.find_elements(By.ID, "checkpointSubmitButton")
    if submitbutton:
        submitbutton[0].click()
    submitbutton = driver.find_elements(By.ID, "checkpointSubmitButton")
    if submitbutton:
        submitbutton[0].click()
    submitbutton = driver.find_elements(By.ID, "checkpointSubmitButton")
    if submitbutton:
        submitbutton[0].click()
    submitbutton = driver.find_elements(By.ID, "checkpointSubmitButton")
    if submitbutton:
        submitbutton[0].click()


if __name__ == "__main__":
    uid, pwd, twofa = "uid|pass|2fa".split("|")
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login.php")
    enter_email(driver, uid)
    enter_password(driver, pwd)
    enter_login(driver)
    enter_twofactor_1(driver, twofa)
    enter_twofactor_2(driver)
    enter_twofactor_3(driver)
    time.sleep(5)
