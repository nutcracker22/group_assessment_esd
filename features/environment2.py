import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
#from sites import app
import time


def choose_webdriver(context):
    driver_input = input("We provided you with two webdriver options, which are located in the folder features/driver. "
                     "Please ensure, that your webdriver of choice suits your browser version before continuing."
                     "Which webdriver would you like to use. Please enter c for Chromedriver and g for geckodriver: ")
    if driver_input.lower() == "c":
        # Use the chrome driver specific to your version of Chrome browser and put it in ./driver directory
        DRIVER_PATH = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')

        options = ChromeOptions()
        # comment out the line below if you want to see the browser launch for tests
        # possibly add time.sleep() if required
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        context.browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    elif driver_input.lower() == "g":
        DRIVER_PATH = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'geckodriver')
        options = FirefoxOptions()
        context.browser = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)
    else:
        nonsense = input("You have not entered a valid choice. Please press ENTER to start again: ")
        choose_webdriver(context)


def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    #context.browser = driver
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    time.sleep(3)
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()

