import os
from selene import browser
from selene import have


def test_filling_form_valid_data_successful_submitting(init_browser):
    browser.open("/")

    browser.element('#firstName').type('User')
    browser.element('#lastName').type('Test')
    browser.element('#userEmail').type('test@ya.ru')
    browser.element('#gender-radio-2').execute_script('element.click()')
    browser.element('#userNumber').type('7123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('September')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('2001')).click()
    browser.all('.react-datepicker__day').element_by(have.text('5')).click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#hobbies-checkbox-2').execute_script('element.click()')
    browser.element('#uploadPicture').type(f'{os.getcwd()}/Grogu.jpg')

    browser.element('#currentAddress').type('Bolshaya Sadovaya Street 302-bis')
    browser.element('#state').click()
    browser.all('#state div').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text('Delhi')).click()

    browser.element('footer').execute_script('element.remove()')
    browser.element('#submit').execute_script('element.click()')

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element("//td[text()='Student Name']/following-sibling::*").should(have.exact_text('User Test'))
    browser.element("//td[text()='Student Email']/following-sibling::*").should(have.exact_text('test@ya.ru'))
    browser.element("//td[text()='Gender']/following-sibling::*").should(have.exact_text('Female'))
    browser.element("//td[text()='Mobile']/following-sibling::*").should(have.exact_text('7123456789'))
    browser.element("//td[text()='Date of Birth']/following-sibling::*").should(have.exact_text('05 September,2001'))
    browser.element("//td[text()='Subjects']/following-sibling::*").should(have.exact_text('Computer Science'))
    browser.element("//td[text()='Hobbies']/following-sibling::*").should(have.exact_text('Reading'))
    browser.element("//td[text()='Picture']/following-sibling::*").should(have.exact_text('Grogu.jpg'))
    browser.element("//td[text()='Address']/following-sibling::*").should(have.exact_text('Bolshaya Sadovaya Street 302-bis'))
    browser.element("//td[text()='State and City']/following-sibling::*").should(have.exact_text('NCR Delhi'))



