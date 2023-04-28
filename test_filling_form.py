import os
from selene import browser
from selene import have


def test_filling_form_valid_data_successful_submitting():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    browser.element('#firstName').type('Kate')
    browser.element('#lastName').type('Voronova')
    browser.element('#userEmail').type('test@ya.ru')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('7123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value = "8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value = "1985"]').click()
    browser.element('//div[@class="react-datepicker__month"]//div[text()=5]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').type(f'{os.getcwd()}/Grogu.jpg')
    browser.element('#currentAddress').type('Bolshaya Sadovaya Street 302-bis')
    browser.element('#state').click()
    browser.element('//div[@id="state"]//div[text()="NCR"]').click()
    browser.element('#city').click()
    browser.element('//div[@id="city"]//div[text()="Delhi"]').click()
    browser.element('#submit').click()
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))



