*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${NEW BOOK URL}  http://${SERVER}/new
${NEW BLOG URL}  http://${SERVER}/new_blog
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

Go To New Book Page
    Go To  ${NEW BOOK URL}

Go To New Blog Page
    Go To  ${NEW BLOG URL}


New Book Page Should Be Open
    Title Should Be  Uusi kirjavinkki

Go To Lista Page
    Go To  ${LISTA URL}

List Page Should Be Open
    Title Should Be  Lukuvinkit

Error Page Should Be Open
    Title Should Be  Virhe

Input Book Info
    [Arguments]  ${otsikko}  ${kirjoittaja}  ${isbn}  ${kommentti}
    Input Text  otsikko  ${otsikko}
    Input Text  kirjoittaja  ${kirjoittaja}
    Input Text  isbn  ${isbn}
    Input Text  kommentti  ${kommentti}

Input Blog Info
    [Arguments]  ${nimi}  ${kirjoittaja}  ${url}  ${kommentti}
    Input Text  nimi  ${nimi}
    Input Text  kirjoittaja  ${kirjoittaja}
    Input Text  url  ${url}
    Input Text  kommentti  ${kommentti}


Submit vinkki
    Click Button  Luo vinkki


