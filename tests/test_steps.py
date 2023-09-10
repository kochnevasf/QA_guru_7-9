import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure import step
from selene import browser, by, be


@step("Open github main page")
def open_default_browser_page():
    browser.open('')


@step("Insert {repo} to the searchbar")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('.QueryBuilder-Input').type(repo).press_enter()


@step("Find {repo} among search results and open it")
def open_repository(repo):
    browser.element('[data-testid=results-list]').element(by.link_text(repo)).click()


@step("Open tab Issues")
def open_issues_tab():
    browser.element('#issues-tab').click()


@step("Issue {issue} is shown on the page")
def assert_issue_name_is_present(issue):
    browser.element(by.text(issue)).should(be.visible)

@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Задача отображается на странице, тест decorator steps")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'github')
def test_github_issue_name():
    open_default_browser_page()

    search_for_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()

    assert_issue_name_is_present('issue_to_test_allure_report')

"""
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()

# allure/bin/allure.bat serve tests/allure-results
