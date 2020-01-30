from selenium import webdriver


def before_all(context):
    try:
        if context.config.userdata["browser"] == 'Chrome':
            print "33"
            context.browser = webdriver.Chrome()
        elif context.config.userdata["browser"] == 'Firefox':
            context.browser = webdriver.Firefox()
        elif context.config.userdata["browser"] == 'Safari':
            context.browser = webdriver.Safari()
    except:
        print "No browser specified. Run default one"
        context.browser = webdriver.Edge()

    context.browser.set_page_load_timeout(30)
    context.browser.implicitly_wait(30)
    context.browser.maximize_window()


def after_all(context):
    context.browser.quit()

