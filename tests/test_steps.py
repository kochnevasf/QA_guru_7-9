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

