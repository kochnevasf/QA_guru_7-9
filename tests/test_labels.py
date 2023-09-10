mport allure
from allure import step
from selene import browser, by, be


@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Задача отображается на странице, тест lambda steps")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'github')
def test_github_issue_name():
    with step("Open github main page"):
        browser.open('')

     with step("Insert 'eroshenkoam/allure-example' to the searchbar"):
        browser.element('.search-input').click()
        browser.element('.QueryBuilder-Input').type(
            'eroshenkoam/allure-example'
        ).press_enter()

    with step("Find 'eroshenkoam/allure-example' among search results and open it"):
        browser.element('[data-testid=results-list]').element(
            by.link_text('eroshenkoam/allure-example')
        ).click()

    with step("Open tab Issues"):
        browser.element('#issues-tab').click()

     with step("Issue 'issue_to_test_allure_report' is shown on the page"):
        browser.element(by.text('issue_to_test_allure_report')).should(be.visible)



""""
import allure
from allure_commons.types import Severity


def test_no_labels():
    pass


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
