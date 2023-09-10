import allure
from selene import browser, by, be


@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Задача отображается на странице, тест selen")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'github')
def test_github_issue_name():
    browser.open('')

    browser.element('.search-input').click()
    browser.element('.QueryBuilder-Input').type('eroshenkoam/allure-example').press_enter()

    browser.element('[data-testid=results-list]').element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()
    browser.element(by.text('issue_to_test_allure_report')).should(be.visible)




"""
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_ya():
    browser.open("https://ya.ru")
    print("ya");
def test_github():
    browser.open("https://github.com")


    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
"""

