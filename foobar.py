from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os


def FOOBAR_FOUND():
    try:
        driver.find_element_by_link_text('I want to play').click()
    except NoSuchElementException:
        return False
    return True


'''
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
'''

driver = webdriver.Chrome("chromedriver.exe")
# python list comprehension page 1
GOOGLE_PYTHON1 = "https://www.google.co.in/search?q=python+list++comprehension&ei=Fav9XoXTBoSdsAe_lrXADg&start=0&sa=N&ved=2ahUKEwjFsYveoq7qAhWEDuwKHT9LDeg4FBDy0wN6BAgMEC4&biw=1366&bih=613"

# python list comprehension page 3
GOOGLE_PYTHON2 = 'https://www.google.co.in/search?q=python+list++comprehension&biw=1366&bih=613&ei=JKv9XtCjD8y0kgXOpI3gCQ&start=20&sa=N&ved=2ahUKEwjQxafloq7qAhVMmqQKHU5SA5wQ8tMDegQIEhAx'

# C++ move semantics page 1
GOOGLE_CPP = 'https://www.google.com/search?q=C%2B%2B+move+semantics&oq=C%2B%2B+move+semantics&aqs=chrome..69i57.5476j0j7&sourceid=chrome&ie=UTF-8'

# C++ move semantics page 3
GOOGLE_CPP1 = 'https://www.google.co.in/search?q=C%2B%2B+move+semantics&ei=_6z9XuHRH5KQrgTTqpaACg&start=20&sa=N&ved=2ahUKEwihzffHpK7qAhUSiIsKHVOVBaAQ8tMDegQIDhAx'

# araylist java page 1
GOOGLE_JAVA = 'https://www.google.com/search?sxsrf=ALeKk02kqXhdOjIsvoeHhrk9j-H_T3KtPA:1593684836188&q=arraylist+java&spell=1&sa=X&ved=2ahUKEwjKwq3Uqq7qAhVCCuwKHX4XBEEQBSgAegQIDhAn&biw=1366&bih=625'

# arraylist java page 3
GOOGLE_JAVA1 = 'https://www.google.com/search?q=arraylist+java&sxsrf=ALeKk02exe263QYiISd_brrx0_nzQPaq7w:1593684939325&ei=y7P9XuqgE4OYkwWKx7ioBQ&start=10&sa=N&ved=2ahUKEwiqssSFq67qAhUDzKQKHYojDlUQ8tMDegQIDRAt&biw=1366&bih=625'

driver.get(GOOGLE_PYTHON1)

# driver.find_element_by_xpath('//*[@id="xjs"]/div/table/tbody/tr/td[4]/a').send_keys(Keys.CONTROL + Keys.ENTER)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(GOOGLE_CPP)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get(GOOGLE_JAVA)

i = 0
j = 0
while not FOOBAR_FOUND():
    print("searching...")
    driver.switch_to.window(driver.window_handles[i])
    if FOOBAR_FOUND():
        print("__FOUND__")
        break
    if j == 0:
        driver.get(GOOGLE_PYTHON2)
    elif j == 1:
        driver.get(GOOGLE_CPP1)
    elif j == 2:
        driver.get(GOOGLE_PYTHON1)
    elif j == 3:
        driver.get(GOOGLE_CPP)
    elif j == 4:
        driver.get(GOOGLE_JAVA1)
    else:
        driver.get(GOOGLE_JAVA)
    i = (i + 1) % 3
    j = (j + 1) % 6
