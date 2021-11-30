*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${NEW URL}  http://${SERVER}/new
${LISTA URL}  http://${SERVER}/list


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Title Should Be  Etusivu

Go To New Page
    Go To  ${NEW URL}

New Page Should Be Open
    Title Should Be  Uusi lukuvinkki

Go To Lista Page
    Go To  ${LISTA URL}

List Page Should Be Open
    Title Should Be  Lukuvinkit

Input Title
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Submit lukuvinkki
    Click Button  Luo vinkki
