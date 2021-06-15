from re import A
from time import sleep
from selenium import webdriver

def subscribe_and_like(login, password, link, posts):
    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(login)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(5)

    browser.get(link)
    subscribe_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
    subscribe_button.click()

    sleep(1)

    for i in range(len(posts)):
        browser.get(posts[i])
        like_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button")
        like_button.click()
        sleep(0.5)


    sleep(5)

    browser.close()