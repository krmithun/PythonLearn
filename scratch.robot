*** Settings ***
Library     SeleniumLibrary




*** Variables ***
${var1}     10

*** Keywords ***
Addition
    [Tags]   Test addition
    [Arguments]    ${num1}     ${num2}
    Log to console  ${num1}

*** Test Cases ***

Suite setup
    set selenium speed  2
    open browser    http://thedemosite.co.uk/


Test database page
    wait until page contains element    //a[contains(text(),'2. The Database')]
    Click Element  //a[contains(text(),'2. The Database')]
    wait until page contains element    //strong[contains(text(),'2. The Database')]
    go back


Suite Teardown
    close all browsers

