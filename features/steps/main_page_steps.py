from behave import given, when, then


@given('I am on main page')
def main_page(context):
    main_page = context.browser
    main_page.get('http://www.ubs.com')

    assert main_page.title == "UBS financial services around the globe | Global topics"

    try:
        main_page.implicitly_wait(10)
        main_page.switch_to_frame(0)
        click = main_page.find_element_by_class_name("actionbutton__txtbody")
        click.click()
    except:
        print "No cookies pop up exist"


@when('I click "{tab_name}" tab and choose "{sub_tab_name}" section')
def clicking_tab(context, tab_name, sub_tab_name):
    main_page = context.browser
    tab_name = "//*[@id='mainmenu']//*[contains(text(), '{}') ]".format(tab_name)
    main_page.find_element_by_xpath(tab_name).click()
    sub_tab_name = "//*[@id='mainmenu']//*[contains(text(), '{}') ]".format(sub_tab_name)
    main_page.find_element_by_xpath(sub_tab_name).click()


@then('Page "{page_name}" is loaded')
def check_page(context, page_name):
    main_page = context.browser

    assert main_page.title == "{} | UBS Global topics".format(page_name)
