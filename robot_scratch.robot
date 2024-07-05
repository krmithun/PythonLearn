*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot

*** Variables ***
${URL}      https://example.com
${BROWSER}  chrome

*** Test Cases ***
Open Browser and Verify Title
    [Documentation]  Open the browser, navigate to the website, and verify the page title
    Open Browser To Login Page
    Verify Page Title    Example Domain
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    css:h1
